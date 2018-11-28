#include<iostream>
#include<algorithm>
#include<vector>
#include <fstream>
using namespace std;

int check(long long int n)
{
	int kl=1, cnt=0;
	while(n>0 && kl!=0)
	{
		if(n%10==1 || n%10==0)
		{
			n=n/10;
			cnt++;
			kl=cnt;
		}	
		else
		{
			kl=0;
		}
	}	
	return kl;
	
}

int chose(long long int n)
{
	long long int fl=1, r1, r2, n1=n, n2;
	while(n1>0 && n2>0 && fl==1)
	{	fl=0;
		r1=n1%10;
		n2=n1/10;
		r2=n2%10;
		n1=n1/10;
		//cout << r1 << " " <<  r2 << " " << n1 << endl; 
		if(r1>=r2)
		{
			fl=1;
		}
		else
		{
			fl=0;
		}
	}
//	cout << "f" << fl << endl;
	return fl;
}
int main()
{
	int t;
	cin >> t;
	int k=1;
	while(t--)
	{
		long long int n;
		cin >> n;
		if(n<=9)
		{
			cout << "Case #" << k++ << ": "  << n << endl;
		}
		else
		{
			int f=0;
			while(f==0)
			{	//cout << n-1 << endl;
				int p, ck;
				ck=check(n);
				//cout << ck << " " << n <<  endl;
				if(ck==0)
				{
				p=chose(n);
				if(p==1)
				{	f=1;
					cout << "Case #" << k++ << ": "  << n << endl;
				}
				else
				{	
					n--;
				}
				}
				else
				{	long long int sm=0;
					for(int i=0;i<ck-1;i++)
					{
						sm=sm*10+9;
					}
					cout << "Case #" << k++ << ": "  << sm << endl;
					f=1;
				}
				
			}
		}
	}
	
	return 0;
}
