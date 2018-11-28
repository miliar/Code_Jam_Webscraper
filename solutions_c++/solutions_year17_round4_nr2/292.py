/*\
 * ...
 * ......
 * In the name of ALLAH
 * ......
 * ...
\*/

#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
#define LD_OUT setprecision(12) << fixed
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 1e3 + 10;

int n,m,p;
bool adj[MN][MN];
int deg[MN] , deg2[MN] , cnt[MN];
int Ans;

bool check(int delta)
{
	if(*max_element(deg2 , deg2 + m) > delta) return false;
	Ans = 0;
	memset(cnt , 0 , sizeof cnt);
	int mex = 0;
	for(int i=0;i<n;++i){
		cnt[i] = min(deg[i] , delta);
		if(deg[i] <= delta) continue;
		int D = deg[i] - delta;
		Ans += D;
		while(D){
			while(mex < i && cnt[mex] == delta) ++mex;
			if(mex == i) return false;
			if(D > delta - cnt[mex]) D -= delta - cnt[mex], cnt[mex] = delta;
			else cnt[mex] += D , D = 0;
		}
	}
	return true;	
}

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;cin>>T;
	int cnt = 0;
	while(T--){
		++cnt;
		memset(adj , 0 , sizeof adj);
		memset(deg , 0 , sizeof deg);
		memset(deg2 , 0 , sizeof deg2);
		cout << "Case #" << cnt << ": ";
		cin >> n >> m >> p;
		for(int i=0;i<p;++i){
			int a,b;cin>>a>>b;--a,--b;
			adj[a][b] = true;
			++deg2[b];
			++deg[a];
		}
		int L = 0 , R = p;
		while(L != R){
			int mid = L+R>>1;
			if(check(mid)) R = mid;
			else L = mid+1;
		}
		check(L);
		cout << L << ' ' << Ans << '\n';
	}
	return 0;
}

