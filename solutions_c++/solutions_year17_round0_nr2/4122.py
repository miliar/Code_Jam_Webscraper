#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;cin >> t;
	for(int tt=1;tt<=t;tt++)
	{
		long long int n,n1;cin >> n;n1=n;		
		vector<int> num;
		while(n1>0)
		{
			num.push_back(n1%10);
			n1=(n1-(n1%10))/10;
		}
		for(int i=0;i<num.size()-1;i++)
		{
			if(num[i+1]>num[i])
			{
				num[i+1]=(num[i+1]+9)%10;
				for(int j=i;j>=0;j--)
				num[j]=9;
			}
		}
		int f=0;
		cout << "Case #" << tt << ": ";
		for(int i=num.size()-1;i>=0;i--)
		{
			if(num[i]!=0)f=1;
			if(f)
			{
				cout << num[i];
			}
		}
		cout << endl;
	}
}