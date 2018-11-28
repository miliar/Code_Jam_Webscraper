#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;

		int length = s.length();
		queue<int> q;
		bool even = true;
		int count=0;

		for(int j=0;j<length;j++)
		{
			if((s[j]=='+' && even) || (s[j]=='-' && !even))
			{
				if(!q.empty()){
					if(j==q.front())
					{
						q.pop();
						even = !even;
					}	
				}
			}
			else
			{
				if(j+k-1<length){
					q.push(j+k-1);
					count++;
					even = !even;
				}
				else
				{
					count=-1;
					break;
				}
				if(!q.empty()){
					if(j==q.front())
					{
						q.pop();
						even = !even;
					}	
				}
			}
		}
		if(count!=-1)
		{
			cout<<"Case #"<<i<<": "<<count<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
}