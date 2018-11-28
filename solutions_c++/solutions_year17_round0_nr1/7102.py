#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,k,l;
	char s[1005];
	
	cin>>t;
	for(int m=0;m<t;m++)
	{
		scanf("%s",s);
		l=strlen(s);
		cin>>k;
		int c=0;
		int flag=1;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(int j=i;j<i+k;j++)
				{
					if(i+k>l)
					{
						flag=0;
						break;
					}
					if(s[j]=='-')
					{
						s[j]='+';
					//	cout<<"if"<<endl;
					}
					else
					{
						s[j]='-';
					//	cout<<"else"<<endl;
					}
					//cout<<s<<endl;
				}
			
			}
			if(flag==0)
			{
				cout<<"Case #"<<m+1<<": IMPOSSIBLE"<<endl;
				break;
			}
			
		}
		if(flag==1)
		{
			cout<<"Case #"<<m+1<<": "<<c<<endl;
		}
	}
	return 0;
}