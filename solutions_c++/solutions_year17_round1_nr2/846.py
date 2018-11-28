#include <bits/stdc++.h>
 
#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)
 
#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=(int)(a)-1;i>=(int)(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)
 
#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
 
// #define DEBUG
 
#ifdef DEBUG
    #define dump(...) fprintf(stderr, __VA_ARGS__)
#else
    #define dump(...)
#endif
 
template<class T>bool chmax(T &a, const T &b) { return (a<b)?(a=b,1):0;}
template<class T>bool chmin(T &a, const T &b) { return (b<a)?(a=b,1):0;}
 
using namespace std;
using ll=long long;
using vi=vector<int>;
using vll=vector<ll>;
 
const double EPS = 1e-10;
const double PI = acos(-1.0);
const int inf =1 << 30;
const ll mod=1000000007LL;
const int dx[4]={1,0,-1,0};
const int dy[4]={0,1,0,-1};
 
 
ll extgcd(ll a,ll b,ll& x,ll& y){x=1,y=0;ll g=a;if(b!=0) g=extgcd(b,a%b,y,x),y-=a/b*x;return g;}
ll ADD(const ll &a, const ll &b,const ll &mod) { return (a+b)%mod;}
ll SUB(const ll &a, const ll &b,const ll &mod) { return (a-b+mod)%mod;}
ll MUL(const ll &a, const ll &b,const ll &mod) { return (1LL*a*b)%mod;}
ll DIV(const ll &a, const ll &b,const ll &mod) {ll x,y; extgcd(b,mod,x,y);return MUL(a,(x+mod)%mod,mod);}
 
random_device rd;
mt19937 mt(rd());
uniform_int_distribution<int> dice(1,6);
uniform_real_distribution<double> score(0.0,10.0);

////
class dinic{
	public :
		void init(int _n){
			n=_n;
			G.resize(n);
			iter.resize(n);
			level.resize(n);
		}

		void add_edge(int from,int to ,int cap){
			G[from].push_back((edge){to,cap,(int)G[to].size()});
			G[to].push_back((edge){from,0,(int)G[from].size()-1});
		}
	
		void add_edge_both(int from,int to ,int cap){
			add_edge(from,to,cap);
			add_edge(to,from,cap);
		}
	
		int max_flow(int s,int t){
			int flow=0;
			for(;;){
				bfs(s);
				if(level[t]<0) return flow;
				iter.assign(n,0);
				int f;
				while((f=dfs(s,t,DINIC_INF))>0){
					flow+=f;
				}
			}
		}
	private:
	
		int n;
		struct edge{int to,cap,rev;};
		static const int DINIC_INF = inf;
		vector< vector<edge> > G;
		vi level;
		vi iter;
	
		void bfs(int s){
			level.assign(n,-1);
			queue<int> que;
			level[s]=0;
			que.push(s);
			while(!que.empty()){
				int v=que.front();que.pop();
				for(int i=0;i< (int)G[v].size(); i++){
					edge &e=G[v][i];
					if(e.cap>0 && level[e.to] <0){
						level[e.to]=level[v]+1;
						que.push(e.to);
					}
				}
			}
		}

		int dfs(int v,int t,int f){
			if(v==t) return f;
			for(int &i=iter[v];i<(int)G[v].size();i++){
				edge &e= G[v][i];
				if(e.cap>0 && level[v]<level[e.to]){
					int d=dfs(e.to,t,min(f,e.cap));
					if(d>0){
						e.cap -=d;
						G[e.to][e.rev].cap+=d;
						return d;
					}
				}
			}
			return 0;
		}	
};
//

int P;
inline int ij2i(int i, int j, bool bk){
    return 2 * P * i + (bk ? P:0) + j;
}

int main(void){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T; cin >> T;
    rep(_, T){
        int n; cin >> n >> P;
        vi R(n); for(auto& e : R) cin >> e;

        vector<vi> Q(n, vi(P));
        rep(i, n){
            rep(j, P){
                cin >> Q[i][j];
            }
            sort(_all(Q[i]));
        }
        
        dinic d;
        int V = n * P * 2 + 2;
        int s = n * P * 2;
        int t = s + 1;

        d.init(V);
        rep(j, P){
            d.add_edge(s, j, 1);
        }
        rep(j, P){
            d.add_edge(2 * P * (n - 1) + P + j, t, 1);
        }
        rep(i, n){
            rep(j, P){
                int a = Q[i][j];
                int nl = ceil (a / 1.1 / R[i]);
                int nu = (int)(a / 0.9 / R[i]);
                if(nl != 0 and nl <= nu){
                    d.add_edge(ij2i(i, j, false), ij2i(i, j, true), 1);
                }
            }
        }

        rep(i, n - 1){
            rep(j1, P){
                rep(j2, P){
                    int a = Q[i][j1], b = Q[i + 1][j2];
                    int nal = ceil (a / 1.1 / R[i]);
                    int nau = (int)(a / 0.9 / R[i]);
                    int nbl = ceil (b / 1.1 / R[i + 1]);
                    int nbu = (int)(b / 0.9 / R[i + 1]);

                    if(nbl <= nau and nal <= nbu){
                        d.add_edge(ij2i(i, j1, true), ij2i(i + 1, j2, false), 1);
                    }
                }
            }
        }

        cout << "Case #" << _ + 1 << ": ";
        cout << d.max_flow(s, t) << endl;
    }

    return 0;
}
