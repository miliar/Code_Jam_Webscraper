#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	
	int test;
	cin>>test;
	
	for(int j=1;j<=test;j++)
	{
		string str;
		cin>>str;
		int K, Ans;
		cin>>K;
		
		int len = str.size();
		Ans = 0;
		
		for(int i=0;i<len-K+1;i++)
		{
			if(str[i] == '-')
			{
				for(int j=i;j<i+K;j++)
				{
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				Ans++;
			}
		}
		
		int flag = 0;
		for(int i=0;i<len;i++)
		{
			if(str[i] == '-')
			{
				flag = 1;
				break;
			}
		}
		
		cout<<"Case #"<<j<<": ";
		if(flag)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<Ans<<endl;	
		}
	}
	return 0;
}
