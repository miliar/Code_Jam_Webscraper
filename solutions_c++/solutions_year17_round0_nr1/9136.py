#include<bits/stdc++.h>
using namespace std;

int main()
{
int t;
	cin>>t;
	for(int in=0;in<t;in++)
	{
		string str;
		cin>>str;

		int n=str.size(),k,m=0;
		cin>>k;

		queue<int> q;
		int x,flg=0;
		
		for(int i=0;i<n;i++)
		{
			if(!q.empty()&&q.front()<=i-k)
				q.pop();

			x=str[i]=='+'?1:0;

			if((x^(q.size()%2==0))==1)
			{
				if(i>n-k)
				{
					flg=1;
					break;
				}
				m++;
				q.push(i);
			}
		}
		
		cout<<"Case #"<<in+1<<": ";
		if(flg)
		cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<m<<endl;
	}
return 0;
}