#include <cstdio>
#include <algorithm>
using namespace std;

int t,n,k;
double pie = 3.14159265358979323846264338;
struct Cake{
	double r,h,area;	
}cake1[1001],cake2[1001];

bool comp1(const Cake& A, const Cake& B){
	if(A.r == B.r) return A.h > B.h;
	return A.r > B.r;
}

bool comp2(const Cake& A, const Cake& B){
	if(A.area == B.area) return A.r > B.r;
	return A.area > B.area;
}

int main(){
	//freopen("test/A-large.in","r",stdin);
	scanf("%d",&t);
	
	FILE *f;
	f=fopen("a.txt","w");
	
	for(int test_case=1; test_case<=t; test_case++){			
		scanf("%d %d",&n,&k);				
		for(int i=0; i<n; i++){
			scanf("%lf %lf",&cake1[i].r,&cake1[i].h);	
			cake1[i].area = cake1[i].r*2.0*cake1[i].h;	
			cake2[i] = cake1[i];
		}			
				
		sort(cake1, cake1+n, comp1);
		sort(cake2, cake2+n, comp2);			
		
		double ans = 0.0, maxR = 0.0;
		for(int i=0; i<k; i++){			
			if(i<k-1) ans += cake2[i].area;
			maxR = max(cake2[i].r,maxR);		
		}										
		
		if(cake1[0].r > maxR && (cake1[0].r*cake1[0].r)-maxR*maxR+cake1[0].area > cake2[k-1].area){			
			ans += (cake1[0].area + cake1[0].r*cake1[0].r);			
		}else{
			ans += (cake2[k-1].area + maxR*maxR);
		}
				
		//printf("%lf\n",ans*pie);
		fprintf(f,"Case #%d: %lf\n",test_case,ans*pie);
	}
	fclose(f);
	
	return 0;
}
