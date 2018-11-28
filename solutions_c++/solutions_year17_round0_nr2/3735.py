#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
 
bool tidy(ll n)
{
	ll temp=n;
	bool flag=false;
	int largest;
	while (temp>0)
	{
		int a=temp%10;
		temp=temp/10;
		if (flag==false)
		{
			flag=true;
			largest=a;
		}
		if (a>largest)
			return false;
		largest=a;
	}
	return true;
}
 
 
int main()
{
	int test;
	cin>>test;
	int g=1;
	while (test--)
	{
		ll n;
		cin>>n;
		cout<<"CASE #"<<g<<": ";
		g++;
		if (tidy(n))
		 cout<<n<<endl;
		else if (tidy(n-1))
			cout<<n-1<<endl;
		else
		{
			string str=to_string(n);
			int size=str.length();
			
			string str2="";
			for (int i=0;i<size;i++)
			{
				if (str[i]<=str[i+1])
				{
					str2[i]=str[i];
				}
				else
				{
					char temp=str[i]-1;
					str2[i]=temp;
					i++;
					while (i<size)
					{
						char temp=9+'0';
						str2[i]=temp;
						i++;
					}
				}
			}
			for (int i=size-1;i>0;i--)
			{
				if (str2[i]<str2[i-1])
				{
					char temp=9+'0';
					str2[i]=temp;
					char temp2=str2[i-1]-1;
					str2[i-1]=temp2;
				}
			}
			ll result=0;
			for (int i=0;i<size;i++)
			{
				result=result*10+(str2[i]-'0');
			}
 
			cout<<result<<endl;
		}
	}
	return 0;
}
