def fees_to_be_paid(fee, on_account_percent = 75, vat_percent = 20):
  vat = fee / 100 * vat_percent
  total = fee + vat
  on_account = total / 100 * on_account_percent
  print('Fee = £' + str(fee))
  print('VAT = ' + str(vat_percent) + '%')
  print('VAT = £' + str(vat))
  print('Total fee = £' + str(total))
  print(str(on_account_percent) + '% of fees to be paid on account = ' + str(on_account))

fees_to_be_paid(250, 75)