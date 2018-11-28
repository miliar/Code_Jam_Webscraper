#include<bits/stdc++.h>

using namespace std;

int main()
{
	string s;
	int t, t1, n, i, j, x, y, count;
	long long k;
	cin>>t;
	for(t1=1;t1<=t;t1++)
	{
		cin>>s;
		count = 0;
		n = s.length();
		int arr[n];
		for(i=0;i<n;i++)
		{
			arr[i]=s[i]-'0';
		}
		j = 1;
		while(j<n)
		{
			while(j<n && arr[j]>=arr[j-1])
			{
				j++;
			}
			if(j==n)
			{
				break;
			}
			i = j-1;
			while(i>0 && arr[i]==arr[i-1])
			{
				i--;
			}
			arr[i]--;
			for(j=i+1;j<n;j++)
			{
				arr[j]=9;
			}
		}
		k = 0;
		for(i=0;i<n;i++)
		{
			k = (k*10)+arr[i];
		}
		cout<<"Case #"<<t1<<": "<<k<<endl;
	}
	return 0;
}
