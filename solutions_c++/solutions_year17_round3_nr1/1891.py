    #include <bits/stdc++.h>
    #include <tr1/unordered_map>
    typedef long long ll;
    typedef unsigned long long ull;
    #define clr(ma) memset(ma,-1,sizeof ma)
    #define INF 1000000000
    #define vi vector<int>
    #define pi pair<int ,int >
    #define T pair<pi ,int>
    #define T2 pair<pi ,pi >
    #define mk make_pair
    #define getBit(m,i) ((m&(1ll<<i))==(1ll<<i))
    #define setBit(m,i) (m|(1<<i))
    #define setBit2(m,i) (m|(1ull<<i))
    #define cont(i,ma) ((ma.find(i))!=(ma.end()))
    #define in(i) scanf("%d",&i)
    #define in2(i,j) scanf("%d%d",&i,&j)
    #define in3(i,j,k) scanf("%d%d%d",&i,&j,&k)
    #define in4(i,j,k,l) scanf("%d%d%d%d",&i,&j,&k,&l)
    #define il(i) scanf("%lld",&i)
    #define itr map<ll,ll>::iterator
    #define itr2 map<ll,map<ll,ll> >::iterator
    #define id(k) scanf("%9lf",&k)
    #define fi(ss) freopen (ss,"r",stdin)
    #define fo(ss) freopen (ss,"w",stdout)
    #define sc(s) scanf("%s",s)
    #define clean(vis)  memset(vis,0,sizeof vis)
    #define  bitcount(x)  __builtin_popcount(x)
    using namespace std;
    vector<pi> v;
    const double PI =acos(-1);
    ll dp [1001][1001];
    bool com (pi a ,pi b){
        if (a.first!=b.first)return a.first>b.first;
         return a.second>b.second;
    }
    int main(){
        fi("/home/mohamedatef/ClionProjects/untitled1/input.txt");
        fo("/home/mohamedatef/ClionProjects/untitled1/out.txt");
        int t;
        in(t);
        int c=1;
        while (t--){
            int n,k;
            in2(n,k);
            v.clear();
            int x,y;
            for (int i=0;i<n;i++){
                in2(x,y);
                v.push_back(mk(x,y));
            }
            sort(v.begin(),v.end(),com);
            clean(dp);
            ll ans=0;
           if (k==1)ans=max(ans,2ll*(ll)v[n-1].first*(ll)v[n-1].second+(ll)v[n-1].first*(ll)v[n-1].first);
            dp[n-1][1]=2ll*(ll)v[n-1].first*(ll)v[n-1].second;
            for (int i=n-2;i>=0;i--){
                for (int j=1;j<=k;j++){
                    ll tmp=2ll*(ll)v[i].first*(ll)v[i].second+(ll)v[i].first*(ll)v[i].first+ dp[i+1][j-1];
                    if (k==j)ans=max(ans,tmp);
                    dp[i][j]=max(dp[i+1][j],tmp-(ll)v[i].first*(ll)v[i].first);
                }
            }
            printf("Case #%d: %.9f\n",c++,PI*ans);
        }
    }