#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"
/*
I'm gonna fight for the prestige,
not for me, but to uplift my little brothers who are sleeping on concrete floors.
*/

using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef long long ll;
typedef unsigned long long ull;
double R[1010], H[1010];
int n, k;
pdd dp[1010][1010];
int visited[1010][1010];
const double PI = 3.141592653589793;
/// first = final_everything_value
/// second = just carrying bigest R that is being used
pdd combine(pdd a, pdd b) {
	/// b should be single
	pdd ret;
	double minr = min(a.second, b.second);
	double minim = minr*minr * PI;
	ret.first= a.first /*- minim */ + b.first ;
	ret.second = a.second;
	if (b.second > a.second) {
		//double dif = b.second - a.second;
		//dif *= (double)2 * PI;
		ret.second = b.second;
		//ret.first += dif;
	}
	return ret;
}
pdd from_an_i(int i) {
	pdd ret;
	ret.first = /*PI*R[i] * R[i]+*/ (double)2*PI*R[i]*H[i];
	ret.second = R[i];
	return ret;
}
pdd go(int first_n, int use_k) {
	if (first_n < 0 || use_k == 0) {
		return pdd(0, 0);
	}
	if (visited[first_n][use_k]) {
		return dp[first_n][use_k];
	}
	visited[first_n][use_k] = 1;
	pdd tmp = pdd(0, 0);
	int i;
	for (i = 0; i <= first_n; i++) {
		pdd t2=go(i - 1, use_k - 1);
		pdd t_here = from_an_i(i);
		pdd here_combine = combine(t2, t_here);
		double v1 = here_combine.first + PI*here_combine.second*here_combine.second;
		double v2 = tmp.first + PI*tmp.second*tmp.second;
		if (v1 > v2) {
			tmp = here_combine;
		}
	}
	return dp[first_n][use_k] = tmp;
}
void solve() {
	memset(visited, 0, sizeof(visited));
	pdd answer = go(n-1, k);
	double ans = answer.first + PI*answer.second*answer.second;
	cout << setprecision(10) << fixed << ans;
}
int bit_cnt(int val) {
	int ret = val & 1;
	while (val) {
		val >>= 1;
		ret += val & 1;
	}
	return ret;
}
double calculate(int patt) {
	double mxm_r = 0;
	double answer = 0;
	for (int i = 0; i < n; i++) {

		if ((patt & (1 << i)) == 0)continue;
		mxm_r = max(mxm_r, R[i]);
		answer += (double)2 * PI*R[i] * H[i];
	}
	answer += mxm_r*mxm_r*PI;
	return answer;
}
void brute_force() {
	double mxm = 0;
	for (int i = 0; i <= (1 << n); i++) {
		if (bit_cnt(i) > k)continue;
		mxm = max(mxm, calculate(i));
	}
	cout << setprecision(10) << fixed << mxm;
}
int main() {
	int tests;

	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int j;
		cin >> n >> k;
		for (j = 0; j < n; j++) {
			cin >> R[j] >> H[j];
		}
		cout << "Case #" << test << ": ";
		//solve();
		brute_force();
		cout << endl;
	}
	
	return 0;
}
