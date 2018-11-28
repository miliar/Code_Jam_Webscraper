#include <bits/stdc++.h>
#define mx 1200

using namespace std;

int pos[mx][2];

int main(){
	int d,it = 1,n,t;
	scanf("%d",&t);
	while(it<=t){
		scanf("%d%d",&d,&n);
		double sp = 1e9;
		double time = 0;

		for (int i = 0; i < n; ++i)
		{
			
			scanf("%d%d",&pos[i][0],&pos[i][1]);
			double temp = (d-pos[i][0])/(pos[i][1]*1.0);
			// printf("%lf\n", temp);

			time = max(time,temp);
		}
		printf("Case #%d: %lf\n",it,d/time );

		it++;
	}
}