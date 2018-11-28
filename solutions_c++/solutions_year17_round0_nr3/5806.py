#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
	int t, casee = 0;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		casee++;
		cout << "Case #" << casee << ": ";
		multiset<int> s;
		s.insert(n);
		for (int i = 0; i < k-1; i++)
		{
			int dis = *s.rbegin();
			s.erase(--s.end());
			if (dis % 2)
			{
				s.insert(dis / 2);
				s.insert(dis / 2);
			}
			else {
				s.insert(dis / 2);
				s.insert((dis-1) / 2);
			}
		}
		int dis = *s.rbegin();
		cout << dis / 2 << ' ' << (dis % 2 ? dis / 2 : (dis-1) / 2) << endl;
	}
}
