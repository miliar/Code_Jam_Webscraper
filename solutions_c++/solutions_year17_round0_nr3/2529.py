#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
void f(const unsigned long long int &n,const unsigned long long int &k,const int &z);
void recurse(const unsigned long long &n,const unsigned long long int &k,const int &z)
{
	if (n%2==0)
		{
			if (k%2==0)
			{
				f((n/2),(k/2),z);
			}
			else
			{
				f(((n-1)/2),((k-1)/2),z);
			}
		}
		else
		{
			if(k%2==0)
			{
				f(((n-1)/2),((k+1)/2),z);
			}
			else
			{
				f(((n-1)/2),((k-1)/2),z);
			}
		}
}
void f(const unsigned long long int &n,const unsigned long long int &k,const int &z)
{
	if (k==1)
	{
		if (n%2==0)
		{
			cout<<"Case #"<<(z+1)<<": "<<(n/2)<<" "<<((n/2)-1)<<endl;
		}
		else
		{
			cout<<"Case #"<<(z+1)<<": "<<((n-1)/2)<<" "<<((n-1)/2)<<endl;
		}
	}
	else
	{
		recurse (n,k,z);
	}
}
int main()
{
	int t;
	cin>>t;
	for (int z = 0;z<t;z++)
	{
		unsigned long long int n;
		cin>>n;
		unsigned long long int k;
		cin>>k;
		f(n,k,z);
	}
}