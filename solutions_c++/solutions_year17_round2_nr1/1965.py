#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	// your code goes here
	
	long t; //no. of trials
	long d,n; //destination, no. of horses;
	long k,s; //initial position, speed;
	long i,j;
	double max,val;;
	
	cin>>t;
	for(i=1;i<=t;i++)
	{	max=0;
		cin>>d>>n;
		for(j=1;j<=n;j++)
		{
			cin>>k>>s;
			val=d-k;
			val=val/s;
			if(val>max) max=val;
		}
		
		val=d/max;
		cout<<"Case #"<<fixed<<setprecision(6)<<i<<": "<<val<<endl;
		
	}
	return 0;
}
