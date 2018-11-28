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
	int t;
	string s;
	cin>>t;
	for(int tc = 1; tc <= t; tc++)       
	{
		cin>>s;
		bool sp = false;
		int v[s.length()];
		int aux[s.length()];
		for(int i = 0 ; i < s.length(); i++)
		{
			v[i] = (int)s[i] - (int)'0';
		}		
		bool spc = false;
		for(int i = 0 ; i < s.length(); i++)
		{			
			if((i+1) < s.length() && v[i] > v[i+1])
			{
				if(v[i] == 1 && v[i+1] == 0)
				{
					spc = true;
					break;
				}
				else
				{
					int tmp = i;
					while(v[tmp] == v[i])
					{
						tmp--;
					}
					tmp++;
					aux[tmp] = v[tmp] - 1;
					for(int j = tmp + 1; j < s.length(); j++)
					{
						aux[j] = 9;
					}
					break;
				}
			}
			else
			{
				aux[i] = v[i];
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(spc)
		{
			for(int i = 0 ; i < s.length() - 1; i++)
			{
				cout<<9;
			}
		}
		else
		{
			for(int i = 0 ; i < s.length(); i++)
			{
				cout<<aux[i];
			}
		}
		cout<<endl;
	}
}
