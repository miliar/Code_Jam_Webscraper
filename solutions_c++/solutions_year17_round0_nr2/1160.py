#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string solve(string s, int idx, int len)
{
	string ret = s;

	for(int i = len - 1; i >= 0 ; i--)
	{
		for(int j = i + 1 ; j < len ; j++)
		{
			if(ret[i] > ret[j]) 
			{
				ret[i]--;
				for(int k = i + 1 ; k < len ; k++)
				{
					ret[k] = '9';
				}
				break;
			}
		}
	}

	return ret;
}

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);

	freopen("B-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int t;
	cin>>t;

	for(int tc = 1 ; tc <= t; tc++)
	{
		long long int n;
		string sn;
		cin>>n;
		cout<<"Case #"<<tc<<": ";
		sn = to_string(n);
		cout<<stoll(solve(sn, 0, sn.size()))<<'\n';
	}	

	return 0;
}
