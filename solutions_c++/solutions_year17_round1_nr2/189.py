#include <bits/stdc++.h>

using namespace std;

typedef long long lint;
typedef pair<int,int> pii;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for (int asd = 0; asd<T; ++asd){
		int n, m;
		cin >> n >> m;
		multiset<double> ing[51];
		double serv[51];
		vector<int> firsting;
		for (int i=0; i < n; ++i){
			cin >> serv[i];
		}
		for (int i=0; i<m; ++i){
			int x; cin >> x; firsting.push_back(x);
		}
		sort(firsting.begin(), firsting.end());

		for (int i=1; i<n; ++i){
			for (int qq=0; qq<m; ++qq){
				double x; cin >> x;
				ing[i].insert(x);
			}
		}
		int ans = 0;

		for (double x : firsting){
			int maxnserv = int(x/serv[0]/0.9 + 1.0), minnserv = int(x/1.1/serv[0] - 1.0);
			for (int nserv = minnserv; nserv <= maxnserv; ++nserv){
				double lrange1 = double(nserv)*serv[0]*0.9, rrange1 = double(nserv)*serv[0]*1.1;
				if (x < lrange1 || rrange1 < x) continue;

				double isvalid = true;

				for (int i=1; i<n; ++i){
					double lrange = double(nserv)*serv[i]*0.9 - 1e-15, rrange = double(nserv)*serv[i]*1.1 + 1e-15;
					if (ing[i].lower_bound(lrange) == ing[i].upper_bound(rrange)){
						isvalid = false; break;
					}
				}
				if (!isvalid) continue;

				for (int i=1; i<n; ++i){
					double lrange = double(nserv)*serv[i]*0.9 - 1e-15, rrange = double(nserv)*serv[i]*1.1 + 1e-15;
					ing[i].erase(ing[i].lower_bound(lrange));
				}
				ans++;
				break;
			}
		}
		printf("Case #%d: %d\n", asd+1, ans);


	}
	return 0;
}