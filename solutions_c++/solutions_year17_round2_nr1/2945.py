#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main(int argc, char **argv)
{
	int t,n,i,d,k,p=1;
	double s,m,temp;
	cin>>t;
	while(p<=t)
	{
		cin>>d>>n;
		m=-1.0;
		for(i=0;i<n;i++)
		{
			cin>>k>>s;
			temp=(d-k)/s;
			if(m==-1.0 || m<temp)
				m=temp;
		}
		m=d/m;
		printf("Case #%d: %lf\n",p,m);
		p++;
	}
	return 0;
}
