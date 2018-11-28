#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pp;
typedef pair<ll,ll> pll;
void read(int& x){ scanf("%d",&x); }
void read(ll& x){ scanf("%lld",&x); }
template<typename T,typename... Args>
void read(T& a,Args&... b){ read(a); read(b...); }
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define x first
#define y second

int N, C, M;
vector<pp> tick;

void in(){
	read(N, C, M);
	tick.clear();
	for(int i=1; i<=M; ++i){
		int p, c; read(p, c);
		tick.emplace_back(p, c);
	}
}

bool taken[1010][1010];
bool cust[1010][1010];
int minnot[1010];
int pcnt[1010];

void work(){
	in();
	sort(all(tick));

	memset(taken, 0, sizeof(taken));
	memset(cust, 0, sizeof(cust));
	int car=0;
	
	for(auto tmp:tick){
		int p=tmp.first, c=tmp.second;
		bool as=0;
		for(int j=0; j<car; ++j){
			if(!cust[c][j] && !taken[j][p]){
				as=1;
				taken[j][p]=1; cust[c][j]=1;
				break;
			}
		}
		if(as) continue;
		for(int j=0; j<car; ++j){
			if(!cust[c][j] && minnot[j]<p){
				as=1;
				cust[c][j]=1; taken[j][minnot[j]]=1;
				while(taken[j][minnot[j]]) ++minnot[j];
				break;
			}
		}
		if(!as){
			cust[c][car]=1; taken[car][1]=1;
			minnot[car]=2;
			++car;
		}
	}
	
	int ans=0;
	memset(pcnt, 0, sizeof(pcnt));
	for(auto tmp:tick) ++pcnt[tmp.x];
	for(int i=1; i<=N; ++i) ans += max(0, pcnt[i]-car);
	printf("%d %d\n", car, ans);
}

#define CASE "small"

int main()
{
	freopen(CASE ".in", "r", stdin);
	freopen(CASE ".out", "w", stdout);
	int tc; read(tc);
	for(int i=1; i<=tc; ++i){
		printf("Case #%d: ", i);
		work();
		fprintf(stderr, "Case #%d done\n", i);
	}
    return 0;
}
