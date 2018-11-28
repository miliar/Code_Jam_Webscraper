#include<bits/stdc++.h>
using namespace std;
int n,m;
char s[30][30];
vector<int> p;
void f(int r1,int c1,int r2,int c2,char val)
{
    int i,j;
    for(i=r1;i<=r2;i++) for(j=c1;j<=c2;j++) s[i][j] = val;
}
main()
{
    int T,cnum=1;
    int low,i,j,x,last;
    freopen("A-large.in","r",stdin);
    freopen("A_out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++) scanf(" %s",s[i]);
        last = -1;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++) if(s[i][j]!='?') low = i;
        }
        for(i=0;i<n;i++)
        {
            p.clear();
            for(j=0;j<m;j++) if(s[i][j]!='?') p.push_back(j);
            for(x=0;x<p.size();x++)
            {
                if(x) f(last+1,p[x-1]+1,i,p[x],s[i][p[x]]);
                else f(last+1,0,i,p[x],s[i][p[x]]);
                if(i==low)
                {
                    if(x) f(i,p[x-1]+1,n-1,p[x],s[i][p[x]]);
                    else f(i,0,n-1,p[x],s[i][p[x]]);
                }
            }
            if(p.size())
            {
                f(last+1,p[p.size()-1],i,m-1,s[i][p[p.size()-1]]);
                if(i==low)
                {
                    f(i,p[p.size()-1],n-1,m-1,s[i][p[p.size()-1]]);
                }
                last = i;
            }
        }
        for(x=0;x<p.size();x++)
        {
            if(x) f(last+1,p[x-1]+1,i,p[x],s[i][p[x]]);
            else f(last+1,0,i,p[x],s[i][p[x]]);
        }
        printf("Case #%d:\n",cnum++);
        for(i=0;i<n;i++) printf("%s\n",s[i]);
    }
}
