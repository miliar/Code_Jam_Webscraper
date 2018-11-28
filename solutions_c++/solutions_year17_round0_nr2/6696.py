#include <bits/stdc++.h>
#define ll             long long
#define pl             pair <ll,ll>
#define ps             pair <string,string>
#define vi             vector <int>
#define vl             vector <ll>
#define vpi            vector <pi>
#define vpl            vector <pl>
#define f(i,a,b)       for(ll i=(a);i<(b);i++)
#define fd(i,a,b)      for(ll i=(a);i>(b);i--)
#define Max(a,b)       ((a)>(b)?(a):(b))
#define Min(a,b)       ((a)<(b)?(a):(b))
#define x              first
#define y              second
#define si(a)          scanf("%d",&a)
#define sii(a,b)       scanf("%d %d",&a,&b)
#define siii(a,b,c)    scanf("%d %d %d",&a,&b,&c)
#define sl(a)          scanf("%lld",&a)
#define sll(a,b)       scanf("%lld %lld",&a,&b)
#define slll(a,b,c)    scanf("%lld %lld %lld",&a,&b,&c)
#define sd(a)          scanf("%lf",&a)
#define sdd(a,b)       scanf("%lf %lf",&a,&b)
#define sddd(a,b,c)    scanf("%lf %lf %lf",&a,&b,&c)
#define ss(s)          scanf("%s",s)
#define pf             printf
#define pfi(n)         printf("%d\n",n)
#define pfl(n)         printf("%lld\n",n)
#define pfls(n)        printf("%lld ",n)
#define pfci(n,ans)    printf("Case %lld: %d\n",n,ans)
#define pfcl(n,ans)    printf("Case %lld: %lld\n",n,ans)
#define pfcd(n,ans)    printf("Case %lld: %lf\n",n,ans)
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define mem(a,v)       memset(a,v,sizeof(a))
#define MAX 1000007
#define MOD 10007
#define LG  16
#define PI (acos(-1.0))
#define ppl pair<pl,ll>
#define id(i,j,n) (n*(i-1)+j)
#define PT pair<double,double>
#define IN(n) (2*(n)-1)
#define OUT(n) (2*(n))

using namespace std;

string n;

ll dp[2][19][10];
bool vis[2][19][10];
ll pwr[19];

ll go(bool t, ll idx, ll lst){
    if(idx==-1) return 0;
    ll &ret=dp[t][idx][lst];
    bool &vst=vis[t][idx][lst];
    if(vst) return ret;
    else vst=true;
    ret=-9223372036854775808;
    if(t){
        f(i,lst,n[idx]-'0'+1){
            bool qt=(i==(n[idx]-'0'));
            ret=max(ret,i*pwr[idx]+go(qt,idx-1,i));
        }
    }
    else{
        f(i,lst,10){
            ret=max(ret,i*pwr[idx]+go(false,idx-1,i));
        }
    }
    return ret;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    pwr[0]=1;
    f(i,1,19) pwr[i]=pwr[i-1]*10;
    ll T;
    sl(T);
    f(t,1,T+1){
        mem(vis,false);
        cin>>n;
        reverse(all(n));
        pf("Case #%lld: ",t);
        pfl(go(true,n.size()-1,0));
    }
}
