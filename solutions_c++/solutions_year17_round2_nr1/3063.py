#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	double d[t],n[t];
	
	for(int i=0;i<t;i++)
	{
		int d,n;
		cin>>d>>n;
		double k[n],s[n];
		for(int j=0;j<n;j++)
		{
			cin>>k[j]>>s[j];
		}
		double max=0;
		double t;
		for(int j=0;j<n;j++)
		      {
		      		t=(float)(d-k[j])/s[j];
		      		if(max<t)
		      			{
		      				max=t;
		      				
		   //   				pos=i;
		      			}
		      }
		      
		printf("Case #%d: %.6f\n",i+1,(d/max));	
		
	}
	
	return 0;}
		
		
