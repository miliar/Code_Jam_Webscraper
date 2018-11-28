#include <bits/stdc++.h>
using namespace std;
#define ll              long long
#define llu             unsigned long long
#define pb              push_back
#define MOD             1000000007
#define MAX             1000007
#define eps             1e-8
#define inf             0x3f3f3f3f
#define INF             2e18
#define clr(a)          memset(a,0,sizeof(a))
#define reset(a)        memset(a,-1,sizeof(a))
#define ff              first
#define ss              second
#define pLL             pair<ll,ll>
#define mp              make_pair
#define pi              pair<int,int>
#define READ(f)         freopen(f,"r",stdin)
#define WRITE(f)        freopen(f,"w",stdout)
#define pii             2.0*acos(0.0)
#define all(a)          a.begin(),a.end()
#define rall(a)         a.rbegin(),a.rend()
#define SQR(a)          ((a)*(a))
#define Unique(a)       sort(all(a)),a.erase(unique(all(a)),a.end())
#define int_map         map<int,int>
#define v_map           map<int,vector<int> >
#define long_map        map<ll,ll>
#define IO              ios::sync_with_stdio(false)
#define inputline(a)    getline(cin,a)
#define min3(a,b,c)     min(a,min(b,c))
#define max3(a,b,c)     max(a,max(b,c))
#define min4(a,b,c,d)   min(min(a,b),min(c,d))
#define max4(a,b,c,d)   max(max(a,b),max(c,d))
#define max5(a,b,c,d,e) max(max3(a,b,c),max(d,e))
#define min5(a,b,c,d,e) min(min3(a,b,c),min(d,e))
#define FOR(a,it)       for(Iterator(a) it = a.begin();it != a.end(); it++)
#define rFOR(a,it)      for(rIterator(a) it = a.rbegin();it != a.rend(); it++)
#define vi              vector <int>
#define vL              vector <ll>
#define dbg(a)          cout<<a<<endl
int d8x[]={-1,-1,0,1,1,1,0,-1};
int d8y[]={0,1,1,1,0,-1,-1,-1};

pLL call(ll temp,ll per){
    map<pLL,ll>visit;
    set<pLL>S;
    ll left=temp/2;
    ll right=(temp-1)/2;
    S.insert({left,right});
    visit[{left,right}]=1;
    ll counter=0;
    while(!S.empty() && counter < temp){
        pLL p=*(S.rbegin());
        S.erase(prev(S.end()));
        ll cc=visit[p];
        counter+=cc;
//        cout<<p.ff<<" "<<p.ss<<endl;
//        cout<<counter <<" "<<cc<<endl;
        if(counter>=per)return p;
        ll l=p.ff;
        ll r=p.ss;
        if(l){
            left=l/2;
            right=(l-1)/2;
            visit[{left,right}]+=cc;
            S.insert({left,right});
        }
        if(r){
            left=r/2;
            right=(r-1)/2;
            visit[{left,right}]+=cc;
            S.insert({left,right});
        }
    }
}

int main(void)
{
    READ("input.txt");
    WRITE(("output.txt"));
    int T,N=0;
    scanf("%d",&T);
    while(++N<=T){
        ll num,per;
        scanf("%lld%lld",&num,&per);
        pLL p=call(num,per);
        printf("Case #%d: %lld %lld\n",N,p.ff,p.ss);
    }
    return 0;
}
