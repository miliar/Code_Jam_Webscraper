#include <cstdio>
#include <cstring>

using namespace std;

char sir[1010];

int solve(int n,int k)
{
    int lim=n-k+1,sol=0;
    for(int i=1;i<=lim;i++)
        if(sir[i]=='-')
        {
            sol++;
            for(int j=i;j<i+k;j++)
                if(sir[j]=='+') sir[j]='-';
                else sir[j]='+';
        }
    for(int i=1;i<=n;i++)
        if(sir[i]=='-') return -1;
    return sol;
}

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int k;
        scanf("\n%s%d",sir+1,&k);
        int n=strlen(sir+1);
        int sol=solve(n,k);
        if(sol==-1) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,sol);
    }
    return 0;
}
