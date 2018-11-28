#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1)
inline double sqr(double x) {return x*x;}
const int MAX = 300;
const double inf = 0x3f3f3f3f;
int minu[1450];
int pd[1450][721][2][2];
int run(int idx, int paid, int cur, int strt){
	if(idx == 1440){
		if(paid == 720){
			return (cur != strt);
		}
		else return 15000;
	}
	if(paid > 720)return 15000;
	int &res = pd[idx][paid][cur][strt];
	if(res != -1)return res;
	res = 15000;
	if(minu[idx] == 1){
		if(cur)res = min(res, run(idx+1, paid+1, 1, strt));
		else res = min(res, run(idx+1, paid, 1, strt) + 1);
	}else if(minu[idx] == 0){
		if(cur)res = min(res, run(idx+1, paid+1, 0, strt) + 1);
		else res = min(res, run(idx+1, paid, 0, strt));
	}else {
		if(cur){
			res = min(res, min(run(idx+1, paid+1, 1, strt), 1 + run(idx+1, paid+1, 0, strt)));
		}else {
			res = min(res, min(run(idx+1, paid, 0, strt), 1 + run(idx+1, paid, 1, strt)));
		}
	}
	return res;
}
int solve() {
	int n, m, lf, rg, k;
	scanf("%d %d", &n, &m);
	for(int i = 0; i <= 1450; ++i)minu[i] = -1;
	memset(pd, -1, sizeof pd);
	for(int i = 0; i < n+m; ++i){
		scanf("%d %d", &lf, &rg);
		if(i < n)k = 1;
		else k = 0;
		for(int j = lf; j < rg; ++j)minu[j] = k;
	}
	return min(run(0, 0, 0, 0), run(0, 0, 1, 1));
}
int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; ++i)printf("Case #%d: %d\n", i,  solve());
}
