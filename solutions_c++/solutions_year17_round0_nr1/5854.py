#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,k,length;
	char x[1010];
	
	cin>>t;					// i am boss
	for(int pt=0;pt<t;pt++)
	{
	scanf("%s",x);				// scanning the number
	length=strlen(x);
	cin>>k;
	int c=0;
	int c1=1;
	for(int i=0;i<length;i++)
		{
			if(x[i]=='-')
			{
				c++;
				for(int j=i;j<i+k;j++)
			{
					if(i+k>length)					// different conditions for checking the number
					{
					c1=0;
					break;
					}
					if(x[j]=='-')
					{
						x[j]='+';
				//	cout<<"if"<<endl;
					}
					else
					{
						x[j]='-';
				//	cout<<"else"<<endl;
					}
					//cout<<s<<endl;
		}
			
			}
			if(c1==0)							// if single digit number
		{
				cout<<"Case #"<<pt+1<<": IMPOSSIBLE"<<endl;
		break;
			}
			
		}
		if(c1==1)
		{								// printing the number
			cout<<"Case #"<<pt+1<<": "<<c<<endl;
		}
	}
	return 0;
}
