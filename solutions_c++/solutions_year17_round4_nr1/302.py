#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 1e5 + 7;
 

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << t+1 << ": ";
		int n, k;
		cin >> n >> k;
		int cnt[5] = {0};
		for (int i=0; i<n; i++)
		{
			int x; cin >> x;
			cnt[x % k]++;
		}
		int res = cnt[0];
		if (k == 2)
		{
			res += cnt[1] / 2;
			cnt[1] %= 2;
		}
		else
		{
			int need = min(cnt[1], cnt[k-1]);
			cnt[1] -= need;
			cnt[k-1] -= need;
			res += need;
			if (k == 3)
			{
				res += cnt[1] / 3;
				cnt[1] %= 3;
				res += cnt[2] / 3;
				cnt[2] %= 3;
			}
			else
			{
				res += cnt[2] / 2;
				cnt[2] %= 2;
				res += cnt[1] / 4;
				cnt[1] %= 4;
				res += cnt[3] / 4;
				cnt[3] %= 4;
				for (int i=1; i<=3; i+=2)
				{
					int mn = min(cnt[i] / 2, cnt[2]);
					res += mn;
					cnt[i] -= mn * 2;
					cnt[2] -= mn;
				}
			}
		}
		for (int i=1; i<k; i++)
			if (cnt[i])
			{
				res++;
				break;
			}
		cout << res << "\n";
	}

	return 0;
}
