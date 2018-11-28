#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define ull unsigned long long
#define ll long long
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}

int T,N,P;

pair<int,int> quote(int ing, int need){
	int l = ing*10/ (11*need);
	if(11*need*l < ing*10) l++;

	int r = ing*10 / (9*need);
	if(9*need*r > ing*10) r--;

	return make_pair(l,r);
}

int main(){
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> N >> P;
		vector<int> R(N,0);
		vector<vector<int>> Q(N,vector<int>(P,0));
		for(int i=0;i<N;++i){cin >> R[i];}
		for(int i=0;i<N;++i){
			for(int j=0;j<P;++j){
				cin >> Q[i][j];
			}
			sort(Q[i].begin(),Q[i].end());
		}

		vector<int> ps(N,0);
		int res = 0;
		int ps_sum = 0;
		while(ps_sum < N*P){
			auto qt = quote(Q[0][ps[0]],R[0]);
			bool flag = false;
			while(ps[0] < P && qt.first > qt.second){
				ps[0]++;ps_sum++;
				if(ps[0]==P) {flag = true;break;}
				qt = quote(Q[0][ps[0]],R[0]);
			}
			if(flag) break;
			int lw = qt.first;int lw_ind = 0;
			int hi = qt.second;int hi_ind = 0;
			for(int i=1;i<N;++i){
				qt = quote(Q[i][ps[i]],R[i]);
				while(ps[i] < P && qt.first > qt.second){
					ps[i]++;ps_sum++;
					if(ps[i] == P) {flag = true;break;}
					qt = quote(Q[i][ps[i]],R[i]);
				}
				if(flag) break;
				if(qt.first > lw) {lw = qt.first;lw_ind = i;}
				if(qt.second < hi) {hi = qt.second;hi_ind = i;}
			}
			if(flag) break;
			if(lw <= hi) {
				res++;
				for(int i=0;i<N;++i) {ps[i]++;ps_sum++;}
			}else{
				ps[hi_ind]++;ps_sum++;
			}
		}
		
		cout << "Case #" << t << ": " << res << endl;
	}
}