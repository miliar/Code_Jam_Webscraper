										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n;
double d;

int main(){
	std::ios::sync_with_stdio(false);
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> d >> n;
		double mx = 0;
		for(int i = 0; i < n; i++){
			double k, s;
			cin >> k >> s;
			mx = max(mx, (d - k) / s);
		}
		double res = d / mx;
		cout << "Case #" << ++test << ": " << setprecision(6) << fixed << res << endl;
	}
	return 0;
}
