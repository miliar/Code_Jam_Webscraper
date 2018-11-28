#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;

int n,p;
int a[4];
int c[4];
int b[100000];
int dp[100][100][100][4];

int solve(int a1, int a2, int a3, int t)
{
    if(a1+a2+a3==0) return 0;
    if(dp[a1][a2][a3][t]!=-1) return dp[a1][a2][a3][t];
    int res=0;
    if(a1){
        int z=t;
        while(z<1)z+=4;
        res=max(res, solve(a1-1,a2,a3,z-1));
    }
    if(a2){
        int z=t;
        while(z<2)z+=4;
        res=max(res, solve(a1,a2-1,a3,z-2));
    }
    if(a3){
        int z=t;
        while(z<3)z+=4;
        res=max(res, solve(a1,a2,a3-1,z-3));
    }
    return dp[a1][a2][a3][t] = res + (t?0:1);
}

int f2(int x)
{
    int i=0;
    c[1]=a[1];
    c[2]=a[2];
    while(c[1] || c[2])
    {
        if(!c[x]) x=3-x;
        b[i++]=x;
        c[x]--;
        x=3-x;
    }
    int res=0;int t=0;
    for(int j=0;j<i;++j)
    {
        if(!t) res++;
        int z=t;
        while(z<b[j])z+=3;
        t=z-b[j];
    }
    return res;
}

int main()
{
    cin.tie();ios::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for(int test=1;test<=T;++test)
    {
        printf("Case #%d: ",test);
        a[0]=a[1]=a[2]=a[3]=0;
        cin >> n >> p;
        for(int i=0;i<n;++i)
        {
            int x;
            cin >> x;
            a[x%p]++;
        }
        if(p==2)
        {
            printf("%d\n",a[0]+(a[1]+1)/2);
        } else if(p==3)
        {
            int ans1=f2(2);
            int ans2=f2(1);
            printf("%d\n",a[0]+max(ans1,ans2));
        } else if(p==4)
        {
            /*int ans = min(a[1],a[3]);
            a[1] -= ans;
            a[3] -= ans;
            ans += a[2]/2;
            a[2]%=2;*/
            memset(dp,-1,sizeof(dp));
            printf("%d\n",a[0]+solve(a[1],a[2],a[3],0));
        }
    }

}
