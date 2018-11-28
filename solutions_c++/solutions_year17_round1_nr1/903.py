#include <bits/stdc++.h>

using namespace std;

/*
int main()
{
    freopen("inp.in", "r", stdin);
    //freopen("outp.out", "w", stdout);

    //ios::sync_with_stdio(false);
    int tc;
    scanf("%d", &tc);
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:\n", case_no);
        //cerr << "Geval " << case_no << " gestart" << endl;
        int nb_rows, nb_cols;
        scanf("%d %d", &nb_rows, &nb_cols);
        vector< vector<char> > field(nb_rows, vector<char>(nb_cols));
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                scanf(" %c", &field[i][j]);
            }
        }

        if(case_no==10) break;
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                printf("%c", field[i][j]);
            }
            printf("\n");
        }
        printf("\n");

        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                if(field[i][j]=='?') continue;
                vector< vector<int> > som(nb_rows, vector<int>(nb_cols, 0));
                for(int a=0; a<nb_rows; a++)
                {
                    for(int b=0; b<nb_cols; b++)
                    {
                        if(field[i][j] != field[a][b] && field[a][b] != '?') som[a][b]++;
                        if(a-1 >= 0)
                        {
                            som[a][b] += som[a-1][b];
                        }
                        if(b-1 >= 0)
                        {
                            som[a][b] += som[a][b-1];
                        }
                        if(a-1 >= 0 && b-1 >= 0)
                        {
                            som[a][b] -= som[a-1][b-1];
                        }
                    }
                }

                cerr << i << " " << j << endl;
                for(int a=0; a<nb_rows; a++)
                {
                    for(int b=0; b<nb_cols; b++)
                    {
                        cerr << som[a][b] << " ";
                    }
                    cerr << endl;
                }

                pair<int, int> best=make_pair(i, j);
                for(int a=0; a<=i; a++)
                {
                    for(int b=0; b<=j; b++)
                    {
                        int tot = som[i][j];
                        if(a-1 >= 0)
                        {
                            tot -= som[a-1][j];
                        }
                        if(b-1 >= 0)
                        {
                            tot -= som[i][b-1];
                        }
                        if(a-1 >= 0 && b-1 >= 0)
                        {
                            tot += som[a-1][b-1];
                        }
                        if(tot==0)
                        {
                            best=min(best, make_pair(a, b));
                        }
                    }
                }
                //cerr << som[1][1] << endl;
                //cerr << i << " " << j << " " << best.first << " " << best.second << endl;
                for(int a=best.first; a<=i; a++)
                {
                    for(int b=best.second; b<=j; b++)
                    {
                        field[a][b]=field[i][j];
                    }
                }
            }
        }

        //if(case_no==8) cerr << "REACHED111" << endl;

        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                //if(case_no==8) cerr << i << " " << j  << " " << nb_rows << " " << nb_cols << " " << field.size() << " " << field[i].size() << endl;
                if(field[i][j]!='?') continue;
                if(j > 0) field[i][j]=field[i][j-1];
                if(field[i][j]=='?' && i > 0) field[i][j]=field[i-1][j];
            }
        }

        //if(case_no==8) cerr << "REACHED" << endl;

        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                printf("%c", field[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}*/

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);

    //ios::sync_with_stdio(false);
    int tc;
    scanf("%d", &tc);
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:\n", case_no);
        //cerr << "Geval " << case_no << " gestart" << endl;
        int nb_rows, nb_cols;
        scanf("%d %d", &nb_rows, &nb_cols);
        vector< vector<char> > field(nb_rows, vector<char>(nb_cols));
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                scanf(" %c", &field[i][j]);
            }
        }

        /*if(case_no <= 10)
        {
            for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                printf("%c", field[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        }
        else break;*/

        vector< pair<int, int> > col_row_pairs;
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                if(field[i][j] != '?') col_row_pairs.push_back(make_pair(j, i));
            }
        }
        sort(col_row_pairs.begin(), col_row_pairs.end());
        for(int idx=0; idx<col_row_pairs.size(); idx++)
        {
            int i = col_row_pairs[idx].second;
            int j = col_row_pairs[idx].first;
            vector< vector<int> > som(nb_rows, vector<int>(nb_cols, 0));
                for(int a=0; a<nb_rows; a++)
                {
                    for(int b=0; b<nb_cols; b++)
                    {
                        if(field[i][j] != field[a][b] && field[a][b] != '?') som[a][b]++;
                        if(a-1 >= 0)
                        {
                            som[a][b] += som[a-1][b];
                        }
                        if(b-1 >= 0)
                        {
                            som[a][b] += som[a][b-1];
                        }
                        if(a-1 >= 0 && b-1 >= 0)
                        {
                            som[a][b] -= som[a-1][b-1];
                        }
                    }
                }

                /*cerr << i << " " << j << endl;
                for(int a=0; a<nb_rows; a++)
                {
                    for(int b=0; b<nb_cols; b++)
                    {
                        cerr << som[a][b] << " ";
                    }
                    cerr << endl;
                }*/

                pair<int, int> best=make_pair(i, j);
                for(int a=0; a<=i; a++)
                {
                    for(int b=0; b<=j; b++)
                    {
                        int tot = som[i][j];
                        if(a-1 >= 0)
                        {
                            tot -= som[a-1][j];
                        }
                        if(b-1 >= 0)
                        {
                            tot -= som[i][b-1];
                        }
                        if(a-1 >= 0 && b-1 >= 0)
                        {
                            tot += som[a-1][b-1];
                        }
                        if(tot==0)
                        {
                            best=min(best, make_pair(a, b));
                        }
                    }
                }
                //cerr << som[1][1] << endl;
                //cerr << i << " " << j << " " << best.first << " " << best.second << endl;
                for(int a=best.first; a<=i; a++)
                {
                    for(int b=best.second; b<=j; b++)
                    {
                        field[a][b]=field[i][j];
                    }
                }
        }

        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                if(field[i][j]=='?' && i-1 >= 0) field[i][j]=field[i-1][j];
            }
        }
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                if(field[i][j]=='?' && j-1 >= 0) field[i][j]=field[i][j-1];
            }
        }
        for(int i=0; i<nb_rows; i++)
        {
            for(int j=0; j<nb_cols; j++)
            {
                printf("%c", field[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
