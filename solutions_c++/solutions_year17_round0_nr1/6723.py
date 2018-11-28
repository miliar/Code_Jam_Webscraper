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

ll get(string s,ll k){
    ll cnt=0;
    f(i,0,s.size()-k+1){
        if(s[i]=='-'){
            cnt++;
            f(j,i,i+k){
                if(s[j]=='-') s[j]='+';
                else s[j]='-';
            }
        }
    }
    f(i,0,s.size()){
        if(s[i]=='-'){
            return -1;
        }
    }
    return cnt;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll T;
    sl(T);
    f(t,1,T+1){
        string s;
        cin>>s;
        ll k;
        sl(k);
        ll v1=get(s,k);
        reverse(all(s));
        ll v2=get(s,k);
        pf("Case #%lld: ",t);
        if(v1==-1 && v2==-1){
            pf("IMPOSSIBLE\n");
        }
        else if(v1==-1){
            pfl(v2);
        }
        else if(v2==-1){
            pfl(v1);
        }
        else{
            pfl(min(v1,v2));
        }
    }
}
