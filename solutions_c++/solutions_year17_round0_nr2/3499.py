#include<bits/stdc++.h>
#define int long long
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define INF (1ll<<60)
typedef pair<int, int> pii;
#define FI first
#define SE second
#define all(s) s.begin(),s.end()
#define RREP(i,n) for(int i=(n)-1;i>=0;--i)
#define pb push_back
#define mp make_pair
#define l_b lower_bound
#define u_b upper_bound

int keta[20];
int sa[19];
//10^a
int ke(int n, int a) {
	int k = 1;
	rep(i,a)
	{
		k *= 10;
	}
	return n / k % 10;
}
signed main() {
	int t;
	cin >> t;
	rep(i,t)
	{
		int n;
		cin >> n;
		memset(keta, 0, sizeof(keta));
		memset(sa, 0, sizeof(sa));
		rep(j,20)
		{
			keta[j] = ke(n, j);
		}
		reverse(keta, keta + 20);
		int itiyoriookiisaisyonokazu = -1;
		rep(j,19)
		{
			sa[j + 1] = keta[j + 1] - keta[j];
			if (sa[j + 1] > 0) {
				itiyoriookiisaisyonokazu = j + 1;
			}
			if (sa[j + 1] < 0) {
				keta[itiyoriookiisaisyonokazu]--;
				for (int k = itiyoriookiisaisyonokazu + 1; k < 20; ++k) {
					keta[k] = 9;
				}
				break;
			}
		}
		bool z = false;
		cout << "Case #" << i + 1 << ": ";
		rep(j,20)
		{
			if (keta[j] != 0)
				z = true;
			if (z)
				cout << keta[j];
		}
		cout << endl;
	}
}
