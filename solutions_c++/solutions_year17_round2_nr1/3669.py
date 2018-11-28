#include <bits/stdc++.h>
#include <limits.h>
using namespace std;
int main()
{
	int t,t1=0;
	cin>>t;
	while(t1<t)
	{
		int D,N;
		double tmax=-1;
		cin>>D>>N;
		int K[N],S[N];
		double T[N];
		for(int i=0;i<N;i++)
		{
			cin>>K[i]>>S[i];
			K[i]=D-K[i];
			T[i]=K[i]/S[i];
		}
		for(int i=0;i<N;i++)
		{
			if(T[i]>tmax)
			{
				tmax=T[i];
			}
		}
		double ans=D/tmax;
		//cout<<"Case #"<<t1+1<<": "<<ans<<endl;
		printf("Case #%d: %lf",t1+1,ans);
		t1++;
	}
	return 0;
}

