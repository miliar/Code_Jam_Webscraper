#include <bits/stdc++.h>

using namespace std;

int t, match[110];
long long a[110], b[110][110];

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int n, p;
		long long ans = 0;
		cin >> n >> p;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++)
				cin >> b[i][j];
		if (n == 1)
		{
			for (int j = 0; j < p; j++)
			{
				long long ku = 1000ll * 1000ll * 1000ll * 1000ll * 1000ll;
				long long kl = -ku;
				kl = max(kl, max(-10ll, (10ll * b[0][j] + 11ll * a[0] - 1) / (11ll * a[0])));
				ku = min(ku, max(-10ll, (10ll * b[0][j]) / (9ll * a[0])));
				// cout << kl << " " << ku << endl;
				if (ku <= 0)
					continue;
				kl = max(1ll, kl);
				if (ku >= kl)
					ans += 1;
			}
		}
		else if (n == 2)
		{
			// cout << "SALAM!" << endl;
			sort(b[1], b[1] + p);
			do
			{
				// for (int i = 0; i <= 1; i++)
				// {
				// 	for (int j = 0; j < p; j++)
				// 		cout << b[i][j] << " ";
				// 	cout << endl;
				// }
				long long tmp = 0;
				for (int j = 0; j < p; j++)
				{
					long long ku = 1000ll * 1000ll * 1000ll * 1000ll * 1000ll;
					long long kl = -ku;
					for (int i = 0; i <= 1; i++)
					{
						kl = max(kl, max(-10ll, (10ll * b[i][j] + 11ll * a[i] - 1) / (11ll * a[i])));
						ku = min(ku, max(-10ll, (10ll * b[i][j]) / (9ll * a[i])));
					}
					// cout << kl << " " << ku << endl;
					if (ku <= 0)
						continue;
					kl = max(1ll, kl);
					if (ku >= kl)
						tmp += 1;
				}
				ans = max(ans, tmp);
			} while (next_permutation(b[1], b[1] + p));
			// cout << "END!" << endl;
		}
		cout << "Case #" << tt << ": ";
		cout << ans << endl;
	}
	return 0;
}