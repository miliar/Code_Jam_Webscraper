#include <bits/stdc++.h>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI; typedef pair<int,int> pii;
const ll mod = 1e9+7;
const double PI = acos(-1);

void fnc00(int qt){
	
	int N, K;
	cin >>N >>K; 
	
	vector<VI> rh(N, VI(2));
	rep(i,N) cin >>rh[i][0] >>rh[i][1];
	
	
	sort(rh.rbegin(), rh.rend(),[](VI l, VI r){
		return (double)l[0]*l[1] < (double)r[0]*r[1];
	});
	//for(auto x :rh) printf("%d:%d, ",x[0],x[1]); puts("");
	int mxr=0, mri=-1;
	rep(i,N) if(rh[i][0] > mxr){mxr=rh[i][0]; mri=i;}
	
	vector<VI> nv;
	rep(i,K) nv.push_back(rh[i]);
	double ans =0;
	int cmx=0;
	for(auto x :nv){
		//double en = PI *  x[0] * x[0];
		double sj = 2*PI * x[0] * x[1];
		ans +=  sj;
		cmx=max(cmx, x[0]);
	}
	ans += PI *  cmx * cmx;
	
	nv.clear();
	nv.push_back(rh[mri]);
	rep(i,K-1) if(i !=mri ) nv.push_back(rh[i]);
	double sm =0;
	cmx=0;
	for(auto x :nv){
		//double en = PI *  x[0] * x[0];
		double sj = 2*PI * x[0] * x[1];
		sm +=  sj;
		cmx=max(cmx, x[0]);
	}
	sm += PI *  cmx * cmx;
	
	//cout <<ans <<"  "<<sm <<"<--sm\n";
	ans = max(ans, sm);
	
	
	
	printf("Case #%d: %.12f\n", qt+1, ans);
}


int main()
{
	//cin.tie(0); ios_base::sync_with_stdio(false);
	int t; cin >> t;
	rep(i, t) fnc00(i);
	
	
	return 0;
}