#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

bool checkTidy(long long int n)
{
	int m, highest;
	highest = n%10;
	n/=10;

	while(n!=0)
	{
		m=n%10;
		if(m>highest) return false;
		else highest = m;
		n/=10;
	}
	return true;
}
long long tidy(long long int n)
{
	int k = log10(n) ;
	int prevm = 0;
//	cout<<" k : "<<k<<endl;
	for(int i=0;i<=k;i++)
	{
		
		long long m= n / pow(10, k-i);
//		cout<<"m: "<<m<<endl;
		
		if(!checkTidy(m))
		{
			m= n / pow(10, k-prevm);
			return (m - 1) * pow(10, k-prevm) + pow(10, k-prevm) - 1;
		}
		
		if(m%10 != (m/10)%10)
		{
			prevm=i;
		}	
	}
	return n;	
}
int main()
{
	ifstream mera_input;
	mera_input.open("B-small-attempt0.in");
	ofstream mera_output;
	mera_output.open("B-small-attempt-output.txt");
	int t;
	long long int n;
	mera_input>>t;
	int count = 0;
	while(t--)
	{
		count++;
		mera_input>>n;
		mera_output	<<"Case #"<<count<<": "<<tidy(n)<<endl;
	}
}
