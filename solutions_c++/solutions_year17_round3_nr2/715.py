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

struct data{
    pl t;
    bool type;
    data(ll a,ll b,bool ty){
        t=pl(a,b);
        type=ty;
    }
};

bool cmp(const data &l,const data &r){
    return l.t<r.t;
}

vector <data> v, tmp;
vl sA, sB;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll T;
    sl(T);
    f(t,1,T+1){
        v.clear();
        ll N,M;
        sll(N,M);
        ll A,B;
        A=B=720;
        f(i,0,N){
            ll a,b;
            sll(a,b);
            A-=(b-a);
            v.pb(data(a,b,true));
        }
        f(i,0,M){
            ll a,b;
            sll(a,b);
            B-=(b-a);
            v.pb(data(a,b,false));
        }
        sort(all(v),cmp);
        ll Ans=1000000000000000;
        f(i,0,2){
            f(j,0,2){
                tmp.clear();
                sA.clear();
                sB.clear();
                tmp.pb(data(0,0,i));
                f(k,0,v.size()){
                    tmp.pb(v[k]);
                }
                tmp.pb(data(1440,1440,j));
                ll ans=(i!=j);
                f(k,1,tmp.size()){
                    if(tmp[k].type==tmp[k-1].type){
                        if(!tmp[k].type){
                            sB.pb(tmp[k].t.x-tmp[k-1].t.y);
                            ans+=2;
                        }
                        else{
                            sA.pb(tmp[k].t.x-tmp[k-1].t.y);
                            ans+=2;
                        }
                    }
                    else ans++;
                }
                //cout<<A<<' '<<B<<' '<<ans<<endl;
                ll A_=A,B_=B;
                sort(all(sA));
                sort(all(sB));
                /*cout<<"Printing"<<endl;
                f(k,0,sA.size()){
                    pfls(sA[k]);
                }
                cout<<endl;
                f(k,0,sB.size()){
                    pfls(sB[k]);
                }
                cout<<endl;*/
                f(k,0,sA.size()){
                    if((A-sA[k])>=0){
                        A-=sA[k];
                        ans-=2;
                    }
                    else break;
                }
                f(k,0,sB.size()){
                    if((B-sB[k])>=0){
                        B-=sB[k];
                        ans-=2;
                    }
                    else break;
                }
                //pfl(ans);
                //cout<<"-------------"<<endl;
                Ans=min(ans,Ans);
                A=A_, B=B_;
            }
        }
        pf("Case #%lld: %lld\n",t,Ans);
    }
}

/*
1
2 1
100 20
200 10
*/
