#include <iostream>
#include <cstdio>
#define ll long long

using namespace std;

int t;
string s;
ll ans, a[100], n;

int main() {
	#ifdef LOCAL	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s;
		cout << "Case #" << i << ": ";
		if (s.size() == 1)
			cout << s << endl;
		else {
			n = s.size();
			for (int i = 0; i < n; ++i) 
				a[i] = s[i] - '0';

			int z = 0;
			while (z++ < 19)
				for (int i = 0; i + 1 < n; ++i) {
						if (a[i] <= a[i + 1])
							continue;
						else {
								a[i]--;
								for (int k = i + 1; k < n; ++k)
									a[k] = 9;
							  break;
						}
			}			
			int k = 0;
			while (k < n && a[k] == 0)
				k++;
			while (k < n)
				cout << a[k++];
		  cout << endl;
		}
	}
	return 0;
}





