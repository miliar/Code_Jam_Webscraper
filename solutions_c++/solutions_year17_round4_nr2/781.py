#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;

int tttt;
void outt(){
	tttt++;
	cout << "Case #" << tttt << ": ";
}


int t;

int n;
int m;
int c;

vector<int> v[2];
map<int, int> mp[2];


int main(){
	cin >> t;
	while (t--){
		scanf("%d%d%d", &n, &c, &m);
		v[0].clear();
		v[1].clear();
		mp[0].clear();
		mp[1].clear();
		for (int i = 0; i < m; i++){
			int p, b;
			scanf("%d%d", &p, &b);
			b--;
			v[b].push_back(p);
			mp[b][p]++;
		}
		outt();
		sort(v[0].begin(), v[0].end());
		sort(v[1].begin(), v[1].end());
		if (v[1].size() == 0){
			cout << v[0].size() << " 0" << endl;
			continue;
		}
		if (v[0].size() == 0){
			cout << v[1].size() << " 0" << endl;
			continue;
		}
		if (v[0].size() > v[1].size()){
			swap(v[0], v[1]);
			swap(mp[0], mp[1]);
		}
		int ans1 = max(v[0].size(), v[1].size());
		int ans2 = 0;
		for (auto it = mp[0].begin(); it != mp[0].end(); it++){
			int A = (*it).second;
			int ot = v[1].size() - mp[1][(*it).first];
			if (ot < A){
				int need = A - ot;
				if ((*it).first == 1){
					ans1 += need;
					continue;
				}
				ans2 += need;
			}
		}
		cout << ans1 << " " << ans2 << endl;
	}
	return 0;
}