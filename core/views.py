from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from inventory.models import Stock
from parties.models import Party
from sales.models import SalesInvoice


@login_required
def dashboard(request):
    today = date.today()
    todays_sales = SalesInvoice.objects.filter(date=today).aggregate(total=Sum("total"))["total"] or 0
    low_stock_count = sum(1 for s in Stock.objects.select_related("item") if s.quantity <= s.item.reorder_level)
    parties_with_dues = [p for p in Party.objects.all() if p.get_balance() > 0]
    total_receivable = sum((p.get_balance() for p in parties_with_dues), 0)

    context = {
        "todays_sales": todays_sales,
        "low_stock_count": low_stock_count,
        "total_receivable": total_receivable,
        "dues_party_count": len(parties_with_dues),
    }
    return render(request, "dashboard.html", context)
