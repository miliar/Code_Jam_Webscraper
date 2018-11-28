#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<string>
#include<ctype.h>
using namespace std;
int main()
{
	int t;
	int i=1;
	unsigned long long n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		while(1)
		{
			int x=n;
			string s=to_string(x);
			if(is_sorted(s.begin(),s.end()))
			{
				cout<<"case #"<<i<<": "<<n<<endl;
				i=i+1;
				break;
			}
			else {
				n=n-1;
			}
		}
	}
}
