#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;

long long string_to_int(string s)
{
	long long ret = 0;
	for (int i = 0; i < s.size(); i++)
        ret = ret * 10 + (s[i] - '0');
	return ret;
}

int main()
{
    freopen("B-large.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
        cout << "Case #" << t << ": ";
		string s;
		cin >> s;
        if (s.size() == 1)
        {
            cout << s << endl;
            continue;
        }
		long long ans = string_to_int(string(s.size() - 1, '9'));
		for (int i = 0; i < s.size(); i++)
        {
            if (i >= 1 && s[i] < s[i - 1]) break;
			if (i == 0 || s[i] - 1 >= s[i - 1])
            {
                //cout << s.substr(0, i) + "!" + char(s[i] - 1) + "!" + string(s.size() - i - 1, '9') << endl;
                ans = max(ans, string_to_int(s.substr(0, i) + char(s[i] - 1) + string(s.size() - i - 1, '9')));
            }
            if (i == s.size() - 1)
                ans = max(ans, string_to_int(s));
        }
        cout << ans << endl;
    }
    return 0;
}
