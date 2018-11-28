#include<bits/stdc++.h>

using namespace std;

int main(){

	int t;
	cin>>t;

	int n;
	double dist;
	double tim;
	double temp;
	double speed;
	for(int i=0;i<t;i++){
		cin>>dist;
		cin>>n;

		tim = 0;
		vector<double> positions(n);
		vector<int> speeds(n);

		for(int j=0;j<n;j++){
			cin>>positions[j]>>speeds[j];
			temp = 1.0*(dist-positions[j])/speeds[j];
			if(tim<temp){
				tim = temp;
			}
		}

		speed = dist/tim;
		cout<<fixed;
		cout<<"Case #"<<i+1<<": "<<setprecision(6)<<speed<<endl;


	}
}