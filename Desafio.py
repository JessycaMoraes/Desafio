#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd

# In[2]:
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas

# In[3]:
#leitura planilha1
sheet1 = pd.read_excel('/home/jessyca/Área de Trabalho/dados.xlsx', sheet_name=0, index_col=0)

# In[4]:
#leitura planilha2
sheet2 = pd.read_excel('/home/jessyca/Área de Trabalho/dados.xlsx', sheet_name=1, index_col=0)

# In[5]:
#apaga primeira linha planilha1
sheet1.columns = [''] * len(sheet1.columns)
sheet1

# In[6]:
#transpor tabela planilha1
sheet1 = sheet1.T
sheet1

# In[7]:
#renomear colunas planilha1
sheet1.columns = ['mês','realizado']
sheet1

# In[8]:
#merge da planilha 1 e 2
resultado = sheet2.merge(sheet1, on='mês', how='left')
resultado

# In[9]:
#calculo da diferenca entre as colunas orcado e realizado
resultado['diff'] = resultado['orcado'] - resultado['realizado']
resultado

# In[10]:
#arquivo de saida em csv
export_csv = resultado.to_csv ('/home/jessyca/Documentos/Desafio/resultado.csv', index = None, header=True)

# In[11]:
#cria gráfico
ind = np.arange(12)
plt.figure(figsize=(18,8))

p1 = plt.bar(ind, resultado['orcado'])
p2 = plt.bar(ind, resultado['realizado'])

plt.xlabel('Mes')
plt.ylabel('$')
plt.title('Gráfico Orçamento')

plt.xticks(ind, resultado['mês'], rotation=0)
plt.yticks(np.arange(0,500, 100))

plt.legend((p1[0], p2[0]), ('Orçado', 'Realizado'))

plt.savefig('/home/jessyca/Documentos/Desafio/grafico.png')
plt.show()
