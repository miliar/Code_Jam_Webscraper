#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define PII pair<int,int>
#define maxn (1e5 + 7)

void mf(){
	//freopen("input.in","r",stdin);

	// freopen("Asmall.in","r",stdin);
	// freopen("Asmall.ou","w",stdout);

	freopen("Alarge.in","r",stdin);
	freopen("Alarge.ou","w",stdout);
}
struct cake{
	ll r,h;
};
const int mn = 1007;
const double pi = acos(-1);
cake a[mn];
int n,k;
bool decreaseCompare(const cake& left, const cake& right){
	return left.h*left.r > right.h*right.r;//false->swap
}
void solve(){
	cin>>n>>k;
	for(int i = 0; i < n;i++){
		cin>>a[i].r>>a[i].h;		
	}

	sort(a, a+n, decreaseCompare);
	double res = 0, rr = 0;
	for(int i = 0; i < n;i++){
		int c = 1;
		rr = pi*a[i].r*a[i].r;
		rr += 2*a[i].r*pi * a[i].h;
		for(int j = 0; j < n; j++){
			if(i!=j && c<k){
				rr += 2*a[j].r*pi*a[j].h;
				c++;
				if(c>=k) break;
			}
		}
		res = max(res, rr);
	}

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