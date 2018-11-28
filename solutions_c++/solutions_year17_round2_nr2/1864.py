#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		double n;
		cin >> n;

		char c[] = {'R','O', 'Y', 'G', 'B', 'V'};
		vector < pair<int, char> > colors;
		for(int i = 0; i < 6; i++) {
			pair<int,int> p;
			cin >> p.first;
			p.second = c[i];
			if(!(i%2)) {
				colors.push_back(p);
				// cout << colors[i/2].second << endl;
			}
		}

		sort(colors.rbegin(), colors.rend());
		// for(int i = 0; i < 3; i++) {
			// cout << colors[i].second << endl;
		// }

		cout << "Case #" << t << ": ";
		if(colors[0].first > colors[1].first+colors[2].first) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		// int gret = 0;
		for(int i = 0; i < colors[0].first-colors[1].first; i++) {
			// cout << gret;
			// cout << colors[0].second << endl;
			// cout << colors[1].second << endl;
			cout << colors[0].second << colors[2].second;
			colors[2].first--;
			// cout << colors[gret].first << endl; 
			// cout << colors[gret^1].first << endl; 
			// if(colors[gret].first <= colors[gret^1].first) gret = gret^1;
			// cout << gret << endl;
		}
		colors[0].first = colors[1].first;
		for(int i = 0; i < colors[2].first; i++) {
			// cout << "vidal" << endl;
			cout << colors[0].second << colors[1].second << colors[2].second;
			colors[0].first--;
			colors[1].first--;
		}
		// gret = 0;
		for(int i = 0; i < colors[0].first; i++) {
			cout << colors[0].second << colors[1].second;
		}
		cout << endl;


	}
}