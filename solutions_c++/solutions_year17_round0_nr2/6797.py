#include<bits/stdc++.h>

using namespace std;
int flag,flg;
void fun(string num,int ind)
{
	flg=0,flag=0;
	for (int i = num.length()-1; i >=1 ; i--)
	{
		if(num[i]=='0')
		{
			//cout<<"A"<<endl;
			num[i]='9';
			flag=1;
			continue;
		}
		if(flag)
		{
			//cout<<"B"<<endl;
			num[i]--;
			flag=0;
		}
		if(num[i]<num[i-1])
		{
			//cout<<"C"<<endl;
			num[i]='9';num[i-1]--;	
		}
	}
	if(flag)
		num[0]--;
	//cout<<num<<endl;
	for (int i = 0; i < num.length(); ++i)
	{
		if(num[i]=='9')
			flg=1;
		if(flg)
			num[i]='9';
	}
	if(num[0]=='0')
		num.erase(num.begin());
	cout<<"Case #"<<ind<<": "<<num<<endl;
}


int main()
{
	int tc;cin>>tc;
	for (int i = 1; i <= tc; ++i)
	{
		string x;cin>>x;
		fun(x,i);
	}
}