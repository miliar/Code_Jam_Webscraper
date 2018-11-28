#include <bits/stdc++.h>

using namespace std;

typedef long long ll;






int main()
{
	ll casses;
	cin >> casses;
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		ll d, n;
		double slowest = 0;
		cin >> d >> n;
		for(int i = 0; i < n; i++)
		{
			ll distance, speed;
			cin >> distance >> speed;
			if(distance > d)
			{
				continue;
			}
			double tempSlowest = (d - distance) / (double)speed;
			if(tempSlowest > slowest)
			{
				slowest = tempSlowest;
			}
		}
		cout << "Case #" << caseNum + 1 << ": " << fixed << std::setprecision(8) << d / (double)slowest << endl;
	}
	return 0;
}










