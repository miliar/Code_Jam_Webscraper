#include<iostream>
using namespace std;
main()
{ 					
	unsigned long T,N,K,len;
	unsigned long base=0,mx=0,nw,tmp;
	unsigned long max,min;
	unsigned long a[1002];
	cin>>T;
	for(unsigned long i=0;i<T;i++)
	{
		len=0;
		cin>>N;
		cin>>K;
		a[0]=0;
		a[1]=N+1;
		len=len+2;
		for(unsigned long j=0;j<K;j++)
		{
			base=0;
			mx=0;
			for(unsigned long k=0;k<len-1;k++)
			{
				if(mx<(a[k+1]-a[k]))
				{
					mx=a[k+1]-a[k];
					base=k;
				}
			}
			len++;
			nw=mx/2;
			nw=nw+a[base];
			for(unsigned long k=base+1;k<len;k++)
			{
				tmp=a[k];
				a[k]=nw;
				nw=tmp;
			}
		}
		base=base+1;
		min=a[base]-a[base-1]-1;
		max=a[base+1]-a[base]-1;
		if(min>max)
		{
			unsigned long tmp;
			tmp=min;
			min=max;
			max=tmp;
		}
		cout<<"Case #"<<i+1<<": "<<max<<" "<<min<<endl;
	}
	return 0;
}

