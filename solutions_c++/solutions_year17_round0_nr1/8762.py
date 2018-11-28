#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		int k, cont = 0;
		string s;
		cin >> s >> k;
		for (int j = 0; j < s.size() - k + 1; j++) {
			if (s[j] == '-') {
				for (int p = 0; p < k; p++)
					s[j + p] = s[j + p] == '-' ? '+' : '-';
				cont++;
				j--;
			}
		}
		bool imp = false;
		for (int p = 0; p < s.size(); p++)
			if (s[p] == '-') {
				imp = true;
				break;
			}
		
		if (imp) cout << "Case #" << i << ": IMPOSSIBLE"<<endl;
		else cout << "Case #" << i << ": " << cont<<endl;
	}
}