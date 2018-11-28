/* Written BY
Aryan Kumar
ar412
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int j = 1; j <= t; ++j)
	{
		cout<<"Case #"<<j<<": ";
		int n,f=0,i;
		string s;
		cin>>n;
		for ( i = n; i >=1; i--)
		{
			s=to_string(i);
			if(s.length()==1)
				{f=1;}
		else{	for (int k = 0; k < s.length()-1; ++k)
			{
				if(s.at(k)<=s.at(k+1))
					{
						f=1;
					}
				else
				 {// cout<<i<<endl;
				 	f=0;
				break;
			}

			}}
			if(f==1)
				break;
		}
		cout<<i<<endl;
	}

	return 0;
}	