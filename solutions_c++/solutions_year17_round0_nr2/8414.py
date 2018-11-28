#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("now2.out","w",stdout);
	int T;
	cin>>T;
	for(int p=1;p<=T;p++)
	{
		string a;
		string ans;
		int test=0;
		cin>>a;
		ans[0]=a[0];
		for(int i=1;i<a.size();i++)
		{
			if(test)ans[i]='9';
			else ans[i]=a[i];
			int now=i;
			while(ans[now]<ans[now-1]&&now)
			{
					ans[now-1]--;
					ans[now]='9';
					test=1;
					now--;
			}
		}
		printf("Case #%d: ",p);
		if(ans[0]!='0')
		{
			for(int i=0;i<a.size();i++)cout<<ans[i];
		}
		else
		{
			for(int i=1;i<a.size();i++)cout<<ans[i];
		}
		printf("\n");
		//cout<<"sb"; 
	}
 } 
