#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
const double eps=1e-9;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;++cs){
		int d,n;
		scanf("%d",&d);
		scanf("%d",&n);
		double dd=d,mxt=0;
		for(int i=0;i<n;++i){
			int k,s;
			scanf("%d",&k);
			scanf("%d",&s);
			double kd=k,sd=s;
			double tm=(dd-kd)/sd;
			if(tm>mxt){
				mxt=tm;
			}
		}
		double res=dd/mxt;
		printf("Case #%d: %.06lf\n",cs,res);
	}
	return 0;
}