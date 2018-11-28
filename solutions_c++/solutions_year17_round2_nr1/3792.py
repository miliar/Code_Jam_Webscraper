#include<iostream>
using namespace std;
int main()
{
	freopen("uuuu.in","r",stdin);
	freopen("outuuu.txt","w",stdout);
	
	int i,t,n;
	double d;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	  cin>>d>>n;
	  double  k[n];
	  double max=0.0d,x=0.0d,l;
	  double s[n];
	  for(int j=0;j<n;j++)
	  {  cin>>k[j]>>s[j];
	  }
	  for(int p=0;p<n;p++)
	  {
	  	x=(d-k[p])/s[p];
	  	if(max<x)
	  	{
	  		max=x;
	  	}
	  }
	  //cout<<max;
	 // float g=d+1.000000f-1.000000;
	  //cout<<g<<" ";
	  l=(d/max);
	  printf("Case #%d",i);
	  printf(": %f",l);
	  printf("\n");
	  //cout<<"Case #"<<i<<": "<<l<<endl;
	  	
	}
	return 0;
}
