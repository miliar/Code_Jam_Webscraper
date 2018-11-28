#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		string n;
		cin>>n;
		int len=n.length();
		for(int i=len-1;i>=0;i--)
		{
			if(i-1>=0 && n[i]<n[i-1])
			{
				n[i-1]--;
				for(int j=i;j<len;j++)
				{
					n[j]='9';
				}
			}
		}
		cout<<"Case #"<<z<<": ";
		int flg=0;
		for(int i=0;i<len;i++)
		{
			if(n[i]!='0' || flg==1)
			{
				flg=1;
				cout<<n[i];
			}
		}
		cout<<endl;
	}
	return 0;
}
