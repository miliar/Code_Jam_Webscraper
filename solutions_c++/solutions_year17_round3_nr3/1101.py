#include <bits/stdc++.h>
#include <time.h>
using namespace std;
typedef unsigned long long ll;

void sleep(int seconds)
{   
    clock_t endwait;
    endwait = clock () + seconds * CLOCKS_PER_SEC / 1000 ;
    while (clock() < endwait) {}
}

int main (){
    int T;
    scanf("%d" ,&T);
    for (int t=1;t<=T;t++){
		int a,n;
		double u;
		
		scanf("%d %d %lf", &a, &n, &u);
		vector < double > c(a);
		for(int i=0;i<a;i++){
			scanf("%lf", &c[i]);
		}
		sort(c.begin(),c.end());
		
		if(n==1){
			//one core
			double res = c[0]+u;
			if(res>1)res=1;
			printf("Case #%d: %lf\n",t,res);
		}else{
			double akt = c[0];
			for(int i=1;i<=n;i++){
				if(n==i){
					double target = 1;
					if(akt==target)break;
					double needed = target - akt;
					double left = u - i*needed;
					if(left>=0){
						u = left;
						akt = target;
						for(int y=i-1;y>=0;y--)c[y]=akt;
					}else{
						akt = target + (left/i);
						u = 0.;
						for(int y=i-1;y>=0;y--)c[y]=akt;
						break;
					}
					break;
				}
				if(u==0)break;
				double target = c[i];
				if(akt==target)continue;
				double needed = target - akt;
				double left = u - i*needed;
				if(left>=0){
					u = left;
					akt = target;
					for(int y=i-1;y>=0;y--)c[y]=akt;
				}else{
					akt = target + (left/i);
					u = 0.;
					for(int y=i-1;y>=0;y--)c[y]=akt;
					break;
				}
				
				
			}
			double iloczyn = 1;
			for(int i=0;i<n;i++){
				iloczyn = iloczyn * c[i];				
			}	
			printf("Case #%d: %lf\n",t, iloczyn);
			
		}
    }
    return 0;
}
