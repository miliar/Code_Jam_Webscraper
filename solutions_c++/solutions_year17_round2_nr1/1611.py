#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

int main()
{
  int T;
  cin >> T;
  cout << setprecision(18);
  
  for(int t = 1; t <= T; t++)
  {
	cerr << "T = " << t << endl;
	ll d, n;
	cin >> d >> n;

	vector<double> ks(n);
	vector<double> ss(n);
	for(int i = 0; i < n; i++)
	{
	  cin >> ks[i] >> ss[i];
	}

	double maxTime = -1e100;
	for(int i = 0; i < n; i++)
	{
	  maxTime = max(maxTime, (d - ks[i]) / ss[i]);
	}
	cout << "Case #" << t << ": " << d / maxTime << endl;
  }
}
