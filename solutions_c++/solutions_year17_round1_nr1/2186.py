#include<cstdio>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
    char ch;
    char carr[26] = {'\0'};
    int t, r, c, from, til, n;
    FILE *input, *output;

    if (argc != 3)
    {
        printf("input을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    vector<char> row;
    vector<vector<char> > cake;
    vector<int> count;

    for (int i = 1; i <= t; i++)
    {
        fscanf(input, "%d %d", &r, &c);

        cake.clear();
        cake.resize(r);
        count.clear();
        count.resize(r);

        for (int j = 0; j < r; j++)
        {
            cake[j].clear();
            cake[j].resize(c);
            fscanf(input, "%s", carr);
            for (int k = 0; k < c; k++)
                cake[j][k] = carr[k];
        }

        for (int j = 0; j < r; j++)
        {
            n = 0;
            for (int k = 0; k < c; k++)
            {
                if (cake[j][k] != '?')
                    n++;
            }
            count[j] = n;
        }

        for (int j = 0; j < r; j++)
        {
            from = 0;
            til = c;
            if (count[j] != 0)
            {
                while (from != c)
                {
                    for (int k = from; k < c; k++)
                    {
                        if (cake[j][k] != '?')
                        {
                            ch = cake[j][k];
                            til = k + 1;
                            break;
                        }
                        til = c;
                    }

                    for (int k = from; k < til; k++)
                        cake[j][k] = ch;

                    from = til;
                }
            }
        }

        for (int j = 0; j < r; j++)
        {
            for (int k = 0; k < c; k++)
                printf("%c", cake[j][k]);
            printf("\n");
        }

        row.clear();
        row.resize(c);
        from = 0;
        til = c;
        while (from != r)
        {
            for (int j = from; j < r; j++)
            {
                if (count[j] != 0)
                {
                    til = j + 1;
                    for (int k = 0; k < c; k++)
                        row[k] = cake[j][k];
                    break;
                }
                til = r;
            }

            for (int k = from; k < til; k++)
            {
                for (int l = 0; l < c; l++)
                    cake[k][l] = row[l];
            }

            from = til;
        }

        for (int j = 0; j < r; j++)
        {
            for (int k = 0; k < c; k++)
                printf("%c", cake[j][k]);
            printf("\n");
        }

        fprintf(output, "Case #%d:\n", i);
        for (int j = 0; j < r; j++)
        {
            for (int k = 0; k < c; k++)
                fprintf(output, "%c", cake[j][k]);
            fprintf(output, "\n");
        }
    }

    fclose(input);
    fclose(output);

    return 0;
}
