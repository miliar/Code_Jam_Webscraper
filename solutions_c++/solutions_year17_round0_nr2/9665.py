#include<iostream>
#include <cstdio>

using namespace std;
main()
{
	int rem,i,j;
	unsigned long long int n,num,out;
	int a[100],test,T;
	freopen("B-large.in", "r", stdin);
	freopen("output_large.txt","w",stdout);
	cin>>T;
	//T=1;
	for(int test=0;test<T;test++){
	cin>>n;
	//n=3332;
	{
		
		num=n;
		i=0;
		while(num!=0){
			rem=num%10;
			num/=10;
			a[i++]=rem;
			//cout<<rem<<"\t";
		}
		int len=i;
		int b[len];
		int valid=1,k=0,nine=0;
		if(len!=1)
		--n;
		out=0;
		for(j=i-1;j>=0;j--)
		{
		  if(!nine){
			
			if(a[j]<=a[j-1])
			{
				b[k]=a[j];
				//cout<<b[k];
				//out=out*10+b[k];
				k++;
			}
			else{
				b[k]=a[j]-1;
				int p=k;
				while((p!=0&&b[p]<b[p-1]))
				{
					
					b[p]=9;
					--b[p-1];
					p--;
			 	}
				nine=1;
				//cout<<b[k];
				//out=out*10+b[k];
				k++;
			}
		  }
		   else
			{
				b[k]=9;
				//cout<<b[k];
				//out=out*10+b[k];
				k++;
			}
		}
		for(int q=0;q<len;q++)
		{
			out=out*10+b[q];
			//cout<<b[q]<<"\n";
		}
		
		cout<<"Case #"<<test+1<<": "<<out<<"\n";
		
	}
	}
return 1;
}
