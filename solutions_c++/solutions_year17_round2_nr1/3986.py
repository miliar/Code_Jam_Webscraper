#include <iostream>
#include<iomanip>
using namespace std;
double z, n, d, a, b;
double buf, koniec;
double minimum;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout << setprecision(6);
	cin >> z;
	for(int i = 1; i<=z; i++)
	{
	cin >> d >> n;
	minimum = 0;
	for(int j = 1; j<=n; j++)
		{
			cin >> a >> b;
			buf = (d-a)/b;
			minimum=max(minimum, buf);
		}
		koniec = d/minimum;
		cout << "Case #" << i << ": " << fixed << koniec << "\n";
	}
	return 0;
}