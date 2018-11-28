#include<bits/stdc++.h>
using namespace std;
#define FALSE 0
#define TRUE 1
#define ll long long
#define lne(i,j,k) for(i=j ; i<k ; i++)
#define le(i,j,k) for(i=j ; i<=k ; i++)

int main()
{
	ll t,i,ii,n;
	double a,b,d,tmax,temp;
	cin>>t;
	le(ii,1,t)
	{
		cout<<"Case #"<<ii<<": ";
		 cin>>d>>n;
		 cin>>a>>b;
		 tmax = (d-a)/b;
		 le(i,2,n)
		 {
		 	cin>>a>>b;
		 	temp = (d-a)/b;
		 	if(tmax<temp)
		 		tmax = temp;
		 }
		 temp = d/tmax;
		 printf("%f\n",temp);
	}
	return 0;
}
