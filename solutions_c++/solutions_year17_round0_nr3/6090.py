#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		long long N, K;
		cin >> N >> K;
		
		long long dK = K;
		int order = 1;
		while (dK)
		{
			dK /= 2;
			order *= 2;
		}
		
		long double segment = (long double)(N-K)/order;
			
		cout << "Case #" << t+1 << ": " << round(segment) << " " << floor(segment) << endl;
	}
}