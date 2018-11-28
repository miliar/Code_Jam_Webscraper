#include <cstdio>
#include <algorithm>
const double pi=3.1415926535897932384626;

struct pc{
	double r,h,s;
};
bool sortsurfmode=false;

bool operator<(const pc& a,const pc& b){
	if(sortsurfmode){
		return a.s>b.s;
	}else{
		return a.r>b.r;
	}
}
pc pcs[1024];
pc tmp[1024];

double solve()
{
	int n,k;
	double ans=0;
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++){
		scanf("%lf%lf",&pcs[i].r,&pcs[i].h);
		pcs[i].s=pcs[i].r*2*pcs[i].h*pi;
	}
	sortsurfmode=false;
	std::sort(pcs,pcs+n);
	sortsurfmode=true;
	for(int i=0;i<=n-k;i++){
		double tot=pcs[i].r*pcs[i].r*pi;
		for(int j=i;j<n;j++){
			tmp[j-i]=pcs[j];
		}
		std::sort(tmp+1,tmp+(n-i));
		for(int j=0;j<k;j++){
			tot+=tmp[j].s;
		}
		if(ans<tot){
			ans=tot;
		}
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: %.10f\n",i+1,solve());
	}
	return 0;
}
