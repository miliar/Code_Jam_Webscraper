#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	freopen("2017_A-large.in","r",stdin);
	freopen("2017_3.out","w",stdout);
	int T;
	cin>>T;
	for(int s=1;s<=T;s++)
	{
		long long  length,all;
		cin>>length>>all;
		double now=0;
		for(int i=0;i<all;i++)
		{
			int temp1;
			int temp2;
			cin>>temp1>>temp2;
			if(double(length-temp1)/double(temp2)>now)now=double(length-temp1)/double(temp2);
		}
		double ans=double(length)/now;
		printf("Case #%d: ",s);
		printf("%.8f\n",ans);
	}
} 
