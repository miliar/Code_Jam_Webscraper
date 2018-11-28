#include <bits/stdc++.h>
#include <string.h>

int main ()
{
    int i = 0;
    int j = 0;
    int w = 0;
    int rows = 0;
    int columns = 0;
    char grid[150][150];
    int aqui= 0;
    bool encontrou = false;
    bool encontrouFull = false;
    bool primeiro= true;

    int numTestCases = 0;
    FILE *entrada;
    FILE *saida;

    entrada = fopen("sample.in", "r");
    saida = fopen("large_output.txt", "w");

    fscanf(entrada, " %d", &numTestCases);

    for (w = 1; w <= numTestCases; w ++)
    {
        for (i = 0; i < 150; i ++)
            for (j = 0; j < 150; j ++)
                grid[i][j] = '.';
        fscanf(entrada, " %d %d", &rows, &columns);

        for (i = 0; i < rows; i ++)
            for(j = 0; j < columns; j ++)
                fscanf(entrada, " %c", &grid[i][j]);



        /*encontrouFull = false;
        primeiro = true;

        for (i = 0; i < rows; i ++)
        {
            encontrou = false;
            for(j = 0; j < columns; j ++)
            {
                if (grid[i][j] != '?')
                    encontrou = true;
            }

            if(!encontrou)
                encontrouFull = true;
        }

        if(encontrouFull)
            primeiro = false;

        if(primeiro)
        {*/
        for (i = 0; i < rows; i ++)
        {
            if (grid[i][0] != '?')
            {
                for (j = 0; j < columns; j ++)
                    if (grid[i][j] == '?')
                        grid[i][j] = grid[i][j-1];
            }
            else
            {
                aqui = 0;
                encontrou = false;
                for (j = 0; j < columns && !encontrou; j++)
                    if (grid[i][j] != '?')
                        {
                            encontrou = true;
                            aqui = j;
                        }
                if (encontrou){
                for (j = 0; j < aqui; j++)
                    grid[i][j] = grid[i][aqui];
                for (j = 0; j < columns; j ++)
                    if (grid[i][j] == '?')
                        grid[i][j] = grid[i][j-1];
                }
            }
        }
        for (i = 0; i < columns; i ++)
        {
            if (grid[0][i] != '?')
            {
                for (j = 0; j < rows; j ++)
                    if (grid[j][i] == '?')
                        grid[j][i] = grid[j-1][i];
            }
            else
            {
                aqui = 0;
                encontrou = false;
                for (j = 0; j < rows && !encontrou; j++)
                    if (grid[j][i] != '?')
                        {
                            encontrou = true;
                            aqui = j;
                        }
                for (j = 0; j < aqui; j++)
                    grid[j][i] = grid[aqui][i];
                for (j = 0; j < rows; j ++)
                    if (grid[j][i] == '?')
                        grid[j][i] = grid[j-1][i];
            }
        }


        fprintf(saida, "Case #%d:\n", w);
        for (i = 0; i < rows; i ++)
        {
            for(j = 0; j < columns; j ++)
                fprintf(saida, "%c", grid[i][j]);
            fprintf(saida, "\n");
        }
    }

    return 0;
}
