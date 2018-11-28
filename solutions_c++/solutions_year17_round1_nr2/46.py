#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;
const ld eps=1e-9;

ld r[55];
vector<ld> q[55];
int used[5050];

int h[55];

int can(vector<ld> t){
	assert(t.size()>0);
	int mi=0;
	int ma=2e6;
	int f=0;
	while (mi<=ma){
		int mid=(mi+ma)/2;
		if (t[0]+eps>(ld)mid*(ld)0.9){
			mi=mid+1;
			f=mid;
		}
		else{
			ma=mid-1;
		}
	}
	if (f==0) return 0;
	ld lb=(ld)f*0.9;
	ld ub=(ld)f*1.1;
	for (auto x:t){
		if (x<lb-eps||x>ub+eps) return 0;
	}
	return 1;
}

void solve(){
	int n,p;
	cin>>n>>p;
	for (int i=0;i<n;i++){
		cin>>r[i];
		q[i].clear();
	}
	vector<pair<ld, pair<int, int> > > all;
	for (int i=0;i<n;i++){
		q[i].resize(p);
		for (int ii=0;ii<p;ii++){
			cin>>q[i][ii];
			q[i][ii]/=r[i];
			all.push_back({q[i][ii], {i, ii}});
		}
	}
	sort(all.begin(), all.end());
	int v=0;
	memset(used, 0, sizeof(used));
	for (int i=0;i<(int)all.size();i++){
		vector<ld> t;
		vector<int> tt;
		memset(h, 0, sizeof(h));
		for (int j=i;j<(int)all.size();j++){
			if (!used[j]&&!h[all[j].S.F]){
				t.push_back(all[j].F);
				tt.push_back(j);
				h[all[j].S.F]=1;
			}
		}
		if ((int)t.size()==n){
			if (can(t)){
				v++;
				for (int x:tt){
					used[x]=1;
				}
			}
		}
	}
	cout<<v<<endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}