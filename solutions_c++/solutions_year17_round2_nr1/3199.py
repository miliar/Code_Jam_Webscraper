#include <bits/stdc++.h>

using namespace std;

double k[1000], s[1000];

int main()
{
    int __; cin >> __;
    cout << fixed << setprecision(8);
    for (int _ = 1; _ <= __; ++_) {
	double d; int n;
	cin >> d >> n;
	double mx = 1e100;
	for (int i = 0; i < n; ++i) {
	    double k, s;
	    cin >> k >> s;
	    mx = min(mx, d * s / (d - k));
	}
	cout << "Case #" << _ << ": " << mx << endl;
    }
    return 0;
}
