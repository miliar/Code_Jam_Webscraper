#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

int a[1010];
int u[1010];
int w[1010];

int n,m,c;

int can(int x, vector<pair<int, int> >& t){
	for (int i=1;i<=c;i++) a[i]=0;
	for (int i=0;i<m;i++) u[i]=0;
	
	for (int i=1;i<=x;i++){
		set<int> pos;
		for (int j=1;j<=n;j++) pos.insert(j);
		for (int j=0;j<m;j++){
			if (u[j]==0){
				if (a[t[j].S]==i) continue;
				auto it=pos.upper_bound(t[j].F);
				if (it!=pos.begin()){
					it--;
					pos.erase(it);
					u[j]=1;
					a[t[j].S]=i;
				}
			}
		}
	}
	for (int j=0;j<m;j++){
		if (!u[j]) return 0;
	}
	return 1;
}

void solve(){
	cin>>n>>c>>m;
	vector<pair<int, int> > t;
	for (int i=1;i<=n;i++) w[i]=0;
	for (int i=0;i<m;i++){
		int p,b;
		cin>>p>>b;
		w[p]++;
		t.push_back({p, b});
	}
	sort(t.begin(), t.end());
	int mi=0;
	int ma=m;
	int v=0;
	while (mi<=ma){
		int mid=(mi+ma)/2;
		if (can(mid, t)){
			ma=mid-1;
			v=mid;
		}
		else{
			mi=mid+1;
		}
	}
	int os=0;
	for (int i=1;i<=n;i++){
		os+=min(w[i], v);
	}
	cout<<v<<" "<<m-os<<endl;
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