#include<bits/stdc++.h>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int I = 1; I <= T; ++I){
		cout << "Case #" << I <<": ";
		int n, c, m;
		cin >> n >> c >> m;
		vector<pair<int,int> > v(m);
		for(int i = 0; i < m; ++i){
			int b,p;
			cin >> p >> b;
			--b;
			v[i] = {p, b};
		}
		sort(v.begin(), v.end());
		int l = 0, r = 1000;
		while(l+1 < r){
			int mid = (l+r)/2;
			vector<set<int> > tmp(c);
			vector<int> used(mid,0);
			int can = 0;
			for(int i = 0; i < m; ++i){
				int b = v[i].second;
				int p = v[i].first;
				can = 0;
				for(int j = 0; j < mid; ++j){
					if(tmp[b].count(j)) continue;
					if(used[j] < p) {
						can = 1;
						used[j]++;
						tmp[b].insert(j);
						break;
					}
				}
				if(can == 0) {
					break;
				}
			}
			if(can == 0) l = mid;
			else r = mid;
		}
		vector<int> last(r,0);
		bool can = 0;
		int prom = 0;
		for(int i = 0; i < m; ++i){
			int b = v[i].second;
			int p = v[i].first;
			for(int j = 0; j < r; ++j){
				can = 0;
				if(last[j] < p) {
					can = 1;
					last[j] = p;
					break;
				}
			}
			if(can == 0) ++prom;
		}
		cout << r << ' ' << prom << endl;
	}

}
