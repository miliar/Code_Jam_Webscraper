#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("res1.out", "w", stdout);
	int T;
	cin>>T;
	string s;
	int res;
	int k;
	int ssize;
	bool ch;
	for(int t=0; t<T; t++)
	{
		s="";
		res=0;
		ch=false;

		cin>>s>>k;
		ssize=s.size();

		for(int i=0; i<ssize-k; i++)
		{
			if(s[i]=='-'){
				res++;
				for(int j=i; j<i+k; j++)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}

		for(int i=ssize-k; i<ssize-1; i++)
		{
			if(s[i]!=s[i+1])
			{
				ch=true;
				break;
			}
		}

		if(ch)
		{
			cout<<"Case #"<<t+1<<": IMPOSSIBLE\n";
		}
		else
		{
			if(s[ssize-1]=='-') res++;
			cout<<"Case #"<<t+1<<": "<<res<<endl;
		}

	}
	return 0;
}
