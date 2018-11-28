#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

double doCase()
{
	double D;
	int N;
	cin >> D >> N;
	double latest = 0;
	for (int i=0; i<N; i++)
	{
		double K, S;
		cin >> K >> S;
		latest = max(latest, (D-K)/S);
	}
	return (D/latest);
}

int main()
{
	int T;
	cin >> T;
	cout << fixed;
	for (int i=0; i<T; i++) cout << setprecision(6) << "Case #" << i+1 << ": " << doCase() << endl;
	return 0;
}