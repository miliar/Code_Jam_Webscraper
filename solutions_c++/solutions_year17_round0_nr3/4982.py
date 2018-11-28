#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;

	for(int j = 0; j < n; ++j)
	{
		priority_queue<long long int> s;
		int count = 0;
		long long int n, k;
		cin >> n >> k;

		s.push(n);

		while(true) {
			++count;
			long long int atas = s.top();

			if (atas == 0) {
				s.push(0);
				s.push(0);
			} else if (atas % 2 == 0) {
				s.push(atas/2);
				s.push(atas/2 - 1);
			} else {
				s.push(atas/2);
				s.push(atas/2);
			}

			if (count == k) {
				if (atas == 0) {
					cout << "Case #" << j + 1 << ": " << "0 0" << endl;
				} else if (atas % 2 == 0) {
					cout << "Case #" << j + 1 << ": " << atas/2 << " " << atas/2 - 1 << endl; 
				} else {
					cout << "Case #" << j + 1 << ": " << atas/2 << " " << atas/2 << endl; 
				}
				break;
			}

			s.pop();
		}
	}

	return 0;
}