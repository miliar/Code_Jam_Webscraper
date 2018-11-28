#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
	ios::sync_with_stdio(false);
	int t,k,i,j,count;
	string s;
	cin>>t;
	bool poss;
	for(int test=1;test<=t;test++)
	{
		poss=true;
		count=0;
		cin>>s;
		cin>>k;
		for(i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
				count++;
				for(j=i;j<(i+k);j++)
				{
					s[j]=(s[j]=='-')?('+'):('-');
				}
			}
			//cout<<"#"<<i<<" "<<s<<endl;
		}
		
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				poss=false;
				cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
				break;
			}
		}
		if(poss)
		{
			cout<<"Case #"<<test<<": "<<count<<endl;
		}
	}
	return 0;
}