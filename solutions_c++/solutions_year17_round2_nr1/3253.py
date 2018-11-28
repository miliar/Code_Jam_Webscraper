#include<iostream>
#include<iomanip>

using namespace std;

int main(){

	 freopen("A-large.in","r",stdin);
	 freopen("A-large.out","w",stdout);

	int t;

	cin>>t;

	int z = t;
	while(t--){
		int total_distance,n;

		cin>>total_distance>>n;

		int distances[n],speeds[n];

		for(int i=0;i<n;i++)
			cin>>distances[i]>>speeds[i];

		double max_time=0;

		for(int i=0;i<n;i++){
			 if(max_time < (double)(total_distance-distances[i])/speeds[i])
			 	max_time = (double)(total_distance-distances[i])/speeds[i];
		}

		double cruise_speed = (double)total_distance/max_time;

		cout<<"Case #"<<z-t<<": "<<fixed<<setprecision(6)<<cruise_speed<<endl;
	}
}

