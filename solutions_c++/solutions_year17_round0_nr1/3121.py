#include <bits/stdc++.h>
#include <string.h>

int main ()
{
    int j = 0;
    int i = 0;
    int w = 0;
    bool possible = true;
    int flips = 0;
    int contador = 0;
    int numTestCases = 0;
    char panquecas[1200];

    FILE *entrada;
    FILE *saida;

    entrada = fopen("sample.in", "r");
    saida = fopen("large_output.txt", "w");

    fscanf(entrada, " %d", &numTestCases);

    for(j = 1; j < numTestCases + 1; j ++)
    {
        fscanf(entrada, " %s", panquecas);
        fscanf(entrada, " %d", &flips);

        contador = 0;
        for (i = 0; i <= (strlen(panquecas) - flips); i ++)
            if (panquecas[i] == '-')
            {
                for (w = 0; w < flips; w ++)
                    if (panquecas[i + w] == '-')
                        panquecas[i + w] = '+';
                    else
                        panquecas[i + w] = '-';
                contador ++;
            }

        possible = true;
        for (i = 0; i < flips; i ++)
            if (panquecas[strlen(panquecas) - flips + i] == '-')
                possible = false;

        /*for (i = 0; i < strlen(panquecas); i ++)
            printf("%c", panquecas[i]);
        printf("\n");*/
        if (possible)
            fprintf(saida, "Case #%d: %d\n", j, contador);
        else
            fprintf(saida, "Case #%d: IMPOSSIBLE\n", j);
    }
}
