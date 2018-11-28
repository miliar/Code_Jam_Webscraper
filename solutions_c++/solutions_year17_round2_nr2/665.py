#include <iostream>
#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int t;
int n, r, o, y, g, b, v;
string s;
char temp, last;
vector < pair < int, char > > my;
char first;


bool cmp(pair < int, char > a, pair < int, char > b)
{
	if (a.first == b.first)
		return (a.second == first);
	return a.first > b.first;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> n >> r >> o >> y >> g >> b >> v;
		s = "IMPOSSIBLE";
		my.clear();
		my.push_back(make_pair(r, 'R'));
		my.push_back(make_pair(y, 'Y'));
		my.push_back(make_pair(b, 'B'));
		
		if (r <= y + b && y <= r + b && b <= r + y) {
			s = "";
			last = 0;
			sort(my.rbegin(), my.rend());
			first = my[0].second;
			for (int i = 0; i < n; i++) {
				sort(my.begin(), my.end(), cmp);
				temp = my[0].second;
				if (temp == last) {
					temp = my[1].second;
					my[1].first--;
				} else 
					my[0].first--;
				s += char(temp);		
				last = temp;
			}
		}
		
		cout << "Case #" << l + 1 << ": ";
		cout <<s;
		cout << endl;		
	}
	
	
	return 0;
}
