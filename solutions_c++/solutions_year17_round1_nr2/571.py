#include<bits/stdc++.h>
#include<unordered_set>
#include<unordered_map>
using namespace std;
int cnt_t;
void outt(){
	cnt_t++;
	printf("Case #%d: ", cnt_t);
}

int n;
int p;

vector<int> v;

#define MM 2000002

struct st{
	int r;
	int id;
	bool del;
};
vector<st> ev[MM];

multiset<int> ms[52];

int main(){
	int T;
	cin >> T;
	while (T--){
		cin >> n >> p;
		v.clear();
		for (int j = 0; j < 52; j++){
			ms[j].clear();
		}
		for (int i = 0; i < n; i++){
			int r;
			scanf("%d", &r);
			v.push_back(r);
		}
		int mr = 0;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < p; j++){
				int q;
				scanf("%d", &q);
				long double F = q;
				F *= 10.0;
				F /= (long double)(9.0);
				F = floor(F);
				long double FF = q;
				FF *= 10.0;
				FF /= (long double)(11.0);
				FF = ceil(FF);
				int lef = (int)(FF)+v[i] - 1;
				lef /= v[i];
				int rig = (int)(F) / v[i];
				lef = max(lef, 1);
				if (lef <= rig){
					ev[lef].push_back({ rig, i, false });
				}
				mr = max(mr, rig);
			}
		}
		cerr << "rig: " << mr << endl;
		int ans = 0;
		for (int i = 0; i < MM; i++){
			for (int j = 0; j < ev[i].size(); j++){
				if (ev[i][j].del){
					auto it = ms[ev[i][j].id].lower_bound(ev[i][j].r);
					ms[ev[i][j].id].erase(it);
				}
				else{
					ms[ev[i][j].id].insert(ev[i][j].r);
				}
			}
			ev[i].clear();
			for (int j = 0; j < n; j++){
				while (!ms[j].empty() && (*ms[j].begin()) < i){
					ms[j].erase(ms[j].begin());
				}
			}
			while (1){
				bool upd = false;
				for (int j = 0; j < n; j++){
					if (ms[j].size() == 0){
						upd = true;
						break;
					}
				}
				if (upd)break;
				for (int j = 0; j < n; j++){
					ms[j].erase(ms[j].begin());
				}
				ans++;
			}
		}
		outt();
		printf("%d\n", ans);
	}
	return 0;
}