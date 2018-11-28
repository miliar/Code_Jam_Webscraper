#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
#define ALL(x) (x.begin(), x.end())
#define mset(a,i) memset(a,i,sizeof(a))
#define rep(i,n) for(int i = 0;i < n;i ++)

const int N = 1e5 + 5;
vector<int> C[4];

int main() {
	int T, n, P, x;
	scanf("%d", &T);
	rep(cas, T) {
		rep(i, 4) {
			C[i].clear();
		}
		scanf("%d%d", &n, &P);
		rep(i, n) {
			scanf("%d", &x);
			C[x%P].push_back(x);
		}
		int siz = C[0].size();
		int answer = siz;
		int c1, c2, c3;
		if (P == 2) {
			siz = C[1].size();
			answer += siz / 2 + (siz % 2);
		} else if (P == 3) {
			c1 = C[1].size();
			c2 = C[2].size();
			if (c1 < c2) {
				swap(c1, c2);
			}
			answer += c2;
			c1 -= c2;
			answer += c1 / 3 + (c1 % 3 != 0);
		} else if (P == 4) {
			c1 = C[1].size();
			c2 = C[2].size();
			c3 = C[3].size();
			if (c1 < c3) {
				swap(c1, c3);
			}
			answer += c3;
			c1 -= c3;
			answer += c1 / 4;
			answer += c2 / 2;
			int remain2 = c2 % 2;
			int remain1 = c1 % 4;
			if (remain2 || remain1) {
				answer ++;
			}
			if (remain2 && remain1 == 3) {
				answer ++;
			}
		}
		printf("Case #%d: %d\n", cas + 1, answer);
	}
    return 0;
}

