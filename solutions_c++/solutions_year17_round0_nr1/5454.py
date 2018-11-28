#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define rep(a,n) for(i=a;i<n;i++)
#define lld long long int
#define mod 1000000007
using namespace std;
int main()
{	int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{	string s; queue<int> q;
		int k,flip,count,x,y,flag=0,i;
		cin>>s;
		cin>>k;
		flip=0;
		count=0;
		for(i=0; i<s.length(); i++)
		{	if( (s[i]=='-' and flip%2==0) or (s[i]=='+' and flip%2==1))
			{  if((i+k-1)>=s.length())
				{flag=1;
				 break;}
			   q.push(i+k-1);
				count++;
				flip++;

			}
			if(i==q.front())
				{	flip--;
					q.pop();
				}
		}
		if(flag==1)
		cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<j<<": "<<count<<endl;
	}
}
