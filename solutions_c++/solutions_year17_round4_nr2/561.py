#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define fi first
#define se second
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;


int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int C, N, M;
		int cnt_C[1100] = {}, cnt_N[1100] = {};
		cin >> N >> C >> M;

		int l, r;
		l = 0;
		r = M;
		for(int i = 0; i < M; i++) {
			int P, B;
			cin >> P >> B;
			cnt_C[B-1]++;
			cnt_N[P-1]++;
			l = max(l,cnt_C[B-1]);
		}
		int res_y, res_z = 1e9;

		while(l <= r) {
			int m = (l+r)/2;
			int rest = 0;
			int promote = 0;
			bool f = true;
			for(int i = 0; i < N; i++) {
				if(cnt_N[i] <= m) {
					rest += m-cnt_N[i];
				}
				else {
					if(rest >= cnt_N[i]-m) {
						promote += cnt_N[i]-m;
						rest -= (cnt_N[i]-m);
					}
					else {
						f = false;
					}
				}
			}

			if(f) {
				res_y = m;
				res_z = promote;
				r = m-1;
			}
			else {
				l = m+1;
			}
		}
		cout << "Case #" << t+1 << ": " << res_y << " " << res_z << endl;
	}
	return 0;
}
