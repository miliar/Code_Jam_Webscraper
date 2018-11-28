#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int main() 
{

	int T;
	cin >> T;

	for(int t=1;t<=T;t++) 
	{
		int N;
		int K;
		priority_queue<int> subN;
		int l,r;

		cin >> N >> K;

		subN.push(N);
		N = 0;

		while(K--)
		{
			N = subN.top()-1;
			subN.pop();
			l = floor((double)N / 2.0f);
			r = N - l;
			subN.push(l);
			subN.push(r);
		}

		cout << "Case #" << t << ": ";
		cout << max(l, r) << " " << min(l, r) << endl;
	}

	return 0;
}
