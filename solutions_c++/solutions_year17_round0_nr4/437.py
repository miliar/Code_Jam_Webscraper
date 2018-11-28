#include <stdio.h>
#include <vector>
typedef struct node node;
struct node
{
    char s;
    int r, c;
};
int main()
{
    freopen("D-small-attempt3.in", "r", stdin);
    freopen("D-small-attempt3.out", "w", stdout);
    freopen("D-error.out", "w", stderr);
    int T, t;
    scanf("%d", &T);
    int N, M;
    char S[100][100];
    int row[100], col[100];
    int plus[200], minus[200];
    int i, j, k, l;
    std::vector<node> V;
    node p;
    int found, v, points;
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &M);
        fprintf(stderr, "Case #%d: Input %d %d\n", t, N, M);
        V.clear();
        points = 0;
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                S[i][j] = '.';
        for (i = 0; i < N; i++)
            row[i] = 0;
        for (i = 0; i < N; i++)
            col[i] = 0;
        for (i = 0; i < 2*N; i++)
            plus[i] = 0;
        for (i = 0; i < 2*N; i++)
            minus[i] = 0;
        for (i = 0; i < M; i++)
        {
            scanf(" %c %d %d", &p.s, &p.r, &p.c);
            p.r--;
            p.c--;
            S[p.r][p.c] = p.s;
            if (p.s != '+')
            {
                row[p.r]++;
                col[p.c]++;
                points++;
            }
            if (p.s != 'x')
            {
                plus[p.r + p.c]++;
                minus[p.r - p.c + N]++;
                points++;
            }
        }

        //fill 1 o
        found = 0;
        for (i = 0; i < N; i++)
        {
            for (j = 0; j < N; j++)
            {
                if (S[i][j] == 'o')
                {
                    found = 3;
                    break;
                }
                found = 0;
                if ((row[i] == 0 && col[j] == 0) || (S[i][j] == 'x' && row[i] == 1 && col[j] == 1)) found++;
                if ((plus[i + j] == 0 && minus[i - j + N] == 0) || (S[i][j] == '+' && plus[i + j] == 1 && minus[i - j + N] == 1)) found++;
                if (found >= 2)
                    break;
            }
            if (found >= 2)
                break;
        }
        if (found == 2)
        {
            if (S[i][j] == '.')
                points += 2;
            else
                points++;
            if (S[i][j] != 'x')
            {
                row[i]++;
                col[j]++;
            }
            if (S[i][j] != '+')
            {
                plus[i + j]++;
                minus[i - j + N]++;
            }
            S[i][j] = 'o';
            V.push_back({'o', i, j});
            //fprintf(stderr, "o %d %d\n", i, j);
        }
        //fill +
        //printf("fill +\n");
        do
        {
            found = 0;
            for (k = 0; k < 2*N; k++)
            {
                if (k < N)
                {
                    for (l = -N; l <= N; l++)
                    {
                        i = (k + l)/2;
                        j = (k - l)/2;
                        //fprintf(stderr, "%d %d\n", i, j);
                        if (i < 0 || i >= N || j < 0 || j >= N) continue;
                        if (S[i][j] != '.') continue;
                        found = 0;
                        if (plus[i + j] == 0 && minus[i - j + N] == 0) found++;
                        if (found == 1)
                            break;
                    }
                    if (found == 1)
                        break;
                }
                else
                {
                    for (l = N; l >= -N; l--)
                    {
                        i = (k + l)/2;
                        j = (k - l)/2;
                        //fprintf(stderr, "%d %d\n", i, j);
                        if (i < 0 || i >= N || j < 0 || j >= N) continue;
                        if (S[i][j] != '.') continue;
                        found = 0;
                        if (plus[i + j] == 0 && minus[i - j + N] == 0) found++;
                        if (found == 1)
                            break;
                    }
                    if (found == 1)
                        break;
                }
            }
            /*for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                {
                    if (S[i][j] != '.') continue;
                    found = 0;
                    if (plus[i + j] == 0 && minus[i - j + N] == 0) found++;
                    if (found)
                        break;
                }
                if (found)
                    break;
            }*/
            if (found == 1)
            {
                points++;
                plus[i + j]++;
                minus[i - j + N]++;
                S[i][j] = '+';
                V.push_back({'+', i, j});
                //fprintf(stderr, "+ %d %d\n", i, j, plus[i + j], minus[i - j + N]);
            }
            /*for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                    printf("%c", S[i][j]);
                printf("\n");
            }
            printf("\n");*/
        } while (found);
        //fill x
        //printf("fill x\n");
        do
        {
            //v = V.size();
            found = 0;
            for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                {
                    if (S[i][j] != '.') continue;
                    found = 0;
                    if (row[i] == 0 && col[j] == 0) found++;
                    if (found)
                        break;
                }
                if (found)
                    break;
            }
            if (found)
            {
                points++;
                row[i]++;
                col[j]++;
                S[i][j] = 'x';
                V.push_back({'x', i, j});
                //fprintf(stderr, "x %d %d\n", i, j);
            }
            /*for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                    printf("%c", S[i][j]);
                printf("\n");
            }
            printf("\n");*/
        } while (found);
        //fill o
        //printf("fill o\n");
        do
        {
            found = 0;
            for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                {
                    if (S[i][j] == 'o') continue;
                    found = 0;
                    if ((row[i] == 0 && col[j] == 0) || (S[i][j] == 'x' && row[i] == 1 && col[j] == 1)) found++;
                    if ((plus[i + j] == 0 && minus[i - j + N] == 0) || (S[i][j] == '+' && plus[i + j] == 1 && minus[i - j + N] == 1)) found++;
                    if (found == 2)
                        break;
                }
                if (found == 2)
                    break;
            }
            if (found == 2)
            {
                if (S[i][j] == '.')
                    points += 2;
                else
                    points++;
                if (S[i][j] != 'x')
                {
                    row[i]++;
                    col[j]++;
                }
                if (S[i][j] != '+')
                {
                    plus[i + j]++;
                    minus[i - j + N]++;
                }
                S[i][j] = 'o';
                found = 0;
                for (k = 0; k < V.size(); k++)
                {
                    if (V[k].r == i && V[k].c == j)
                    {
                        V[k].s = 'o';
                        found = 2;
                    }
                }
                if (!found)
                {
                    V.push_back({'o', i, j});
                    found = 2;
                }
                //fprintf(stderr, "o %d %d\n", i, j);
            }
            /*for (i = 0; i < N; i++)
            {
                for (j = 0; j < N; j++)
                    printf("%c", S[i][j]);
                printf("\n");
            }
            printf("\n");*/
        } while (found == 2);

        printf("Case #%d: %d %d\n", t, points, V.size());
        for (i = 0; i < V.size(); i++)
            printf("%c %d %d\n", V[i].s, V[i].r + 1, V[i].c + 1);

        fprintf(stderr, "Output %d %d\n", points, V.size());
        if (points != 3*N - 2)
            fprintf(stderr, "SHIT\n");
        for (i = 0; i < N; i++)
        {
            for (j = 0; j < N; j++)
                fprintf(stderr, "%c", S[i][j]);
            fprintf(stderr, "\n");
        }
    }
}
