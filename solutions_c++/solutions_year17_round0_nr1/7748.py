#include <iostream>
using namespace std;

int main() {
int t,tt,k,ret,l;
string s;
cin>>t;
tt=t;
while(tt--)
{
	ret=l=0;
	cin>>s>>k;
	for(int q=0;q<=s.length()-k;q++)
	{
		if(s[q]=='-')
		{
			// cout<<q+1<<" ";
			ret++;
			for(int qq=q;qq<q+k;qq++)
			{
				if(s[qq]=='-')
					s[qq]='+';
				else
					s[qq]='-';
				// cout<<s<<endl;
			}
		}
	}
	for(int q=s.length()-k;q<s.length();q++)
		if(s[q]=='+')
			l++;
	if(l==k)
		cout<<"Case #"<<t-tt<<": "<<ret<<endl;
	else
		cout<<"Case #"<<t-tt<<": "<<"IMPOSSIBLE"<<endl;
}
return 0;
}