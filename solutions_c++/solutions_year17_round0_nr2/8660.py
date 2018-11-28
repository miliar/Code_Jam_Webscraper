
#include<iostream>
using namespace std;
main()
{
	unsigned long long T;
	unsigned long long N,n;
	unsigned long long a[25];
	cin>>T;
	for(unsigned long long i=0;i<T;i++)
	{
		unsigned long long j,k;
		cin>>N;
		mm:
		n=N;
		j=0;
		while(n>0)
		{
			a[j]=n%10;
			n=n/10;
			j++;
		}
		j=j-1;
		for(k=0;k<j;k++)
		{
			if(a[k+1]>a[k])
				break;
		}
		if(k==j)
		{
			cout<<"Case #"<<i+1<<": "<<N<<endl;
		}
		else
		{
			N=N-1;
			goto mm;
		}
	}
	return 0;
}
