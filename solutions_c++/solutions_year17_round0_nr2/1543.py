#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define all(v) v.begin(), v.end()
#define F first
#define S second
#define make0 memset(a,0,sizeof(a))
#define p push_back
#define fast_cin() ios_base::sync_with_stdio(false)
#define pi pair <int,int>
#define pll pair <ll,ll>

bool check(ll N)
{
	string s = to_string(N);
	for(int i=0;i<s.size()-1;i++)
	{
		if(s[i] > s[i+1])
			return false;
	}
	return true;
}

int main()
{
	check(453);
	fast_cin();
	int T;
	cin >> T;
	for(int f = 1 ; f <= T; f++)
	{
		string S;
		cin >> S;
		int idx ;
		bool flag = false;
		for(int i=0;i<S.size()-1;i++)
		{
			if(S[i] > S[i+1])
			{
				for(int j=i;j>=0;j--)
				{
					if(S[j] == S[i])
						idx = j;
					else
						break;
				}
				flag = true;
				break;
			}
		}
		cout << "Case #" << f << ": ";
		if(!flag)
		{
			cout << S << endl;
			continue;
		}
		for(int i=0;i<idx;i++)
		{
			cout << S[i];
		}
		// cout << idx << endl;
		int x = S[idx]-48;
		if(idx == 0)
		{
			if(x > 1)
			{
				cout << (x-1);
			}
		}
		else
		{ 	
			cout << (x-1);
		}
		for(int i=idx+1;i<S.size();i++)
		{
			cout << "9";
		}
		cout << endl;
	}
	return 0;
}