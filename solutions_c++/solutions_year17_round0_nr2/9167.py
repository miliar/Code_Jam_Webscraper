#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long long int n,j,temp;
		cin>>n;
		if(n<10)
		{
			cout<<"Case #"<<i<<": "<<n<<endl;
		}
		else{
		
		for(j=n;j>=10;j--)
		{
			vector<int> a;
			temp=j;
			while(temp>0)
			{
				a.push_back(temp%10);
				temp/=10;
			}
			int flag=1;
			for(int k=0;k<a.size()-1;k++)
			{
				if(a[k]<a[k+1])
				{
					flag=0;
					break;
				}
			}
			if(flag)
			break;
		}
		cout<<"Case #"<<i<<": "<<j<<endl;
		}
	}
	return 0;
}
