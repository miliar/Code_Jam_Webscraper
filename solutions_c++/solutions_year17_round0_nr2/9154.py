#include <bits/stdc++.h>

using namespace std;

int main() {

	// freopen("b.in", "r", stdin);
	// freopen("b.out", "w", stdout);

	int t, counter = 0;
	string st;

	cin >> t;

	while(t--) {
		cin >> st;

		bool ok = true;
		int index = -1;

		for (int i = 0; i < st.size() - 1; i++) {
			if (st[i] > st[i + 1]) {
				ok = false;
				while (i > 0 && st[i] - 1 < st[i - 1])
					i--;
				st[i]--;
				index = i;
				break;
			}
		}
		counter++;
		cout << "Case #" << counter << ": "; 

		if (index == -1)
			cout << st << "\n";
		else {
			for (int i = 0; i < index; i++)
				cout << st[i];
			
			if (st[index] > '0')
				cout << st[index];
			
			for (int i = index + 1; i < st.size(); i++)
				cout << '9';	
			cout << '\n';
		}
	}
	return 0;
}