#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B_large.txt","w",stdout);
	long long a,b,c,T,num;
	char s[100];
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>T;
	for(c=0;c<T;c++)
	{
		num=0;
		cin>>s;
		for(a=0;s[a+1];a++)
		{
			if(s[a]>s[a+1])
			{
				s[a]--;
				for(b=a+1;s[b];b++)
				{
					s[b]='9';
				}
				for(b=a-1;b>=0;b--)
				{
					if(s[b]>s[b+1])
					{
						s[b+1]='9';
						s[b]--;
					}
				}
			}
		}
		for(a=0;s[a];a++)num*=10,num+=s[a]-'0';
		cout<<"Case #"<<c+1<<": "<<num<<"\n";
	}
}
