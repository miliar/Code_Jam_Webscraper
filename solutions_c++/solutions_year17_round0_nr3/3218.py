#include<iostream>
#include<vector>
using namespace std;

#define ll long long int

ll expo(ll a,ll b)
{
	ll ans = 1;
	while(b)
	{
		if(b&1)
		{
			ans = ans*a;
		}
		a = a*a;
		b = b/2;
	}
	return ans;
}

int main()
{
	int t,ti,i;
	cin>>t;
	for(ti = 1;ti<=t;ti++)
	{
		ll n,k,val;
		cin>>n>>k;
		if(k == 1)
		{
			if(n&1)
			{
				cout<<"Case #"<<ti<<": "<<(n/2)<<" "<<(n/2)<<"\n";
			}
			else
			{
				cout<<"Case #"<<ti<<": "<<(n/2)<<" "<<(n/2)-1<<"\n";
			}
		}
		else
		{
			ll temp = 1,sum = 1;
			int j = 0;
			while(sum<k)
			{
				temp = temp*2;
				sum += temp;
				j++;
			}
			//cout<<j<<"\n";
			ll a = n,b = -1,an = 1,bn = -1,t1;
			for(i = 1;i<=j;i++)
			{
				if(b != -1)
				{
					if(a == b)
					{
						if(a&1)
						{
							a = a/2;
							an = 2*an+2*bn;
							b = -1;
							bn = -1;
						}
						else
						{
							a = a/2;
							b = a-1;
							t1 = an+bn;
							bn = t1;
							an = t1;
						}
					}
					else if(a%2 == 0)
					{
						a = a/2;
						b = a-1;
						bn = 2*bn+an;
					}
					else
					{
						a = a/2;
						b = a-1;
						an = 2*an+bn;
					}
				}
				else
				{
					if(a&1)
					{
						a = a/2;
						an = 2*an;
					}
					else
					{
						a = a/2;
						b = a-1;
						bn = an;
					}
				}
				if(b>a)
				{
					a = a+b;
					b = a-b;
					a = a-b;
					an = an+bn;
					bn = an-bn;
					an = an-bn;
				}
				//cout<<a<<":"<<an<<"; "<<b<<":"<<bn<<"\n";
			}
			val = k-(sum-expo(2,j));
			if(val<=an)
			{
				if(a&1)
				{
					cout<<"Case #"<<ti<<": "<<a/2<<" "<<a/2<<"\n";
				}
				else
				{
					cout<<"Case #"<<ti<<": "<<a/2<<" "<<a/2-1<<"\n";
				}
			}
			else
			{
				if(b&1)
				{
					cout<<"Case #"<<ti<<": "<<b/2<<" "<<b/2<<"\n";
				}
				else
				{
					cout<<"Case #"<<ti<<": "<<b/2<<" "<<b/2-1<<"\n";
				}
			}
		}
	}
}
