#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-small-attempt1.in","rt",stdin);
  	freopen("A-small-attempt1-out.txt","wt",stdout);
	long long i,j,n;
	double t,k,d,l,time,t1,t2,p,a,s;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>d>>n;
		double x[n],y[n];
		for(j=0;j<n;j++)
		{
			cin>>x[j]>>y[j];
		}
		cout<<"Case #"<<i+1<<": ";
		if(n==1)
		{
			time=(d-x[0])/y[0];
		}
		else
		{
			t1=t2=0;
			if(x[1]>x[0])
			{
				a=x[1];
				x[1]=x[0];
				x[0]=a;
				a=y[1];
				y[1]=y[0];
				y[0]=a;
			}
			time=(d-x[0])/y[0];
			s=-1;
			p=(x[0]-x[1])/(y[1]-y[0]);
			if(p<=0||(x[1]+p*y[1]>=d))
			{
				t1=(d-x[1])/y[1];
			}
			else
			{
				if(y[0]<y[1])
					s=y[0];
				else
					s=y[1];
				t1=p;
				t2=(d-x[1]-p*y[1])/s;
			}
			if(t1+t2>time)	
				time=t1+t2;
		}
		printf("%.6lf\n",d/time);
	}
	return 0;
}


