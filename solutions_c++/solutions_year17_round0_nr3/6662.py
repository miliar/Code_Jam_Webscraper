#include<iostream>
using namespace std;
main()
{ 					
	int T,N,K,len;
	int base=0,mx=0,nw,tmp;
	int max,min;
	int a[1002];
	cin>>T;
	for(int i=0;i<T;i++)
	{
		len=0;
		cin>>N;
		cin>>K;
		a[0]=0;
		a[1]=N+1;
		len=len+2;
		for(int j=0;j<K;j++)
		{
			base=0;
			mx=0;
			for(int k=0;k<len-1;k++)
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
			for(int k=base+1;k<len;k++)
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
			int tmp;
			tmp=min;
			min=max;
			max=tmp;
		}
		cout<<"Case #"<<i+1<<": "<<max<<" "<<min<<endl;
	}
	return 0;
}

