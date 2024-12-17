# Machine Learning para Preços de Imóveis e Notas de Estudantes

Este repositório contém dois projetos de aprendizado de máquina que utilizam modelos de regressão linear para prever:

1. **Preços de imóveis** com base em suas características.
2. **Notas de estudantes** com base em suas horas de estudo.

## Projeto 1: Previsão de Preços de Imóveis

**Descrição:** Este projeto visa construir um modelo preditivo para estimar o preço de imóveis utilizando Regressão Linear. O modelo utiliza um conjunto de dados de imóveis com diferentes características para treinar e, em seguida, prever o preço de novos imóveis.

**Tecnologias utilizadas:**

* Python
* Pandas (para manipulação e análise de dados)
* Scikit-learn (para construção e avaliação do modelo de regressão)
* Statsmodels (para análise estatística mais aprofundada, como o cálculo do VIF)
* Matplotlib e Seaborn (para visualização dos dados e resultados)
* Plotly (para visualizações interativas)
* NumPy (para operações numéricas)

**Descrição detalhada:**

O projeto começa com uma análise exploratória dos dados (EDA), incluindo a verificação de correlações entre as variáveis e a distribuição do preço de venda. Em seguida, os dados são divididos em conjuntos de treinamento e teste. Um modelo de Regressão Linear é treinado usando o conjunto de treinamento e avaliado usando o conjunto de teste. Métricas como R² são usadas para avaliar o desempenho do modelo. O projeto também investiga a multicolinearidade entre as variáveis preditoras usando o Variance Inflation Factor (VIF). Por fim, o modelo é usado para prever os preços de novos imóveis.

## Projeto 2: Previsão de Notas de Estudantes

**Descrição:** Este projeto tem como objetivo prever as pontuações de testes de estudantes com base em suas horas de estudo, utilizando um modelo de Regressão Linear.

**Tecnologias utilizadas:**

* Python
* Pandas (para manipulação e análise de dados)
* Scikit-learn (para construção e avaliação do modelo de regressão, incluindo métricas como R², MAE, MSE e RMSE)
* Scipy.stats (para testes de normalidade como Shapiro-Wilk e Kolmogorov-Smirnov, e para o gráfico QQ Plot)
* Matplotlib e Seaborn (para visualização de dados e resultados)
* Joblib (para salvar o modelo treinado)

**Descrição detalhada:**

O projeto carrega um conjunto de dados contendo as horas de estudo e as pontuações dos testes dos estudantes. Após o carregamento, é realizada uma análise exploratória dos dados (EDA) para entender a distribuição dos dados e a relação entre as variáveis.  Um modelo de Regressão Linear é treinado com os dados de treinamento. O desempenho do modelo é avaliado usando métricas como R², Erro Absoluto Médio (MAE), Erro Quadrático Médio (MSE) e Raiz do Erro Quadrático Médio (RMSE). Os resíduos do modelo são analisados para verificar a linearidade e a homocedasticidade (variância constante dos erros).  Testes de normalidade, como Shapiro-Wilk e Kolmogorov-Smirnov, são aplicados aos resíduos, e um gráfico QQ plot é gerado para verificar visualmente a normalidade. Finalmente, o modelo treinado é salvo usando a biblioteca `joblib` para uso posterior.

## Observações

* Os dados utilizados nos projetos são simplificados para fins didáticos.
* A performance do modelo pode ser melhorada com a utilização de técnicas mais avançadas e com a inclusão de mais dados.
