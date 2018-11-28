#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int n, c, m;
		cin >> n >> c >> m;
		vector <int> ci[2];
		for (int i = 0; i < m; i++){
			int p, b;
			cin >> p >> b;
			p--;
			b--;
			ci[b].push_back(p);
		}

		vector<pair<int, int> > v;
		bool found = true;
		while (found){
			found = false;
			pair<int, int> p;
			for (int i = 0; i < ci[0].size() && !found; i++){
				for (int j = 0; j < ci[1].size()&& !found; j++){
					if (ci[0][i] != ci[1][j]){
						p.first = i;
						p.second = j;
						found = true;
					}
				}
			}
			if (found){
				swap(ci[0][p.first], ci[0][ci[0].size() - 1]);
				swap(ci[1][p.second], ci[1][ci[1].size() - 1]);
				p.first = ci[0].back();
				p.second = ci[1].back();
				v.push_back(p);
				ci[0].pop_back();
				ci[1].pop_back();
			}
		}


		//try replacement 
		for (int i = 0; i < v.size(); i++){
			if (ci[0].size() > 0 && ci[1].size() > 0){
				if (ci[0][0] != v[i].first && ci[0][0] != v[i].second){
					swap(ci[0][0], v[i].first);
					swap(ci[0][0], ci[0][ci[0].size() - 1]);
					v.push_back(make_pair(ci[0].back(), ci[1].back()));
					ci[0].pop_back();
					ci[1].pop_back();
				}
			}
		}
		int ans;
		int promo = 0;
		if (ci[0].size() > 0 && ci[1].size() > 0 && ci[0][0] != 0){
			ans = v.size() + max(ci[0].size(), ci[1].size());
			promo = min(ci[0].size(), ci[1].size());
		}
		else {
			ans = v.size() + ci[0].size() + ci[1].size();
		}
		cout << "Case #" << z << ": " << ans << " " << promo  << endl;
	}
	return 0;
}