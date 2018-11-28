#include <iostream>
#include <string>
using namespace std;

int main() {
	int t,r=1,k;
	cin>>t;
	while(r<=t){
		string s;
		cin>>s>>k;
		int ans = 0,l=s.size();
		for(int i=0;i<l;i++)
		{
			if(s[i] == '-' && l-i>=k)
			{
				for(int j=0,m=i;j<k;j++,m++)
				{
				  if(s[m] == '-')	
				  s[m] = '+';
				  else
				  s[m] = '-';
				}
				ans++;
			}
		}
		
		int count = 0;
		for(int i=0;i<l;i++)
		{
			
			if(s[i] == '+')
			count++;
		}
		
		if(count == l)
		cout<<"Case #"<<r<<": "<<ans<<endl;
		else
		cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;
		
		r++;
	}
	return 0;
}