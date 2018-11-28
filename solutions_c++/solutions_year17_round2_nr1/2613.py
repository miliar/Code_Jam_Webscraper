#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <limits.h>
#include <string.h>
#include <stack>
#include <iomanip>
using namespace std;

#define ll long long
#define ld long double

int t;
ll dest,n;
long double maxi,temp;
ll s,speed;
long double ans;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	std::ios_base::sync_with_stdio(false);
	cin.tie(0);
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		scanf("%lld %lld",&dest,&n);
		maxi = -1;
		for(int i=0;i<n;i++){
			scanf("%lld %lld",&s,&speed);
			temp = ((ld)dest-(ld)s)/(ld)speed;
			maxi = max(maxi,temp);	
		}
		ans = dest/maxi;
		printf("%.6Lf\n",ans);
	}
	return 0;
}