#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair < int , int > pii ;


char str[111] , len;
bool vis[22][11][2];
LL dp[22][11][2] , pw[22];

string S;

LL f(int x , int prev , int st)
{
    if(x==len)return 0;
    LL &ret = dp[x][prev][st];
    if(vis[x][prev][st])return ret;
    ret = -1e18;
    for(int i = prev;i<=(st?9:S[x]-'0');++i)
    {
        LL sa = f(x+1,i,st||(i<S[x]-'0'));
        if(sa>=0)
            ret = max(ret , i * pw[len-x-1] + sa);
    }
    return ret;
}


void solve()
{
    LL N , i ;
    cin>>N;
    sprintf(str,"%lld",N);
    string T(str);
    S = T;
    if(S.length()==1){cout<<S;return;}
    len  = S.length();
    LL l = 0 , g = 0 ;
    pw[0]=1;
    memset(vis,0,sizeof(vis));
    for(i=1;i<=S.length();++i)
        pw[i] = pw[i-1]*10LL;
    for(i=0;i+1<S.length();++i)
        l = l * 10 + 9;
    for(i=0;i<=S[0]-'0';++i)
        l = max(l , f(0,i,0));
    cout<<max(l,g);
}
int main()
{
//////    ini();
    freopen("in.in","r+",stdin);
    freopen("1.txt","w+",stdout);
    int T , i ;
    cin>>T;
    cin.ignore();
    for(i=1;i<=T;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
    return 0;
}
