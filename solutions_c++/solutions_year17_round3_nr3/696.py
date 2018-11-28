
#include<stdio.h>
#include<algorithm>

using namespace std;

double solve(int n,int k,double u,double *p){
    sort(p,p+n);
    double m = p[0];
    int s = 1;
    while ( 1 ){
	while( s<n && p[s] == m){
	    s++;
	}
	if(s==n){
	    m = m + u/s;
	    double end = 1.0;
	    for(int i=0;i<s;i++){
		end *= m;
	    }
	    return end;
	}
	if((p[s] - m) * s > u){
	    m = m + u/s;
	    double end = 1.0;
	    for(int i=0;i<s;i++){
		end *= m;
	    }
	    for(int i=s;i<n;i++){
		end *= p[i];
	    }
	    return end;
	}
	else{
	    u -= s*(p[s]-m);
	    m = p[s];
	}
    }
    return -1;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
	int n,k;
	double u;
	double p[1000];
	scanf("%d%d",&n,&k);
	scanf("%lf",&u);
	for(int i=0;i<n;i++){
	    scanf("%lf",p+i);
	}
	printf("Case #%d: %lf\n",t,solve(n,k,u,p));
    }
    return 0;
}
