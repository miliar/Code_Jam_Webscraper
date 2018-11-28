#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<lint, lint> pi;

int n, m, chk1[105][105], chk2[105][105];
int prv[105][105];

void solve1(){
	int v1[105] = {}, v2[105] = {};
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			if(chk1[i][j]) v1[i] = v2[j] = 1;
		}
	}
	for(int i=1; i<=n; i++){
		if(!v1[i]){
			for(int j=1; j<=n; j++){
				if(!v2[j]){
					chk1[i][j] = 1;
					v2[j] = v1[i] = 1;
					break;
				}
			}
		}
	}
}

void solve2(){
	int v1[205] = {}, v2[205] = {};
	vector<pi> v;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			v.push_back(pi(i, j));
			if(chk2[i][j]) v1[i+j] = 1, v2[i-j+n] = 1;
		}
	}
	sort(v.begin(), v.end(), [&](const pi &a, const pi &b){
		return abs(a.first - a.second) > abs(b.first - b.second);
	});
	for(auto &i : v){
		if(!v1[i.first + i.second] && !v2[i.first - i.second + n]){
			v1[i.first + i.second] = 1;
			v2[i.first - i.second + n] = 1;
			chk2[i.first][i.second] = 1;
		}
	}
}
void solve(){
	cin >> n >> m;
	int ans = 0;
	int v1[105] = {};
	for(int i=0; i<m; i++){
		int x, y;
		char z[3];
		cin >> z >> x >> y;
		if(*z != '+'){
			chk1[x][y] = 1;
			prv[x][y] += 1;
		}
		if(*z != 'x'){
			chk2[x][y] = 1;
			prv[x][y] += 2;
		}
	}
	solve1();
	solve2();
	vector<tuple<char, int, int> > v;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			ans += chk1[i][j] + chk2[i][j];
			if(prv[i][j] != chk1[i][j] + 2 * chk2[i][j]){
				if(chk1[i][j] && !chk2[i][j]) v.emplace_back('x', i, j);
				if(!chk1[i][j] && chk2[i][j]) v.emplace_back('+', i, j);
				if(chk1[i][j] && chk2[i][j]) v.emplace_back('o', i, j);
			}
		}
	}
	cout << ans << " " << v.size() << endl;
	for(auto &i : v){
		cout << get<0>(i) << " " << get<1>(i) << " " << get<2>(i) << endl;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		solve();
		memset(chk1, 0, sizeof(chk1));
		memset(chk2, 0, sizeof(chk2));
		memset(prv, 0, sizeof(prv));
	}
}
