#include<bits/stdc++.h>
using namespace std;

char cake[30][30];
bool v[30];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        memset(v,0,sizeof(v));
        printf("Case #%d:\n",t);
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%s",cake[i]);
            int lst = -1;
            for(int j=0;j<m;j++)
            {
                if(cake[i][j] == '?') continue;
                v[i] = true;
                for(int k=lst+1;k<j;k++) cake[i][k] = cake[i][j];
                lst = j;
            }
            if(v[i])
            {
                for(int j=lst+1;j<m;j++)
                    cake[i][j] = cake[i][lst];
            }
        }
        int lst = -1;
        for(int i=0;i<n;i++)
        {
            if(v[i])
            {
                if(i && lst < 0)
                {
                    for(int j=0;j<i;j++)
                        for(int k=0;k<m;k++)
                            cake[j][k] = cake[i][k];
                }
                lst = i;
                continue;
            }
            if(lst>=0)
            {
                for(int j=0;j<m;j++)
                    cake[i][j] = cake[lst][j];
            }
        }
        for(int i=0;i<n;i++)
            puts(cake[i]);
    }
}
