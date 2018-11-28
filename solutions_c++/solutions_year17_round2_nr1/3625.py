#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		double d;
		long long int n;
		cin>>d>>n;
	    double arr[n];
	    for(long long int i=0;i<n;i++)
	    {
	    	double k,s;
	    	cin>>k>>s;
	    	float x=(double)((d-k)/s);
	    	arr[i]=x;
		}
		double max=0;
		for(int i=0;i<n;i++)
		{
			if(arr[i]>max)
			max=arr[i];
		}
		printf("Case #%d: %.6lf\n",t,d/max);
	}
	fclose(stdout);
}