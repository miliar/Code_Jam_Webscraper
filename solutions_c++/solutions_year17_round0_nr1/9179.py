#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	char a[1001];
	int n,g,size,t,h=0;
	bool b;
	cin>>t;
	while(t--)
	{
		h++;
		cin>>a>>g;
		b=0,n=0,size=g-1;
		for(int i=0;a[i+g-1]!='\0';i++)
		{
			size++;
			if(a[i]=='-')
			{
				n++;
				for(int i2=0;i2<g;i2++)
				{
					if(a[i+i2]=='-')a[i+i2]='+';
					else a[i+i2]='-';
				}
			}
		}
		for(int i=1;i<=g;i++)if(a[size-i]=='-'){b=1;break;}
		cout << "Case #"<<h<<": ";
		if(b)cout << "IMPOSSIBLE";
		else cout << n;
		cout << "\n";
	}
}
