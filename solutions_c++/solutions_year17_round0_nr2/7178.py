#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int var=1;var<=t;var++)
	{
		char arr[100];
		cin>>arr;
		int n = strlen(arr);
		bool flag=false;
		while(!flag)
		{
			if(n==1)
				break;
			for(int i=0;i<n-1;i++)
			{
				if(arr[i+1]<arr[i])
				{
					arr[i]--;
					flag=false;
					for(int j=i+1;j<n;j++)
						arr[j]='9';
					// cout<<arr<<endl;
					break;
				}
				else
				{
					flag=true;
				}
			}

		}
		cout<<"Case #"<<var<<": ";
		int i=-1;
		while(arr[++i]=='0');
		for(;i<n;i++)
		{
			cout<<arr[i];
		}
		cout<<endl;
	}
	return 0;
}
