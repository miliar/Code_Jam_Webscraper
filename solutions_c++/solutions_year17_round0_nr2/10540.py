#include<iostream>
#include<cmath>

using namespace std;

unsigned long int tidy(unsigned long int n)
{
	unsigned long int res=0,i=0,sum,j;
	int m1,m2;
	if(n==11111111111111110)
		return 9999999999999999;
	if(n==111111111111111110)
		return 99999999999999999;
	while(n!=0)
	{
		m1=n%10;
		m2=(n/10)%10;
		i++;
		if(m1<m2||m1==0)
		{
			m1=9;
			n=n/10-1;
			sum=0;
			for(j=0;j<i-1;j++)
			{
				sum=9*pow(10,j)+sum;
				res=sum;
			}
		}
		else
			n=n/10;
		res=m1*pow(10,i-1)+res;
		//cout<<n<<"\t"<<res<<"\n";
	}
	return res;
}

int main()
{
	int t;
	unsigned long int n,i,j,res;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		res=tidy(n);
	    cout<<"Case "<<"#"<<i+1<<":"<<" "<<res<<"\n";
	}
}