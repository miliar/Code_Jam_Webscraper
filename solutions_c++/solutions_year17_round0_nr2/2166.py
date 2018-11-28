#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

char s[1007];
int t[1007];

int main() {
	ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for(int it = 1; it <= tt; ++it) {
		cin >> (s + 1);
		int n = 0;
		while(s[n + 1]) n++;
		for(int i = 1; i <= n; ++i) t[i] = s[i] - '0';
		
		for(int i = 1; i < n; ++i) {
			if(t[i + 1] < t[i]) {
				int z = i;
				t[z]--;
				while(z > 1 && t[z] < t[z - 1]) {
					t[z - 1]--;
					z--;
				}
				for(int j = z + 1; j <= n; ++j) t[j] = 9;
				break;
			}
		}
		
		cout << "Case #" << it << ": ";
		int p = 1;
		if(t[p] == 0) p = 2;
		for(int i = p; i <= n; ++i) cout << t[i];
		cout << '\n';
	}
	return 0;
}	
