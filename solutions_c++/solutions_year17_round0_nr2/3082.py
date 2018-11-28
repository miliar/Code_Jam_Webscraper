#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bits/stdc++.h>

long long Elevar (int num, int potencia)
{
    if (potencia == 0)
        return 1;
    else
        return (num * Elevar(num, potencia - 1));
}

int main ()
{
    int i = 0;
    int j = 0;
    bool temZero = false;
    bool botarNove = false;
    int ultimoAlgarismo = -1;
    long long elevado = 0;
    long long number = 0;
    long long resposta = 0;
    int algarismos[20];
    int numTestCases = 0;

    FILE *entrada;
    FILE *saida;

    entrada = fopen("sample.in", "r");
    saida = fopen("large_output.txt", "w");

    fscanf(entrada, " %d", &numTestCases);

    for(j = 1; j < numTestCases + 1; j ++)
    {
        fscanf(entrada, " %lld", &number);

        for (i = 0; i < 19; i ++)
        {
            elevado = Elevar (10, i);
            if (number/elevado < 1)
                algarismos[i] = -1;
            else
                algarismos[i] = (number/elevado)%10;
        }
        algarismos[19] = -1;

        ultimoAlgarismo = -1;
        while (algarismos[ultimoAlgarismo + 1] != -1)
            ultimoAlgarismo ++;

        do
        {
            temZero = false;
            for (i = ultimoAlgarismo; i >= 0; i--)
            {
                if (temZero)
                    algarismos[i] = 9;
                else if (algarismos[i] == 0)
                {
                    algarismos[i] = 9;
                    temZero = true;
                    algarismos[i+1] --;
                    if (i+1 == ultimoAlgarismo && algarismos[i+1] <= 0)
                    {
                        algarismos[i+1] = -1;
                        ultimoAlgarismo --;
                    }
                }
            }
        }
        while(temZero);


        do{
        botarNove = false;
        for (i = ultimoAlgarismo; i > 0; i--)
            if(botarNove)
            {
                algarismos[i] = 9;
                algarismos[0] = 9;
            }
            else if (algarismos[i] > algarismos[i-1])
            {
                algarismos[i] --;
                botarNove = true;
                algarismos[i - 1] = 9;
            }
        }
        while(botarNove);

        resposta = 0;
        for (i = 0; i <= ultimoAlgarismo; i++)
        {
            resposta = resposta + (algarismos[i] * Elevar(10, i));
        }

        fprintf(saida, "Case #%d: %lld\n", j, resposta);

    }
}
