//incompleted
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <functional>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 105;
const int P = 1e9+7;

int in[MAXN][MAXN];
int ans[MAXN][MAXN];

bool bySecond(pair<int, int> a, pair<int, int> b){
	return a.se < b.se;
};

struct Greedy{
	vector<pair<int, int> > qx, qy;
	vector<int> dx, dy;

	void clear(){
		qx.clear();
		qy.clear();
		dx.clear();
		dy.clear();
	}

	void available(vector<pair<int, int> > &q, vector<int> &d){
		int i, j, k;
		sort(q.begin(), q.end());
		sort(d.begin(), d.end());
//		for(i = 0; i < q.size(); i++)
//			printf("(%d %d)", q[i].fi, q[i].se);
//		printf("\n");
//		for(i = 0; i < d.size(); i++)
//			printf("%d ", d[i]);
//		printf("\n");
		i = j = k = 0;
		while(i < q.size()){
			if(j < d.size() && q[i].fi == d[j]){
				i++;
				j++;
			}
			else{
				q[k] = q[i];
				i++;
				k++;
			}
		}
		q.resize(k);
	}

	vector<pair<int, int> > solve(int r){
		available(qx, dx);
		available(qy, dy);

		sort(qx.begin(), qx.end(), bySecond);
		sort(qy.begin(), qy.end(), bySecond);
		vector<pair<int, int> > ret;
		int i, j;
		i = 0;
		j = qy.size()-1;
		while(i < qx.size() && j >= 0){
			if(qx[i].se + qy[j].se >= r){
				ret.pb(mp(qx[i].fi, qy[j].fi));
				i++;
				j--;
			}
			else{
				i++;
			}
		}
		return ret;
	}
};

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		int n, m;
		int i, j, k;
		scanf("%d%d", &n, &m);
		memset(in, 0, sizeof in);
		memset(ans, 0, sizeof ans);
		for(k = 0; k < m; k++){
			char s[2];
			scanf("%1s%d%d", s, &i, &j);
			i--;
			j--;
			if(s[0] == '+')
				in[i][j] = 2;
			else if(s[0] == 'x')
				in[i][j] = 1;
			else if(s[0] == 'o')
				in[i][j] = 3;
		}

		//workOrth
		Greedy g;
		for(i = 0; i < n; i++){
			g.qx.pb(mp(i, 1));
			g.qy.pb(mp(i, 1));
		}
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				if(in[i][j]&1){
					g.dx.pb(i);
					g.dy.pb(j);
				}
		vector<pair<int, int> > q = g.solve(2);
		for(const pair<int, int> &p : q){
			i = p.fi;
			j = p.se;
			ans[i][j] |= 1;
		}

		//workDiagEven
		g.clear();
		for(i = 0; i <= 2*n-2; i += 2){
			g.qx.pb(mp(i, 1 + min(i, 2*n-2-i)));
		}
		for(i = 0; i < n; i += 2){
			g.qy.pb(mp(i, n-i));
			if(i != 0)
				g.qy.pb(mp(-i, n-i));
		}
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				if(((i^j)&1) == 0 && (in[i][j]&2)){
					g.dx.pb(i+j);
					g.dy.pb(i-j);
				}
		q = g.solve(n+1);
		for(const pair<int, int> &p : q){
			i = (p.fi+p.se)/2;
			j = (p.fi-p.se)/2;
			ans[i][j] |= 2;
		}

		//workDiagOdd
		g.clear();
		for(i = 1; i <= 2*n-2; i += 2){
			g.qx.pb(mp(i, 1 + min(i, 2*n-2-i)));
		}
		for(i = 1; i < n; i += 2){
			g.qy.pb(mp(i, n-i));
			if(i != 0)
				g.qy.pb(mp(-i, n-i));
		}
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				if(((i^j)&1) == 1 && (in[i][j]&2)){
					g.dx.pb(i+j);
					g.dy.pb(i-j);
				}
		q = g.solve(n+1);
		for(const pair<int, int> &p : q){
			i = (p.fi+p.se)/2;
			j = (p.fi-p.se)/2;
			ans[i][j] |= 2;
		}

		int cnt = 0;
		int sum = 0;
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++){
				cnt += (ans[i][j] != 0);
				sum += ((in[i][j] | ans[i][j])&1) + ((in[i][j] | ans[i][j])>>1&1);
			}
		printf("Case #%d: %d %d\n", i0, sum, cnt);
		char toChar[4] = {0, 'x', '+', 'o'};
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				if(ans[i][j])
					printf("%c %d %d\n", toChar[in[i][j] | ans[i][j]], i+1, j+1);
	}
	return 0;
}
