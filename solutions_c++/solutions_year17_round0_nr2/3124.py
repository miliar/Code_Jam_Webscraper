#include<iostream>
using namespace std;

int main()
{
	int t,j;
	cin>>t;
	for(j = 1;j<=t;j++)
	{
		string s;
		cin>>s;
		int ln = s.length(),k;
		int arr[20],i = 0;
		for(i = 0;i<ln;i++)
		{
			arr[i+1] = s[i]-'0';
		}
		bool done = false;
		for(i = 2;i<=ln;i++)
		{
			if(arr[i]<arr[i-1])
			{
				if(done == true)
				{
					arr[i] = 9;
				}
				else
				{
					arr[i] = 9;
					bool flag = false;
					for(k = i-1;k>1;k--)
					{
						if(arr[k] == arr[k-1])
						{
							arr[k] = 9;
						}
						else
						{
							arr[k]--;
							flag = true;
							break;
						}
					}
					if(flag == false)
					{
						arr[1]--;
					}
					done = true;
				}
			}
		}
		i = 1;
		while(arr[i] == 0 && i<=ln)
		{
			i++;
		}
		
		cout<<"Case #"<<j<<": ";
		if(i == ln+1)
		{
			cout<<"0\n";
		}
		else
		{
			for(;i<=ln;i++)
			{
				cout<<arr[i];
			}
			cout<<"\n";
		}
		
	}
}
