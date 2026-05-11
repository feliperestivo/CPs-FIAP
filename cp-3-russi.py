temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior_risco = 0
sala_maior_risco = 0

for i in range(len(temperaturas)): 

    resultado_soma = sum(temperaturas[i])
    media = resultado_soma / 4

    registro_critico = len(
        [temperatura for temperatura in temperaturas[i]
         if temperatura >= 33]
    )

    print(f"Sala {i+1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registro_critico}")
    print()

    if registro_critico > maior_risco:
        maior_risco = registro_critico
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")

