#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, cas, p, tmp, tmp2, tmp3, ans;
	int a[200];

	cin >> t;
	cas = 1;
	while (t) {
		cin >> n >> p;
		ans = 0;
		
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
			a[i] = a[i] % p;
			if (a[i]==0) ans++;
		}

		if (p==2) {
			tmp = n - ans;
			if (tmp % 2 == 0)
				ans += tmp/2;
			else ans += tmp/2 + 1;
		} else if (p == 3) {
			tmp = 0;
			tmp2 = 0;
			for (int i = 0; i < n; ++i)
				if (a[i]==1)
					tmp++;
				else if (a[i]==2)
					tmp2++;
			if (tmp > tmp2) {
				ans += tmp2;
				tmp -= tmp2;
				if (tmp % 3 == 0)
					ans += tmp/3;
				else ans += tmp/3 + 1;
			} else if (tmp < tmp2) {
				ans += tmp;
				tmp2 -= tmp;
				if (tmp2 % 3 == 0)
					ans += tmp2/3;
				else ans += tmp2/3 + 1;
			} else {
				ans += tmp;
			}
		} else {
			tmp = 0;
			tmp2 = 0;
			tmp3 = 0;
			for (int i = 0; i < n; ++i)
				if (a[i]==1)
					tmp++;
				else if (a[i]==2)
					tmp2++;
				else if (a[i]==3)
					tmp3++;
			ans += tmp2 / 2;
			if (tmp2 % 2 == 0) tmp2 = 0;
			else tmp2 = 1;
			if (tmp > tmp3) {
				ans += tmp3;
				tmp -= tmp3;
				if (tmp % 4 == 0) {
					ans += tmp/4;
					if (tmp2 == 1)
						ans++;
				} else if (tmp % 4 == 3 && tmp2 == 1) {
					ans += tmp/4 + 2;
				} else {
					ans += tmp/4 + 1;
				}
			} else if (tmp < tmp3) {
				ans += tmp;
				tmp3 -= tmp;
				if (tmp3 % 4 == 0) {
					ans += tmp3/4;
					if (tmp2 == 1)
						ans++;
				} else if (tmp3 % 4 == 3 && tmp2 == 1) {
					ans += tmp3/4 + 2;
				} else {
					ans += tmp3/4 + 1;
				}
			} else {
				ans += tmp;
			}

		}
		

		cout << "Case #" << cas++ << ": ";
		cout << ans << endl;
		t--;
	}

	return 0;
}