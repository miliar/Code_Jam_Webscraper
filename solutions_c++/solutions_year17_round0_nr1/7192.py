#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int var=1;var<=t;var++)
	{
		char arr[5000];
		cin>>arr;
		int k;
		int n = strlen(arr);
		cin>>k;
		int ans=0;
		for(int i=0;i<(n-k+1);i++)
		{
			if(arr[i]=='-')
			{
				ans++;
				for(int j=i; j<(i+k); j++)
				{
					if(arr[j]=='-')
						arr[j]='+';
					else
						arr[j]='-';
				}
			}
		}
		bool flag = true;
		for(int l=0;l<n;l++)
		{
			if(arr[l]=='-')
			{
				flag=false;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<var<<": "<<ans<<endl;
		else
			cout<<"Case #"<<var<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
