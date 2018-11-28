#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin>>T;
	int z=1;
	while(T--)
	{
		double D;
		int N;
		cin>>D>>N;
		double K[N];
		double S[N];
		for(int i=0; i<N; i++)
			cin>>K[i]>>S[i];
		cout<<"Case #"<<z++<<": ";
		if(N==1)
		{
			double ans=(D-K[0])/S[0];
			cout<<fixed<<setprecision(6)<<D/ans<<endl;
		}
		else if(N==2)
		{
			double ans;
			if(K[1]<K[0])
			{
				swap(K[0],K[1]);
				swap(S[0],S[1]);
			}
			if(S[0]<=S[1])
			ans=D/((D-K[0])/S[0]);
			else
			{
				double t=(K[1]-K[0])/(S[0]-S[1]);
				double x=K[0]+S[0]*t;
				//cout<<K[0]<<" "<<S[1]<<endl;
				if(x<D)
				ans=D/(t+(D-x)/S[1]);
				else
				ans=D/((D-K[0])/S[0]);
			}
			cout<<fixed<<setprecision(6)<<ans<<endl;
		}
	}
	return 0;
}