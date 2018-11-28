#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

bool check (long long int num)
{
	string s = to_string(num);
	long long int len = s.length();int flag;

	for(long long int i=0; i<len-1; i++)
	{	flag=0;
		for(long long int j=i+1; j<len; j++)
		{
			if(s[i] > s[j])
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
		{
			return false;
		}
	}
	return true;
}
int main()
{
	bool ans;
	long long int T,n,*anss;

	cin>>T;
	anss = new long long int[T];
	for(long long int f=0; f<T; f++)
	{

	cin>>n;

	while(n>0)
	{
		ans = check(n);
		if(ans)
			break;
		else
			n--;
	}
	anss[f] = n;
	}
	for(long long int f=0; f<T; f++)
	{
		cout<<"Case #"<<(f+1)<<": ";
		cout<<anss[f]<<endl;

	}
}


