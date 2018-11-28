#include<bits/stdc++.h>

using namespace std;

int main()
{
	string s;
	int t, t1, k, n, i, j, x, y, count;
	cin>>t;
	for(t1=1;t1<=t;t1++)
	{
		cin>>s>>k;
		count = 0;
		n = s.length();
		int arr[n];
		memset(arr,0,sizeof arr);
		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				arr[i]=1;
			}
		}
		i = 0;
		while(i<=(n-k))
		{
			while(i<n && arr[i]==0)
			{
				i++;
			}
			if(i>(n-k))
			{
				break;
			}
			for(j=0;j<k;j++)
			{
			arr[j+i]=1-arr[j+i];
			}
			count++;
		}
		while(i<n)
		{
			if(arr[i]==1)
			{
				count=-1;
			}
			i++;
		}
		if(count==-1)
		{
			cout<<"Case #"<<t1<<": IMPOSSIBLE\n";
		}
		else
		{
			cout<<"Case #"<<t1<<": "<<count<<endl;
		}
	}
	return 0;
}
