#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#define PI acos(-1)
using namespace std;
int k,n;

struct Pie{

	double r;
	double h;
	double val;
}p[1001];
;
bool cmp(const Pie &a,const Pie &b){
	if(a.val==b.val)
	return a.r<b.r;

	return a.val>b.val;

}
int main()
{

	freopen("A-large.in","r",stdin);
	freopen("al","w",stdout);
	int T;
	cin>>T;


	for(int cs=1;cs<=T;cs++){

		cin>>n>>k;
		for(int i=0;i<n;i++){
			cin>>p[i].r>>p[i].h;
			p[i].val = 2.0*p[i].r*p[i].h;
		}
		sort(p,p+n,cmp);


		double ans =0,ret=0;
		for(int i=0;i<n;i++){

			int now =1,tmp=0;
			ans=p[i].r*p[i].r;
			ans+=p[i].val;

			while(now!=k && tmp!=n){

				if(tmp==i){
					tmp++;
				}else{
					if(p[tmp].r<=p[i].r){
						ans+=p[tmp].val;
						now++;
					}
					tmp++;

				}

			}
			if(ret<ans)ret= ans;

		}
		ret= ret*PI;
		printf("Case #%d: %.12lf\n",cs,ret);


	}


	return 0;
}
