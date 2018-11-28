#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define PII pair<int,int>
const int mn = 57;
void mf(){
	// freopen("input.in","r",stdin);

	freopen("Csmall3.in","r",stdin);
	freopen("Csmall3.ou","w",stdout);

	//freopen("Clarge.in","r",stdin);
	//freopen("Clarge.ou","w",stdout);
}
int n,k;
double u;
double a[mn];
double const eps = 1e-7;
bool decreaseCompare(const int& left, const int& right){
	return left > right;//false->swap
}
void solve(){
	cin>>n>>k; cin>>u;
	for(int i = 0; i < n; i++) cin>>a[i];
	sort(a, a+n, decreaseCompare);	
	
	ll d = 0, c = 1e10, mid;
	double base = 1e10, ans = 0.0;
	while(d<=c){
		mid = d + (c - d)/2;
		double limit = mid*1.0/ base;
		double need = 0;
		for(int i = 0; i < k; i++){
			need += max(0.0, limit - a[i]);
		}
		if(need <=u || (abs(need - u)<=eps)){
			ans = limit;d = mid +1;
		}else{
			c = mid -1;
		}
	}
	double res = 1;
	for(int i = 0; i < k; i++) res*= max(a[i], ans);	
	cout<<setprecision(9)<<fixed;
	cout<<res<<endl;
}

int main(){
	ios_base::sync_with_stdio(false);
	#ifdef tuanh
		mf();
	#endif
	int ntest;
	cin>>ntest;
	for(int nt = 1; nt <= ntest; nt++){
		cout<<"Case #"<<nt<<": ";
		solve();	
	}
	
	return 0;
}