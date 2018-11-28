//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
pair<double, double> p[1004];
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		double d;
		int n;
		scanf("%lf",&d);
		scanf("%d",&n);
		int i;
		double mx=0.0;
		for(i=0;i<n;i++){
			scanf("%lf%lf",&p[i].F, &p[i].S);
			double h=(d-p[i].F)/p[i].S;
			mx=max(mx,h);
		}
		printf("Case #%d: %.9lf\n",hh,d/mx);
	}
    return 0;
}
