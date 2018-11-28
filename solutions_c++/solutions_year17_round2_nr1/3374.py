#include <bits/stdc++.h>

using namespace std;

int main(){

	int t,D,N,distance,speed;;
	cin>>t;

	for(int p=1;p<=t;p++){

		cin>>D>>N;

		vector<pair<int,int> > P(N);

		for(int i=0;i<N;i++){
			cin>>distance>>speed;
			P[i] = make_pair(distance,speed);
		}

		int curr_pos = P[0].first;
		int curr_speed = P[0].second;

		double t = (D-curr_pos)*1.0/(curr_speed*1.0);
		double s = D*1.0/t;

		for(int i = 0;i<N;i++){
			double temp_t = (D-P[i].first)*1.0/(P[i].second*1.0);
			double temp_s = D*1.0/temp_t;
			s = min(temp_s,s);
		}

        printf("Case #%d: %6f\n",p,s);
		//cout<<"Case #"<<p<<":"<<" "<<s<<endl;

	}

	return 0;
}
