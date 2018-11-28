#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main(){
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> t;
	for(int i = 0 ;i < t; i++){
		int n, d;
		int k, s;
		cin >> d >> n;
		double ans = -1;
		for(int i = 0; i < n ; i++){
			cin >> k >> s;
			double x = s + k / (double)(d - k) * (double)s;
			if(ans < 0)
				ans = x;
			else ans = min(ans, x);
		}
		cout.precision(7);
		cout.flags(ios::fixed);

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}