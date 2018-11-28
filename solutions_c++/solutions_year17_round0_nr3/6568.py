#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

priority_queue < pair<int, pair<int, int> > > pq;
int main()
{
	ofstream outFile("output.out");
	ifstream inFile("C-small-1-attempt0.in");


	int t;
	//cin >> t;
	inFile >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		long long n;
		long long k;
		//cin >> n;
		inFile >> n;
		//cin >> k;
		inFile >> k;

		pq.push(make_pair(n, make_pair(0, n + 1)));

		int l, r, mid;
		for (int i = 0; i < k; i++)
		{
			pair<int, pair<int, int>> cur = pq.top();
			pq.pop();

			l = cur.second.first;
			r = cur.second.second;
			mid = (l + r) / 2;

			pq.push(make_pair(mid - l - 1, make_pair(l, mid)));
			//cout << i << "= a:  " << mid - l << " ,  " << l << " / " << mid << endl;

			pq.push(make_pair(r - mid - 1, make_pair(mid, r)));
			//cout << i << "= a:  " << r - mid << " ,  " << mid << " / " << r << endl;

		}
		int maxH = max(mid - l - 1, r - mid - 1);
		int minH = min(mid - l - 1, r - mid - 1);


		cout << "Case #" << tc << ":" << " " << maxH << " " << minH << endl;
		outFile << "Case #" << tc << ":" << " " << maxH << " " << minH << endl;

		while (!pq.empty())
			pq.pop();
	}

	inFile.close();
	outFile.close();

	return 0;
}
