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
		char a[1005];
		cin>>a;
		int k,s=strlen(a),i,j,flips=0;
		cin>>k;
		for(i=0;i<s-k;i++)
		{
			if(a[i]=='+')
				continue;
			if(i+k<=s)
			{
				for(j=i;j<i+k;j++)
					if(a[j]=='+')
						a[j]='-';
					else
						a[j]='+';
				flips++;
			}
		}
		for(j=i;j<s;j++)
			if(a[j]=='+')
				continue;
			else
				break;
		if(j<s)
		{
			for(j=i;j<s;j++)
				if(a[j]=='-')
					continue;
				else
					break;
				if(j<s)
					cout<<"Case #"<<x-t<<": IMPOSSIBLE"<<endl;
				else
					cout<<"Case #"<<x-t<<": "<<++flips<<endl;
		}
		else
			cout<<"Case #"<<x-t<<": "<<flips<<endl;
	}
	return 0;
}