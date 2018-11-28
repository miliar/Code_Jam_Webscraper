#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	
	char s[1000]="";
	int k=0;
	int t=0;
	int l=0;
	int flip=0;
	cin>>t;
	int x=t;
	while(t--)
	{
		flip=0;
		cin>>s;
		cin>>k;
		l=strlen(s);
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				if((l-i)<k)
				{
					flip=-1;
					cout<<"Case #"<<x-t<<": "<<"IMPOSSIBLE"<<endl;
					break;
				}
				else
				{
					s[i]='+';
					for(int j=1;j<k;j++)
					{
						if(s[i+j]=='-')
							s[i+j]='+';
						else 
							s[i+j]='-';
					}
					flip++;
				}
			}
		}
		if(flip!=-1)
		cout<<"Case #"<<x-t<<": "<<flip<<endl;
	}
}
