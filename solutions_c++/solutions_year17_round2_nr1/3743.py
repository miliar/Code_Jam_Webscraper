#include <iostream>
#include <string>
using namespace std;


int main()
{
	int cases = 0;
	cin >> cases;
	for (int T = 1; T <= cases; T++)
	{
		cout << "Case #" << (T) << ": " ;
		double D;
		int N;
		cin >> D;
		cin >> N;
		double maxTime = 0;
		for (int i = 0; i < N; i++)
		{
			double Ki, Si;
			cin >> Ki; //Start Position of horse i
			cin >> Si; //Max speed of horse i
			double time = (D - Ki) / Si; //time = Distance / speed
			if (time > maxTime)
				maxTime = time;
		}
		double result = D / maxTime;
		cout << fixed<< result << endl; // Distance / time = speed
	}
}