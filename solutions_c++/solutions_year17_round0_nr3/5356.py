#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t<=T; ++t)
	{
		int N, K;

		cin >> N;
		cin >> K;

		cout << "Case #" << t << ": ";

		int p = 0;
		while ((1<<p) <= K)
			++p;
		p--;
		int d = 1<<p;
		int l = (N-d+1) / d;

		if ((K-d) < ((N-d+1) % d))
			cout << (l+1)/2 << " " << l/2 << endl;
		else
			cout << l/2 << " " << (l-1)/2 << endl;

		/*int max1, max2;
		vector<int> gaps;
		gaps.reserve(K * (K+1) / 2);
		gaps.push_back(N);
		vector<int>::iterator beg = gaps.begin();
		for (int i = 1;;++i)
		{
			max1 = (*beg) >> 1;
			max2 = max((*beg)-1,0) >> 1;
			if (i == K)
				break;
			if (i > 1)
			{
				vector<int>::iterator it = gaps.end();
				while (max1 > *(it - 1))
					it--;
				gaps.insert(it, max1);
			}
			else
				gaps.push_back(max1);
			beg++;
			gaps.push_back(max2);
		}
		cout << max1 << " " << max2 << endl;*/
	}

	return 0;
}