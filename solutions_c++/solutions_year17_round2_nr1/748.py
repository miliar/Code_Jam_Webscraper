#include <iostream>
#include <iomanip>
#include <cstring>
#include <stdio.h>
using namespace std;

int main()
{
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	int count = 1;
	while(t--)
	{
		int dis;
		int number;
		cin >> dis >> number;
		double large = 0;
		while(number--)
		{
			int a,b;
			cin >> a >> b;
			large = max(large, (dis - a) * 1.0 / b);
		}
		cout << "Case #"<<count++ << ": ";
		cout << fixed << setprecision(10) << dis*1.0 / large << endl;
	}
}
