#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)

int n, c, m;
pair<int,int> A[1111];
int taken[1111], done[1111];
int have[1111][1111], mark[1111][1111];
int arr[1111];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> n >> c >> m;
		For(i,1,m) {
			int x, y;
			scanf("%d %d", &x, &y);
			A[i] = make_pair(x, y);
		}
		sort(A + 1, A + m + 1);
		memset(done, 0, sizeof done);
		int ans = 0;
		For(t,1,1001) {
			int idx = 0;
			memset(taken, 0, sizeof taken);
			For(i,1,m) if (!done[i]) {
				if (A[i].first > idx && !taken[A[i].second]) {
					taken[A[i].second] = true;
					++idx;
					done[i] = true;
				}
			}
			if (idx == 0) {
				ans = t - 1;
				break ;
			}
		}
		memset(have, 0, sizeof have);
		memset(mark, 0, sizeof mark);
		int cnt = 0;
		reverse(A + 1, A + m + 1);
		memset(arr, 0, sizeof arr);
		For(i,1,m) ++arr[A[i].first];
		int cnt2 = 0;
		For(i,1,n) if (arr[i] > ans) cnt2 += arr[i] - ans;
		For(i,1,m) {
			int x = A[i].first, y = A[i].second;
			For(j,1,ans) if (!mark[j][x] && !have[y][j]) {
				++cnt;
				mark[j][x] = have[y][j] = true;
				break ;
			}
		}
		//assert(cnt2 == m - cnt);
		printf("Case #%d: %d %d\n", TK, ans, cnt2);
	}
	return 0;
}