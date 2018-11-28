#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
#include <iostream>
using namespace std;

int main()
{

    int T, R, C;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        DI(t)
        printf("Case #%d:\n",t);

        cin >> R >> C;
        vector<string> cake(R);

        for(int i =0; i<R; ++i)
            cin >> cake[i];
        set<char> done;
        for(int i = 0; i < R; ++i)
            for(int j = 0 ; j < C ; ++j)
                if(cake[i][j] != '?' && done.find(cake[i][j]) == done.end())
                {//boki
                    done.insert(cake[i][j]);
                    int st = j, en = j;
                    for(int k = j-1; k>=0;--k)
                        if(cake[i][k] == '?')
                        {
                            cake[i][k] = cake[i][j];
                            st = k;
                        }
                        else
                            break;

                    for(int k = j+1; k<C;++k)
                        if(cake[i][k] == '?')
                        {
                            cake[i][k] = cake[i][j];
                            en = k;
                        }
                        else
                            break;
                    //gora dol
                    for(int k = i-1; k>=0;--k)
                    {
                        bool clear = true;
                        for(int m = st; m<=en;++m)
                            if(cake[k][m] != '?')
                            {
                                clear = false;
                                break;
                            }
                        if(clear)
                            for(int m = st; m<=en;++m)
                                cake[k][m] = cake[i][j];
                        else
                            break;
                    }

                    for(int k = i+1; k<R;++k)
                    {
                        bool clear = true;
                        for(int m = st; m<=en;++m)
                        {
                            if(cake[k][m] != '?')
                            {
                                clear = false;
                                break;
                            }}
                        if(clear)
                            for(int m = st; m<=en;++m)
                                cake[k][m] = cake[i][j];
                        else
                            break;
                    }

                }

        for(const auto& s : cake)
            cout << s << endl;
    }
    return 0;
}
