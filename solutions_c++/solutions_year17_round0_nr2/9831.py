#include <bits/stdc++.h>
using namespace std;

#define f0(i,n) for(int i=0;i<n;i++)
typedef signed long long int sll;
typedef long long int ll;
 
int main()
{
	ofstream out("file1.out");
	ifstream in("B-small-attempt0.in");
	ll t,c1,c2,num1;in>>t;
	ll num;
	f0(j,t)
	{
		in>>num;
		num1=num;
		c1 = num1%10;
		num1/=10;
		for(;num>0;)
		{
			while(num1)
			{
			c2= num1%10;
			num1/=10;
			if(c2<=c1)
			 	swap(c1,c2);
				 else 
				 {
				     num1= --num;
				     c1=num1%10;
				     num1/=10;
					 break;				
				 }	
			}
		if(num1==0)
			{
				out<<"Case #"<<j+1<<": "<<num<<"\n";
				break;
			}	
		}
	}
}
