import pandas as pd

dff = pd.read_excel('pcc.xls', sheet_name='Sheet1')


df1 = pd.DataFrame({'date': dff['DATE'].tolist(),
                    'ref': dff['DATE'].tolist(),
                    'journal_id': dff['CODE_JRN'].tolist(),
                    'account_id': dff['CODE_COM'].tolist(),
                    'name': dff['LIBELLE'].tolist(),
                    'partner_id': dff['CODE_AUX'].tolist(),
                    'debit': dff['DEBIT'].tolist(),
                    'credit': dff['CREDIT'].tolist(),
                    })

#print(df1)
df1.to_excel(excel_writer = "C:/dev/odoo6.xls" , index=False)