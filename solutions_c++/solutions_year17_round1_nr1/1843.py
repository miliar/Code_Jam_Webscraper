#include<bits/stdc++.h>
using namespace std;
const int maxn=100;
char s[maxn][maxn];
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("test.txt","w",stdout);
    int T,ca=1;scanf("%d",&T);
    while(T--)
    {
        int n,m;
        stack<int>un;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            scanf("%s",s[i]+1);
        int root;
        for(int i=1;i<=n;i++)
           {
                int cnt=0;
                for(int j=1;j<=m;j++)
                    if(s[i][j]!='?')
                {
                    int pos=1;
                    while(j-pos>=1&&s[i][j-pos]=='?')
                    {
                        s[i][j-pos]=s[i][j];pos++;
                    }
                    pos=1;
                    while(j+pos<=m&&s[i][j+pos]=='?')
                    {
                        s[i][j+pos]=s[i][j];pos++;
                    }
                }
                else cnt++;
                if(cnt==m)un.push(i);
                else
                {
                    root=i;
                    while(!un.empty())
                    {
                        int u=un.top();un.pop();
                        for(int j=1;j<=m;j++)
                            s[u][j]=s[root][j];
                    }
                }
           }
           while(!un.empty())
           {
               int u=un.top();un.pop();
               for(int j=1;j<=m;j++)
                    s[u][j]=s[root][j];
           }
           printf("Case #%d:\n",ca++);
           for(int i=1;i<=n;i++)
                printf("%s\n",s[i]+1);
    }

    return 0;
}
