#include <iostream>
#include <string>
#include<iomanip>

using namespace std;
class horse {
	public :double k;
	public :double s;
};

int main()
{
	int t, ct;
	freopen("a.in", "r", stdin);
	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		cout << "Case #" << t << ": ";
		int d, n;
		cin >> d >> n;
		horse* h = new horse[n];
		for (int i = 0; i < n; i++) {
			cin >> h[i].k >> h[i].s;
		}
		double t = (double)(d - h[0].k) / h[0].s;
		for (int i = 0; i < n; i++) {
			if(t < ((double)(d - h[i].k) / h[i].s)) t = (d - h[i].k) / h[i].s;
		}
		double rs = (double)d / t;
		cout << setprecision(6)<<fixed<<rs << endl;
	}


	return 0;
}
