#include <iostream>
#include <string>
#include <vector>
#include <array>
using namespace std;
int main()
{
	int cases = 0;
	cin >> cases;
	for (int T = 1; T <= cases; T++)
	{
		int N; //Stalls
		int K; //People
		cin >> N;
		cin >> K;
		cout << "Case #" << (T) << ": ";
		vector<int> options;
		options.push_back(N);
		int maxOptions = 0;
		int d1, d2 = 0;
		for (int i = 0; i < K-1; i++)
		{
			maxOptions = (int)options.back();
			options.pop_back();
			if ((maxOptions % 2) == 0)
			{
				d1 = maxOptions / 2;
				d2 = d1 - 1;
			}
			else
			{
				d1 = d2 = (maxOptions - 1) / 2;
			}
			options.push_back(d1);
			options.push_back(d2);
			std::sort(options.begin(), options.end(), [](int a, int b) {
				return a < b;
			});
		}
		//Final Values
		maxOptions = (int)options.back();
		if ((maxOptions % 2) == 0)
		{
			d1 = maxOptions / 2;
			d2 = d1 - 1;
		}
		else
		{
			d1 = d2 = (maxOptions - 1) / 2;
		}
		cout << d1 << " " << d2 << endl;
	}
}