#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>

using namespace std;


int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
	int n,k,c;
	string s;
	cin>>n;
	for(int tc = 1; tc <= n; tc ++)
	{
		cin>>s>>k;
		bool aux[s.length()];
		for(int i = 0 ; i < s.length(); i++)
		{
			if(s[i] == '+')
			{
				aux[i] = true;			
			}
			else
			{
				aux[i] = false;
			}
		}
		c=0;
		for(int i = 0 ; i <= (s.length() - k); i++)
		{
			/*cout<<"aux is: "<<endl;
			for(int j = 0 ; j < s.length(); j++)
			{
				cout<<aux[j];
			}
			cout<<endl;*/
			if(!aux[i])
			{
				c++;
				//cout<<"Changing in index: "<<i<<endl;
				for(int ip = i; ip < (i + k); ip++)
				{
					//cout<<"flipping: "<<ip<<endl;
					aux[ip] = !aux[ip];
				}				
			}
		}
		bool p = true;
		for(int i = 0; i < s.length(); i++)
		{
			if(!aux[i])
			{
				p = false;
				break;
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(p)
		{
			cout<<c;
		}
		else
		{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
}
