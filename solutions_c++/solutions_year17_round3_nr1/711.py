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
#define ppl pair<pl,ll>
#define id(i,j,n) (n*(i-1)+j)
#define IN(n) (2*(n)-1)
#define OUT(n) (2*(n))
#define double long double
#define mp make_pair
using namespace std;

pl pan[MAX];
vl srt;
const double PI=acos(-1.0);

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll T;
    sl(T);
    f(t,1,T+1){
        srt.clear();
        ll N, K;
        sll(N,K);
        f(i,0,N){
            sll(pan[i].x,pan[i].y);
        }
        sort(pan,pan+N);
        ll Ans=0;
        f(i,0,N){
            if(srt.size()>=(K-1)){
                sort(all(srt));
                ll ans=0;
                f(j,0,K-1){
                    ans+=srt[srt.size()-1-j]*2;
                }
                ans+=pan[i].x*pan[i].y*2;
                ans+=pan[i].x*pan[i].x;
                Ans=max(ans,Ans);
            }
            srt.pb(pan[i].x*pan[i].y);
        }
        //cout<<Ans<<endl;
        cout<<"Case #"<<t<<": "<<fixed<<setprecision(10)<<Ans*PI<<endl;
    }
}

/*
1
2 1
100 20
200 10
*/
