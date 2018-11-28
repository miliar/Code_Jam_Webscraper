#include <bits/stdc++.h>
using namespace std;

string s;

void solve()
{
	size_t k;
    cin >> s >> k;
    int count = 0;
    for(size_t i = 0; i <= s.size() - k; ++i) if(s[i] == '-')
    {
        for(int j = i; j < i + k; ++j)
            s[j] = (s[j] == '-' ? '+' : '-');
        count += 1;
    }
    for(size_t i = 0; i < s.size(); ++i) if(s[i] == '-')
    {
        cout << "Impossible";
        return;
    }
    cout << count;
}

int main()
{
	int t; cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
        solve();
		cout << endl;
	}
	return 0;
}
