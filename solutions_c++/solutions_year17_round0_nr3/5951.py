#include <bits/stdc++.h>
using namespace std;

bool arr[1003];
int ls[1003], rs[1003];

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t) {
		int n, k;
		scanf("%d %d", &n, &k);

		memset(arr, 0, sizeof(arr));

		int y = -1, z = -1;
		while(k--) {
			int prv = -1;
			for(int i = 0; i < n; ++i) {
				if(arr[i])
					prv = i;
				else
					ls[i] = (i - prv) - 1;
			}
			prv = n;
			for(int i = n - 1; i >= 0; --i) {
				if(arr[i])
					prv = i;
				else
					rs[i] = (prv - i) - 1;
			}

			int pos = -1;

			for(int i = 0; i < n; ++i) {
				if(arr[i])
					continue;


				if(pos == -1) {
					pos = i;
					continue;
				}
				if(min(ls[i], rs[i]) > min(ls[pos], rs[pos]) ||
						(min(ls[i], rs[i]) == min(ls[pos], rs[pos])
												&& max(ls[i], rs[i]) > max(ls[pos], rs[pos])))
					pos = i;
			}

			arr[pos] = 1;
			y = max(ls[pos], rs[pos]);
			z = min(ls[pos], rs[pos]);
		}

		cout << "Case #" << t <<": " << y << " " << z << "\n";
	}
	return 0;
}
