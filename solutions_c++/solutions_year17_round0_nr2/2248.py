#include<bits/stdc++.h>
using namespace std;

void correggi(string& n, int pos)
{
	for(int i=pos+1; i<(int)n.length(); ++i)
		n[i] = '9';
	--n[pos--];
	while(pos>=0 && n[pos]>n[pos+1]) {
		n[pos+1] = '9';
		--n[pos--];
	}
}

string pulisci(string& n)
{
	int i=0;
	while(i<(int)n.length() && n[i]=='0')
		++i;
	return n.substr(i);
}

string solve(string& n)
{
	for(int i=0; i<(int)n.length()-1; ++i)
		if(n[i]>n[i+1])
			correggi(n, i);
	return pulisci(n);
}

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;

	for(int i=1; i<=t; ++i) {
		string n;
		cin >> n;
		cout << "Case #" << i << ": " << solve(n) << "\n";
	}

	return 0;
}
