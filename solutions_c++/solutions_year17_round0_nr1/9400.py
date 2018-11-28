#include <bits/stdc++.h>
using namespace std;
 
int main() 
{
	int t;
	cin>>t;
	string str;
	int flip;
	for(int i=0;i<t;i++) {
		cin>>str>>flip;
		string ans;
		int len=str.size(),c=0,found=0;
		for(int k=0;k<len;k++) 
		{
			if(str[k]=='-') 
			{
				if((k+flip-1)>=len) 
				{
					cout <<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
					found=1;
					break;
				}
				for(int j=0;j<flip;j++) {
					if(str[k+j]=='+')
						str[k+j]='-';
					else if(str[k+j]=='-')
						str[k+j]='+';
				}
				c++;
			}
			ans=to_string(c);
		}
        if(found!=1)
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}