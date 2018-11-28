#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{	
	int T,N,S,j,k;double D,K;
	double time[1000]={0};
	double speed;
	double maxtime;
	cin>>T;
	//cout<<"t:"<<T<<"\n";
	for (int i = 0; i < T; ++i)
	{
		cin>>D;
		//cout<<"D:"<<D<<"\n";	
		cin>>N;
		//cout<<"N:"<<N<<"\n";
		for ( k = 0; k < 1000; k++)
			{
				time[k]=0;
			}	
		for (j= 0; j < N; ++j)
		{
			cin>>K;
			cin>>S;
			//cout<<"K:"<<K<<"S:"<<S;
			time[j]=((D-K)/S);

		}
		maxtime=*max_element(time,time+1000);
		//cout<<i+1<<":"<<setprecision(6)<<fixed<<maxtime<<"\n";
		speed=D/maxtime;
		cout<<"Case #"<<i+1<<": "<<setprecision(6)<<fixed<<speed<<"\n";
	}
	return 0;
}