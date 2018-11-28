//============================================================================
// Name        : gcj.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;
int k[1123];
int s[1123];

//bool ok(double speed){
//
//}

int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	int cn = 0;
	while(t--){
		cn++;
		int d,n;
		scanf("%d%d",&d,&n);

		for(int i=0;i<n;i++){
			scanf("%d%d",&k[i],&s[i]);
		}

		double time = 0;

		for(int i=0;i<n;i++){
			double dd = d-k[i];
			time = max(time , dd/s[i]);
		}

		double ans;
		if(time <= (1e-9)){
			ans = d;
		}else{
			ans = d/time;
		}
		printf("Case #%d: %.6lf\n",cn,ans);
	}
	return 0;
}
