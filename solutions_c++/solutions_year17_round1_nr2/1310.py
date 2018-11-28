#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<cassert>
using namespace std;

#define SMALL 1
//#define LARGE 1

struct ent{
	int evt, ind, id, val;
	bool operator<(const ent& e) const {
		if(val != e.val)
			return val < e.val;
		return evt < e.evt;
	}
};

long long max(long long a, long long b) {
	return a>b?a:b;
}

pair<int, int> getRange(long long x, long long req) {
	auto ret = make_pair(-1, -1);
	//cerr<<ret.first<<" "<<ret.second<<" "<<req<<" "<<x<<endl;
	for(int i=x/req+1,cnt=0;i>=1;i--,cnt++) {
		if(i*req*110 >= x*100 && i*req*90 <= x*100)
			ret.first = i;
		else if(cnt > 10)
			break;
	}
	for(int i=max(x/req-1, 1),cnt=0;;i++,cnt++) {
		if(i*req*110 >= x*100 && i*req*90 <= x*100)
			ret.second = i;
		else if(cnt > 10)
			break;
	}
	assert(!((ret.first == -1)^(ret.second == -1)));
	return ret;
}

void removeSmallest(vector<int>& v, vector<bool>& vis, vector<int>& ends) {
	int mn = -1, ind = -1;
	for(int i=0;i<v.size();i++) {
		if(mn == -1 || ends[v[i]] < mn) {
			mn = ends[v[i]];
			ind = i;
		}
	}
	//cerr << ind << endl;
	vis[v[ind]] = 1;
	v.erase(v.begin()+ind);
}

int main() {
#ifdef LARGE
	freopen("b_large.i", "rt", stdin);
	freopen("b_large.o", "wt", stdout);
#elif SMALL
	freopen("b_small.i", "rt", stdin);
	freopen("b_small.o", "wt", stdout);
#else
	freopen("b_sample.i", "rt", stdin);
#endif

	int tc = 0;
	cin>>tc;
	for(int tt=1;tt<=tc;tt++) {
		int n, p, val;
		cin>>n>>p;
		vector<int> r(n);
		for(int i=0;i<n;i++) cin>>r[i];
		vector<int> ends;
		vector<ent> evts;
		int id=0;
		for(int i=0;i<n;i++) {
			for(int j=0;j<p;j++) {
				cin>>val;
				auto x = getRange(val, r[i]);
				//cerr<<i<<" "<<j<<": "<<x.first<<" "<<x.second<<endl;
				if(x.first == -1)
					continue;
				ent st = {0, i, id, x.first};
				ent end = {1, i, id, x.second};
				ends.push_back(x.second);
				id++;
				evts.push_back(st);
				evts.push_back(end);
			}
		}
		sort(evts.begin(), evts.end());
		vector<bool> vis(id);
		vector<vector<int> > v(n);
		int ans = 0;
		for(auto& e : evts) {
			//cerr << e.evt<<endl;
			if(e.evt == 1) {
				if(vis[e.id]) continue;
				bool found = 0;
				for(int j=0;j<v[e.ind].size();j++) {
					if(v[e.ind][j] == e.id) {
						v[e.ind].erase(v[e.ind].begin()+j);
						found = 1;
						break;
					}
				}
				assert(found);
			} else {
				v[e.ind].push_back(e.id);
				int cnt = 0;
				for(int j=0;j<v.size();j++) cnt+=(v[j].size()>=1);
				//cerr << cnt << endl;
				if(cnt != n)
					continue;
				ans++;
				for(int j=0;j<v.size();j++)
					removeSmallest(v[j], vis, ends);
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}

	return 0;
}
