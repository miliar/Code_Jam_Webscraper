#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main()
{
	ios::sync_with_stdio(false);
	ll t;
	cin>>t;
	for(int x = 0; x < t; ++x)
	{
		string n;
		cin>>n;
		int sz = n.size();
		for(int  i = 0; i < sz - 1; ++i)
		{
			if((int)n[i] > (int)n[i+1])
			{
				for(int j = i+1; j< sz; ++j)
					n[j] = '9';
				n[i]--;
				while(i != 0)
				{
					if((int)n[i] < (int)n[i-1])
					{
						n[i] = '9';
						n[i - 1]--;
						--i;
					}
					else
					{
						break;
					}
				}
				break;
			}
		}
		cout<<"Case #"<<x+1<<": ";
		if(n[0] != '0')
			cout<<n<<endl;
		else
			cout<<n.substr(1)<<endl;
	}
	return 0;
}