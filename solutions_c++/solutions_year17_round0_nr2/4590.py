#include <bits/stdc++.h>

#define dbg(x) cerr<<#x": "<<x<<"\n"
#define dbg_v(x, n) do{cerr<<#x"[]: ";for(int _=0;_<n;++_)cerr<<x[_]<<" ";cerr<<'\n';}while(0)
#define dbg_ok cerr<<"OK!\n"


using namespace std;

int n, k;

bool ok(int k)
{
	string s = to_string(k);
	for(int i=1;i<s.size();i++)
	{
		if(s[i] < s[i-1])
			return false;
	}
	return true;
}


void solve(int k)
{
	while(!ok(k)) k--;
	cout << k;
}

/*
void solve(string s)
{
	int  ok = 0;
	if(s.size() == 1)
	{
		cout << s;
		return;
	}
	/*
	for(int i=0;i<s.size();i++)
	{
		if(s[i] != '0' && s[i] != '1')
			ok = 1;
	}
	if(ok == 0)
	{
		for(int i=1;i<s.size();i++)
			cout << 9;
		return ;
	}
	int i=1;
	while(s[i] >= s[i-1] && i<s.size())
	{
		i++;
	}
	if(i==s.size())
	{
		cout << s;
		return;
	}

	if(s[i-1] == '1' && s[i] == '0')
	{
		for(int i=1;i<s.size();i++)
			cout << 9;
		return;
	}

	cout << s.substr(0, i-1);
	if(s[i-1] >= '1') 
		cout << char(s[i-1]-1);
	for(int j=i;j<s.size();j++)
		cout << 9;


}
*/

int main()
{
	string s;
	//ios_base::sync_with_stdio(0);
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> n;

	for(int i=1;i<=n;i++)
	{

		cout << "Case #" << i << ": ";
		cin >> k;
		solve(k);
		cout << '\n';
	}



}

 