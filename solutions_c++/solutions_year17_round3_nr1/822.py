#include <bits/stdc++.h>

using namespace std;

#define ll long long

const double PI = 3.14159265358979323846264;
const int maxn = 1111;

struct cake{
	double r,h;

}cakes[maxn],tmpc[maxn];

bool cmph(const cake &a,const cake &b){
	return a.h*a.r>b.h*b.r;
}

int main(){
	 freopen("A-large.in","r",stdin);
	 freopen("A-large.out","w",stdout);

	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		cas++;

		int n,k;
		cin>>n>>k;

		for(int i=0;i<n;i++){
			cin>>cakes[i].r>>cakes[i].h;
		}

		memcpy(tmpc,cakes,sizeof(cakes));

		double ans = 0;
		for(int i=0;i<n;i++){
			memcpy(cakes,tmpc,sizeof(cakes));

			if(i!=0)swap(cakes[i],cakes[0]);
			if(k!=1)sort(cakes+1,cakes+n,cmph);
			double r = 0;

			double tmp = 0;
			for(int j=0;j<k;j++){
				tmp += cakes[j].h*2*PI*cakes[j].r;
				r = max(r,cakes[j].r);
			}

			tmp += PI*r*r;
			ans = max(ans,tmp);
		}

		printf("Case #%d: %.9f\n",cas,ans);
	}
	return 0;
}