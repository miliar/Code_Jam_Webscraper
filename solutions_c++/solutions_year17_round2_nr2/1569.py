#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int c[20];

// vector<int> node[1005];

// int cn[1005];
// int idx = 0;

priority_queue<pair<int, int> > pq;
char ans[1005];

vector<pair<int, int> > v;

char ss[7] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int main(){
	int T;
	cin >> T;
	int t=1;
	for(;t<=T;t++){
		int N;
		cin >> N;
		v.clear();
		for(int i=0;i<6;i++) cin >> c[i];
		for(int i=0;i<6;i++){
			if(c[i] == 0) continue;
			v.push_back(make_pair(-c[i], i));
		}
		memset(ans, 0, sizeof(ans));
		sort(v.begin(), v.end());


		if(v.size() == 1){
			printf("Case #%d: ", t);
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		char rr[7];
		for(int i=0;i<v.size();i++){
			int color = v[i].second;
			rr[i] = ss[v[i].second];
			v[i].second = i;
		}

		int co = 0;
		bool ok = 1;
		int pv = -1;

		for(int i=0;i<N;i++){
			int j = 0;
			while(j < v.size() && v[j].first == 0) j++;
			if(j == v.size()) break;
			if(v[j].second == pv) j++;
			while(j < v.size() && v[j].first == 0) j++;
			if(j == v.size()) break;

			ans[i] = rr[v[j].second];
			v[j].first++;
			pv = v[j].second;
			sort(v.begin(), v.end());
		}

		ans[N] = '\0';
		
		for(int i=1;i<N;i++){
			if(ans[i] == ans[i-1] || ans[i] == 0 || ans[i-1] == 0){
				ok = 0;
				break;
			}
		}

		if(ans[0] == ans[N-1]) ok = 0;
		printf("Case #%d: ", t);
		if(ok) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}