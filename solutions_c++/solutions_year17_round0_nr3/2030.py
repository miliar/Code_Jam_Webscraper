//Tanuj Khattar
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
map<LL,LL> sz[2];
int main()
{
  int T;si(T);
  for(int t=1;t<=T;t++){
    printf("Case #%d: ",t);
    LL n,k;
    sll(n);sll(k);
    int x = 0, y = 1;
    sz[x].clear(),sz[y].clear();
    sz[x][-n] = 1;LL ans = -1;
    for(int i=0;i<64 && ans == -1;i++){
      for(auto it : sz[x]){
        LL s = -it.F, c = it.S;
        if(c >= k){
          ans = s;
          break;
        }
        k -= c;
        LL lc = (s - 1) / 2, rc = s - 1 - lc;
        sz[y][-lc] += c;
        sz[y][-rc] += c;
      }
      swap(x,y);
      sz[y].clear();
    }
    assert(ans  !=  -1);
    LL la = (ans - 1) / 2, ra = ans - 1 - la;
    printf("%lld %lld\n",max(la,ra),min(la,ra));
  }
	return 0;
}
