#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	int t,x;
	cin>>t;
	x=t;
	while(t--)
	{
		char a[20];
		cin>>a;
		int j,s=strlen(a),i=0,flag=0;
		while(i<s-1)
		{
			if(flag && a[i]=='9')
				a[i+1]='9';
			else if(a[i]<=a[i+1])
			{
				if(a[i]==a[i+1])
				{
					j=i;
					while(a[j]==a[j+1] && j<s-1)
						j++;
					if(j==s-1)
						break;
					else
					{
						if(a[j]<a[j+1])
							i=j-1;
						else
							a[i]--,a[i+1]='9',flag++;	
						
					}
				}
				else
				{
					if(a[i+1]=='9')
						flag=0;
				}
			}
			else
			{
				a[i]--;
				a[i+1]='9';
				flag++;
			}
			i++;
		}
		cout<<"Case #"<<x-t<<": ";
		if(a[0]=='0')
			for(i=1;i<s;i++)
				cout<<a[i];
		else
			cout<<a;
		cout<<endl;
	}
	return 0;
}