#include<iostream>
using namespace std;

int main()
{
	int t,j,i,ln,p,count;
	cin>>t;
	for(j = 1;j<=t;j++)
	{
		string s;
		int k;
		cin>>s>>k;
		int ln = s.length();
		int arr[1007];
		for(i = 0;i<ln;i++)
		{
			arr[i+1] = s[i];
		}
		bool pos = true;
		count = 0;
		for(i = 1;i<=ln;i++)
		{
			if(arr[i] == '-')
			{
				if(i>ln-k+1)
				{
					pos = false;
					break;
				}
				for(p = i;p<=i+k-1;p++)
				{
					if(arr[p] == '-')
					{
						arr[p] = '+';
					}
					else
					{
						arr[p] = '-';
					}
				}
				count++;
			}
		}
		cout<<"Case #"<<j<<": ";
		if(pos == false)
		{
			cout<<"IMPOSSIBLE\n";
		}
		else
		{
			cout<<count<<"\n";
		}
	}
}
