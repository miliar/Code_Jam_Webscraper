#include <bits/stdc++.h>

using namespace std;

int main(){

	int t;
	scanf("%d",&t);
	for(int cases=1;cases<=t;cases++){
		int D,n;
		scanf("%d %d",&D,&n);
		vector<pair<int,int> > P(n);
		int distance,speed;
		for(int i=0;i<n;i++){
			scanf("%d %d",&distance,&speed);
			P[i] = make_pair(distance,speed);
		}
		sort(P.begin(),P.end());
		int index = 0;
		for(int i=0;i<n;i++){
			if(P[i].second < P[index].second){
				index = i;
			}
		}

		int curr_pos = P[index].first;
		int curr_speed = P[index].second;

		double t = (D-curr_pos)*1.0/(curr_speed*1.0);
		double s = D*1.0/t;


		for(int i = 0;i<n;i++){
			double temp_t = (D-P[i].first)*1.0/(P[i].second*1.0);
			double temp_s = D*1.0/temp_t;
			s = min(temp_s,s);
		}

		printf("Case #%d: %6f\n",cases,s);

	}

	return 0;
}
