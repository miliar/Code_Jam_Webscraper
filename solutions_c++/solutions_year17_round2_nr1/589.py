#include <iostream>
#include <iomanip>
using namespace std;

int onecase()
{
	int D, N;
	int KI[2000], SI[2000];
	long double ArriveTime[2000];
	long double latestArrive=-1;

	cin>>D>>N;
	for(int i=0;i<N;i++){
		cin>>KI[i]>>SI[i];
		ArriveTime[i]=(D-KI[i])*1.0/SI[i];
		if(ArriveTime[i]>latestArrive)latestArrive=ArriveTime[i];
	}

	long double speed=D*1.0/latestArrive;
	cout<<setprecision(9)<<speed<<endl;

	return 0;
}

int main(){
	//onecase();return 0;

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}