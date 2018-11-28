#include<bits/stdc++.h>
/*
*/

using namespace std;


int main() {
	long long int T;
	cin >> T;
	for (size_t index = 0; index < T; index++)
	{
		long long int N, K;
		cin >> N >> K;
		map<long long int, long long int>D;
		D[N] = 1;
		long long int y, z;
		while (K > 0)
		{
			auto now = *D.rbegin();
			K -= now.second;
			long long int X = now.first / 2;
			long long int Y = now.first - now.first / 2 - 1;
			y = X;
			z = Y;
			D[X] += now.second;
			D[Y] += now.second;
			D.erase(now.first);
		}
		cout << "Case #" << index + 1 << ": " << max(y, z) << " " << min(y, z) << endl;
	}
}
