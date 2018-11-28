#include<bits/stdc++.h>

using namespace std;

long long count_digit(int x)
{
	int count=0;
	while(x)
	{
		x=x/10;
		count++;
	}
	return count;
}

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		long long N;
		cin>>N;
		long long digit=count_digit(N);
		long long a=N,b=0,c=0;
		if(digit==1)
		{
			a=N,b=0,c=0;
		}
		long long prev=0;
		while( digit>=2 )
		{
			long long v=pow(10,digit);
			long long x=(N%v)/(v/10);
			
			digit=digit-1;
			
			v=pow(10,digit);

			long long y;
			if(v==10)
			{
				y=(N%v);
			}
			else
				y=(N%v)/(v/10);
				
			if(x>y)
			{
				digit++;
				if(prev==x)
				{
					v=pow(10,digit-1);
					N=N-N%v;
					N=N-v;
					N=N+(v-1);
					digit++;
					
					v=pow(10,digit);
					prev=(N%v)/(v/10);
					a=N;
					
				}	
				else
				{
					a=(N/(pow(10,digit)));
					a=a*(pow(10,digit));

					b=(x-1)*(pow(10,digit-1));
			
					c=(pow(10,digit-1))-1;
				
					break;
				}	
				
			}
			else
				prev=x;
			
		}
		cout<<"Case #"<<t<<": "<<(a+b+c)<<endl;
		
	}
	return 0;
}
