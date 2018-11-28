#include <iostream>
#include <string>
#include <vector>
using namespace std;

void removeZero(string &n)
{
	bool flag = true;
	while(flag)
	{
		flag = false;
		for(int j=n.length()-1;j>0;j--)
		{
			if(n[j]<n[j-1])
			{
				flag = true;
				for(int k=j;k<n.length();k++){n[k] = '9';}
				for(int k=j-1;k>=0;k--)
				{
					if(n[k]=='1')
					{
						if(k!=0){n[k] = '9';}
						else
						{
							for(int l=0;l<n.length()-1;l++)
							{
								n[l] = n[l+1];
							}
							n.resize(n.length()-1);
						}
					}
					else
					{
						n[k]-=1;
						break;
					}
				}
				if(flag){break;}
			}
		}	
	}
}

int main()
{
	int t;
	string n;
	bool flag;
	cin>>t;
	for(int i=0; i<t; i++)
	{
		cin>>n;
		if(n=="0"){cout<<0<<endl;}
		else
		{
			flag = false;
			removeZero(n);
			while(flag)
			{
				flag = false;
				for(int i=n.length()-1;i>0;i--)
				{
					if(n[i]<n[i-1])
					{
						n[i] = '9';
						n[i-1]-=1;
						removeZero(n);
						flag = true;
					}
				}
				cout<<n<<endl;
			}
		}
		cout<<"Case #"<<i+1<<": "<<n<<endl;
	}
}