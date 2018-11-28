#include<bits/stdc++.h>
using namespace std;
const int maxn=1010;
const double pi=acos(-1);
struct cake{
	double r,h;
	double areah()const{
		return 2*pi*r*h;
	}
	bool operator<(cake oth)const{
		return areah()<oth.areah();
	}
}c[maxn];
int n,k;
void solve(){
	cin>>n>>k;
	for(int i=1;i<=n;i++)
		cin>>c[i].r>>c[i].h;
	sort(c+1,c+1+n);
	reverse(c+1,c+1+n);
	double ans=0;
	for(int i=1;i<=n;i++){
		double res=pi*c[i].r*c[i].r+c[i].areah();
		if(i<=k){
			for(int j=1;j<=k;j++)if(i!=j){
				res+=c[j].areah();
			}
		}else{
			for(int j=1;j<k;j++){
				res+=c[j].areah();
			}
		}
		ans=max(ans,res);
	}
	printf("%.10f\n",ans);
}
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
