#include<bits/stdc++.h>
using namespace std;

long long convert(string str,int l)
{
	long long j=1;
	long long sum = 0;
	for(int i=l-1;i>=0;i--)
	{
		int x = str[i]-'0';
		sum+=x*j;
		j*=10;
	}
	return sum;
}

int check(string str,int l)
{
	for(int i=l-1;i>0;i--)
	{
		int a = str[i]-'0';
		int b = str[i-1]-'0';
		if(a<b)
		return 0;
	}
	return 1;
}

string fun(string str,int l)
{
	for(int i=l-1;i>=0;i--)
	{
		if(check(str,l))
		return str;
		if(str[i]=='9')
		continue;
		str[i]='9';
		int j=i-1;
		while(j>=0)
		{
			int a = str[j]-'0';
			if(a==0)
			{
				str[j]='9';
				i=j;
				j--;
			}
			else
			break;
		}
		int a = str[j]-'0';
		a--;
		str[j]=a+'0';
	}
	return "cms";
}


int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int t;
	cin>>t;
	int j=1;
	while(t--)
	{
		string str;
		cin>>str;
		int l = str.length();
		if(l==1)
		cout<<"Case #"<<j<<": "<<convert(str,l)<<endl;
		else
		{
			if(check(str,l))
			cout<<"Case #"<<j<<": "<<convert(str,l)<<endl;
			else
			{
				cout<<"Case #"<<j<<": "<<convert((fun(str,l)),l)<<endl;
			}
		}
		j++;
	}
	return 0;
}
