#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1445;

int n, k, pos;
double a[N], s[N], x;

int main() {
	freopen("C-small-1-attempt2.in", "r", stdin);
	freopen("2.txt", "w", stdout); 
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		cin >> n >> k;
		cin >> x;
		for (int i = 1; i <= n; i++) cin >> a[i];
		sort(a + 1, a + 1 + n);
		double l=0,r=1;
		while (r-l>=1e-10) {
			double mid=(r+l)/2;
			double s=0;
			for (int i=1;i<=n;i++)
			if (a[i]<mid) s+=mid-a[i];
			if (s>x) r=mid;
			else l=mid;
		}
		double ans=1;
		for (int i=1;i<=n;i++)
		if (a[i]<l) ans*=l;
		else ans*=a[i];
		printf("Case #%d: %.10f\n", ++cas, ans);
	}
}
