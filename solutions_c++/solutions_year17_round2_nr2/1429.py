#include <bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{

	 freopen("B-small-attempt0 (2).in", "r", stdin);
freopen("B-small-attempt0 (2).out", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		int n, r, o, y, g, b, v;
		std::vector<string> q;
		cin >> n >> r >> o >> y >> g >> b >> v;

		multimap<int, char> m;
		m.insert( pair<int, char>(r, 'R') );
		m.insert( pair<int, char>(o, 'O') );
		m.insert( pair<int, char>(y, 'Y') );
		m.insert( pair<int, char>(g, 'G') );
		m.insert( pair<int, char>(b, 'B') );
		m.insert( pair<int, char>(v, 'V') );

		std::map<int, char>::reverse_iterator it = m.rbegin();

		for (int i = 0; i < it->first; ++i)
		{
			string s = "" ;
			s = s + it->second;
			q.push_back(s);
		}
		
		int curr = 0 ;
		for (std::map<int, char>::reverse_iterator i = ++m.rbegin(); i != m.rend(); ++i)
		{	int f = i->first;
			for (int j = curr; j < curr + f  && j < q.size(); ++j)
			{
				q[j] = q[j] + i->second;
			}
			if ( (curr + f) > q.size())
			        for (int j = 0; j < curr + f - q.size(); ++j)
				{
				q[j] = q[j] + (i->second);
				}
			curr = (curr + f) % ((int)q.size());

 
		}


		cout << "Case #" << k << ": " ;
		if (q[0][0] == q[q.size()-1][q[q.size()-1].size() - 1])
			cout << "IMPOSSIBLE" << endl;
		else
		{for (int i = 0; i < q.size(); ++i)
				{
					cout << q[i] ;
				}
				cout << endl;}
	}
}


