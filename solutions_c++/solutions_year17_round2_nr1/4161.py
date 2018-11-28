/*
 * CruiseControl.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: Mostafa
 */

#include<bits/stdc++.h>

using namespace std; 


int main () {
#ifndef ONLINE_JUDGE
//	freopen("input.txt", "rt", stdin);
	freopen("A-small-attempt2.in", "rt", stdin);
	freopen("output.txt", "w", stdout);

#endif
	int t,tc=1;
	scanf("%d",&t);
	while(t--) {
		double k[1001],s[1001];
		printf("Case #%d: ",tc++);
		double d,n;
		scanf("%lf%lf",&d,&n);

		for(int i=0;i<n;i++) {
			scanf("%lf%lf",&k[i],&s[i]);
		}
		double res=0;
		if(n>1 && k[0]<k[1] && s[0]>s[1]) {
			swap(k[0],k[1]);
			swap(s[0],s[1]);
		}
		if(n>1 && k[0]>k[1] && s[0]<s[1]) {
			double h=(k[0]-k[1])/(s[1]-s[0]);
			double meeting=(h*s[0])+k[0];
			if(meeting<=d) {
				res=h+((d-meeting)/s[0]);
				res=d/res;
			}
			else {
				double r1=d-k[0],r2=d-k[1];
				r1/=s[0],r2/=s[1];
				res=d/max(r1,r2);
			}
			printf("%lf\n",res);

		}
		else {
			if(n>1 && k[0]>k[1]) {
				swap(k[0],k[1]);
				swap(s[0],s[1]);
			}
			res=d/((d-k[0])/s[0]);
			printf("%lf\n",res);
		}
	}
	return 0;
}
