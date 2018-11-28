#include <iostream>
using namespace std;
int is_tidy(long long a)
{
	int p, q, flag = 1;
	p = a%10, q = 0;
	a = a/10;
	while(a)
	{
		q = a%10;
		if(q > p)
		{
			flag = 0;
			break;
		}
		a = a/10;
	
	    p = q;
	}
	return flag;
}
int digits(long long a)
{
	int c = 0;
	if(a == 0)
		return 1;
	while(a)
	{
		c++;
		a = a/10;
	}
	return c;
}
long long get_tidy(long long a)
{
	if(is_tidy(a))
		return a;
	int i;
	for(i = 1;;i++)
	{
		a = a/10;
		if(is_tidy(a))
			break;
	}
	while(i--)
		a*=10;
	a = a - 1;
	return get_tidy(a);
}
int main()
{
	long long a, ans;
	int t, i;
	cin>>t;
	for(i = 1; i <= t; i++)
	{
		cin>>a;
		ans = get_tidy(a);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}