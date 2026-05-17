# Análise de Dados - Titanic 🚢

Este é o meu primeiro projeto de análise de dados utilizando Python. O objetivo foi analisar o famoso dataset do Titanic para entender os fatores que influenciaram a sobrevivência dos passageiros.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas** (Manipulação de dados)
- **Seaborn & Matplotlib** (Visualização de dados)

## 📊 Principais Insights
- **Gênero:** Mulheres tiveram uma taxa de sobrevivência significativamente maior que os homens.
- **Classe:** Passageiros da 1ª classe tiveram prioridade e maior taxa de sobrevivência em comparação com a 3ª classe.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
df = sns.load_dataset('titanic')

# Criando o gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='class', y='survived', hue='sex', palette='viridis')

# Customizando para ficar bonito no LinkedIn
plt.title('Taxa de Sobrevivência no Titanic por Classe e Gênero', fontsize=14)
plt.xlabel('Classe Social', fontsize=12)
plt.ylabel('Proporção de Sobrevivência', fontsize=12)
plt.legend(title='Gênero')

# SALVANDO A IMAGEM
plt.savefig('grafico_titanic.png', dpi=300, bbox_inches='tight')
print("Gráfico salvo como 'grafico_titanic.png'!")

plt.show()
