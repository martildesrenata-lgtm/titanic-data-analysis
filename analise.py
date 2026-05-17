import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando a base diretamente do Seaborn
df = sns.load_dataset('titanic')

# Análise 1: Qual a taxa de sobrevivência por gênero?
survival_gender = df.groupby('sex')['survived'].mean() * 100

# Análise 2: Qual a taxa de sobrevivência por classe social?
survival_class = df.groupby('class')['survived'].mean() * 100

print(f"Taxa de sobrevivência - Mulheres: {survival_gender['female']:.2f}%")
print(f"Taxa de sobrevivência - Homens: {survival_gender['male']:.2f}%")
print("\nTaxa de sobrevivência por Classe:")
print(survival_class)

# Visualização simples
sns.barplot(data=df, x='class', y='survived', hue='sex')
plt.title('Sobrevivência por Classe e Gênero (Titanic)')
plt.show()
