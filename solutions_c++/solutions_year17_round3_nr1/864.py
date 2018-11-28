#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

double solve(int n,int k,double *r,double *h){
    double a[1000];
    int used[1000];
    for(int i=0;i<n;i++){
	a[i] = r[i]*h[i] * 2 * M_PI;
	used[i] = 0;
    }
    double aa = 0;
    double cr = 0;
    for(int i=0;i<k;i++){
	int ci = 0;
	double cm = 0;
	double cura;
	for(int j=0;j<n;j++){
	    if(used[j]) continue;
	    cura = a[j];
	    if(r[j]> cr)
	       cura += (r[j]-cr) * (r[j]+cr) * M_PI;
	    if(cura > cm){
		ci = j;
		cm = cura;
	    }
	}
	aa +=cm;
	used[ci] = 1;
	if(r[ci] > cr)
	    cr = r[ci];
    }
    return aa;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
	int n,k;
	double r[1000],h[1000];
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++){
	    scanf("%lf%lf",r+i,h+i);
	}
	printf("Case #%d: %.10lf\n",t,solve(n,k,r,h));
    }
    return 0;
}
