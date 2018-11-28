#include<bits/stdc++.h>
using namespace std;
const int M = 1002;
string s;
bool m[M];
int f[M];
int k;
int solve()
{
    int res,sum;
    res=sum=0;
    memset(f,0,sizeof(f));
    for(int i=0;i<=s.length()-k;++i){
        if((sum+m[i])%2){
            f[i]=1;
            ++res;
        }
        sum+=f[i];
        if(i-k+1>=0) sum-=f[i-k+1];
    }
    for(int i=s.length()-k+1;s[i];++i){
        if((sum+m[i])%2)
            return -1;
        if(i-k+1>=0) sum-=f[i-k+1];
    }
    return res;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.ou","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tt=0;tt<t;++tt){
        getchar();
        cin>>s>>k;
        for(int i=0;i<s.length();++i)
            m[i]=(s[i]!='+');
        int ans=solve();
        printf("Case #%d: ",tt+1);
        if(ans==-1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",ans);
    }
    return 0;
}
