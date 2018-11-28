#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int t;
int n, c, m, pos, buyer;
vector < int > a[2];
int e1, e2;
vector < int > num1, num2;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		
		cin >> n >> c >> m;
		
		a[0].clear();
		a[1].clear();
		e1 = 0;
		e2 = 0;
		num1.clear();
		num2.clear();
		for (int i = 0; i < m; i++) {
			cin >> pos >> buyer;
			a[buyer - 1].push_back(pos);
			if (buyer == 1 && pos == 1)
				e1++;
			else if (buyer == 2 && pos == 1)
				e2++;
		}
		
		int l1 = a[0].size();
		int l2 = a[1].size();
		
		int ans = max(l1, l2) + max(0, min(e1 - l2 + e2, e2 - l1 + e1));
		
		num1.resize(n + 1);
		for (int i = 0; i < l1; i++) {
			num1[a[0][i]]++;
		}
		
		num2.resize(n + 1);
		for (int i = 0; i < l2; i++) {
			num2[a[1][i]]++;
		}
		
		int prom = 0;
		
		for (int i = 2; i <= n; i++) {
			int x = num1[i];
			int y = num2[i];
			
			int temp = max(0, min(x - (l2 - y), y - (l1 - x)));
			prom = max(temp, prom);
		}
		
		
		//~ for (int i = 0; i < l1 && i < l2; i++) {
			//~ int x = a[0][i];
			//~ int y = a[1][l2 - i - 1];
			//~ if (x == y && x != 1)
				//~ prom++;
		//~ }
		
		
		cout << "Case #" << l + 1 << ": ";
		cout << ans << ' ' << prom;
		cout << endl;
	}	
	
	return 0;
}
