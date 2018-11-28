#include<bits/stdc++.h>
using namespace std;
void func(int arr[],int n)
{
	long long x=0;
	for(int i=0;i<n;i++)
	{
		x*=10;
		x+=arr[i];
	}
	cout<<x<<"\n";
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("op.txt","w",stdout);
	int t;cin>>t;
	while(t--)
	{
	    cout<<"Case #"<<100-t<<": ";
		string s;cin>>s;
		int arr[s.length()];
		for(int i=s.length()-1;i>=0;i--)
			arr[i]=s[i]-'0';
		int f=0;
		for(int i=0;i<s.length()-1;i++)
		{
			if(arr[i]>arr[i+1])
			{
				f=1;
				break;
			}
		}
		if(f==0)
			func(arr,s.length());
		else
		{
			for(int i=1;i<s.length();i++)
			{
				int x=0;
				if(arr[i]<arr[i-1])
				{
					int j=i;
					while(arr[j]<arr[j-1]&&j>=1)
					{
					    if(arr[j]<arr[j-1])
					{
						arr[j-1]--;
						for(int k=j;k<s.length();k++)
							arr[k]=9;
						x=1;
					}
					j--;
				}
				}
				if(x==1)
					break;
			}
			func(arr,s.length());
		}
	}
	return 0;
}
