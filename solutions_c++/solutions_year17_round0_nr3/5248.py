//Amit Gupta              
//
#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define TR(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define TR(...)
#endif

typedef long long               LL;
typedef pair<int,int>           II;
typedef vector<int>             VI;
typedef vector<II>              VII;


#define REP(i,i1,n)             for(int i=i1;i<n;i++)
#define REPB(i,i1,n)            for(int i=i1;i>=n;i--)
#define PB                      push_back
#define MP                      make_pair
#define ALL(c)                  (c).begin(),(c).end()
#define F                       first
#define S                       second
#define log2                    0.30102999566398119521373889472449L
#define SZ(a)                   (int)a.size()
#define EPS                     1e-12
#define MOD                     1000000007
#define FAST_IO                 ios_base::sync_with_stdio(false);cin.tie(NULL)
#define SI(c)                   scanf("%d",&c)
#define SLL(c)                  scanf("%lld",&c)
#define PIN(c)                  printf("%d\n",c)
#define PLLN(c)                 printf("%lld\n",c)
#define N                       200010
#define endl                    '\n'
#define FILL(ar,vl)             for(int i=0;i<N;i++)ar[i]=vl
#define FILL2(ar,vl)            for(int i=0;i<N;i++)for(int j=0;j<N;j++)ar[i][j]=vl

inline int mult(int a , int b) { LL x = a; x *= LL(b); if(x >= MOD) x %= MOD; return x; }
inline int add(int a , int b) { return a + b >= MOD ? a + b - MOD : a + b; }
LL powmod(LL a,LL b) { if(b==0)return 1; LL x=powmod(a,b/2); LL y=(x*x)%MOD; if(b%2) return (a*y)%MOD; return y%MOD; }

//--------------------------MAIN CODE STARTS HERE----------------

int main() {	
    int t;
    cin>>t;
    for(int ti = 1; ti <= t; ti++) {
        LL n,k;
        cin>>n>>k;
        map<LL,LL> mp, mp1;
        LL st = 1, nm = 2;
        mp.insert({n,1});
        while(st < k) {
            map<LL,LL>::iterator i = mp.begin();
            while(i != mp.end()) {
                LL n1 = i->F, n2 = i->S;
                LL vl1 = (n1)/2;
                LL vl2 = (n1-1)/2;
                if(mp1.find(vl1) == mp1.end()) {
                    mp1.insert({vl1,n2});
                }
                else mp1[vl1] += n2;
                if(mp1.find(vl2) == mp1.end()) {
                    mp1.insert({vl2,n2});
                }
                else mp1[vl2] += n2;
                i++;
            }
            mp.clear();
            mp = mp1;
            mp1.clear();
            st = st + nm;
            nm*=2;
        }
        st -= nm/2;
        auto z = mp.end();
        z--;
        LL ans1,ans2;
        LL left = k - st;
        if(z->S >= left) {
            ans1 = z->F/2;
            ans2 = (z->F-1)/2;
        }
        else {
            z--;
            ans1 = z->F/2;
            ans2 = (z->F-1)/2;
        }
        cout<<"Case #"<<ti<<": "<<ans1<<" "<< ans2<<"\n";
    }
}
