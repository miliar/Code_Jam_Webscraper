#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<deque>
#include<set>

using namespace std;

#define sz(x) (int)(x.size())
#define fi(a, b) for(int i=a;i<b;++i)
#define fj(a, b) for(int j=a;j<b;++j)
#define fk(a, b) for(int k=a;k<b;++k)
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

///////////////

int const N = 1e2 + 41;
ll const INF = (1e9 * 1LL * 1e9);

int n, q;
ll e[N], s[N], d[N][N];
double d0[N];
vector<double> answ;
int fi, se;

int was[N];

void print(int t, double ans){
	printf("Case #%d: %.6lf\n",t+1,ans);
}

void clear(){
	fi(0, n) d0[i] = INF, was[i] = 0;
}

ll dist[N][N];

void floyd(){
	fi(0, n) fj(0, n){
		if(d[i][j] == -1) dist[i][j] = INF;
		else dist[i][j] = d[i][j];
	}
	fi(0, n){
		fj(0, n){
			fk(0, n){
				dist[j][k] = min(dist[j][i] + dist[i][k], dist[j][k]);
			}
		}
	}
}

void solve(int test){
	cin >> n >> q;
	fi(0, n) cin >> e[i] >> s[i];
	fi(0, n) fj(0, n) cin >> d[i][j];
	
	floyd();

	for(int t=0;t<q;++t){
		clear();
		cin >> fi >> se;
		--fi;--se;
		d0[fi] = 0;
		while(true){
			bool f = false;
			pair<double, int> mini = mp(INF * 2.0, -1);
			fi(0, n){	
				if(!was[i]){
					mini = min(mini, mp(d0[i], i));
					f = true;
				}
			}
			if(!f) break;
			int id = mini.second;
			double cur = mini.first;
			was[id] = 1;
			fi(0, n){
				if(dist[id][i] != INF && dist[id][i] <= e[id]){
					d0[i] = min(d0[i], cur + dist[id][i] * 1.0 / s[id]);
				}
			}
		}
		answ.pb(d0[se]);
	}
	printf("Case #%d:",test+1);
	fi(0, sz(answ)) printf(" %.6lf",answ[i]);
	printf("\n");
	answ.clear();
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;
	for(int t=0;t<test;++t){
		solve(t);
	}

	return 0;
}