//Amit Gupta              
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
    for(int ti = 1; ti <= t; ti++){
        string s;
        int k;
        cin>>s;
        cin>>k;
        int cnt = 0;
        for(int i = 0; i < s.size() ; i++) {
            if((s[i] == '-')&& (i + k  <= s.size() )) {
                for(int j = i; j < i + k ; j++) {
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                cnt ++;
            }
        }
        int f = 0;
        for(int i = 0; i < s.size() ; i++) {
            if(s[i] == '-') f = 1;
        }
        cout<<"Case #"<<ti<<": ";
        if(f) cout<<"IMPOSSIBLE\n";
        else cout<<cnt<<"\n";
    }
}
