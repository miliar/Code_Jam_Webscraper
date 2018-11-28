#include<iostream>
#include<math.h>
using namespace std;
int countDigits(int n)
{
	long long int i;
	int cnt;
	for(i=n;i>0;i=i/10)
	{
		cnt++;
	}
	return cnt;
}
int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		long long int num,ans;
		long long int digit;
		int numdig,prev,j,done=0,mark=-1;
		cin>>num;
		numdig = countDigits(num);
		j = numdig-1;
		ans = num;
		digit = (num/pow(10,j));
		digit = digit % 10;
		while(j>0 && !done) 
		{
			prev = digit;
			j--;
			digit = (num/pow(10,j));
			digit = digit % 10;
			if(digit==prev && mark==-1)
			{
				mark = j;
			}
			else if(digit<prev)
			{
				done=1;
			}
			else if(digit>prev)
			{
				if(mark!=-1)
				{
					mark=-1;
				}
			} 
		}
		if(done==1)
		{
			if(mark!=-1)
			{
				j=mark;
			}
			j++;
			ans = (num/pow(10,j));
			ans=ans*pow(10,j) - 1;	
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
