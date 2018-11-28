#include <stdio.h>
#include <stdlib.h>

int CheckPotencia(long long number)
{
    if (number < 2)
        return 0;
    else
        return (CheckPotencia(number/2) + 1);
}

/*long long GetMin(long long number, long long contador)
{
    if (contador == 0)
        return (llabs((number - 1)/2));
    else
        return GetMin((number - 1)/2, (contador - 1));
}

long long GetMax(long long number, long long numStalls)
{
    if (number == 0)
        return numStalls - 1;
    else if (number%2 == 0)
        return (GetMin(numStalls, CheckPotencia(number/2)) - GetMin(numStalls, CheckPotencia(number)) - 1);
    else
        return (GetMax(number/2, numStalls) - GetMin(numStalls, CheckPotencia(number)) - 1);
}*/

long long GetNumerador(int contador)
{
    if (contador == 0)
        return 1;
    else
        return (2 * GetNumerador(contador - 1));
}


int main ()
{
    int i = 0;
    int potencia = 0;
    int numTestCases = 0;
    long long numStalls = 0;
    long long numPeople = 0;
    long long minimum = 0;
    long long maximum = 0;
    long long numerador = 0;
    long long tamanho = 0;

    FILE *entrada;
    FILE *saida;

    entrada = fopen("sample.in", "r");
    saida = fopen("large_output.txt", "w");

    fscanf(entrada, " %d", &numTestCases);

    for(i = 1; i < numTestCases + 1; i ++)
    {
        fscanf(entrada, " %lld %lld", &numStalls, &numPeople);
        potencia = CheckPotencia(numPeople);
        numerador = GetNumerador(potencia);
        if ((numStalls - (numPeople - 1))%numerador == 0)
            tamanho = (numStalls - (numPeople - 1))/numerador;
        else
            tamanho = 1 + (numStalls - (numPeople - 1))/numerador;
        minimum = (tamanho - 1)/2;
        maximum = (tamanho - 1) - minimum;
        fprintf(saida, "Case #%d: %lld %lld\n", i, maximum, minimum);
    }

    fclose(entrada);
    fclose(saida);
}
