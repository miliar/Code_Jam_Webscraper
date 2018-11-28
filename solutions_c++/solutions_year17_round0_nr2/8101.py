#include <bits/stdc++.h>

using namespace std;

/*bool comp(string a, string b)
{
    if(a.size() < b.size())
        return true;
    if(b.size() < a.size())
        return false;
    return a < b;
}

string make9(int len)
{
    string res;
    for(i = 1; i < len; ++)
        res.push_back('9');
    return res;
}*/

/*bool bad(string &s)
{
    string ans = make9(s.size());
    for(int pref = -1; pref < s.size(); ++pref)
        if(s[pref + 1] != '0')
        {

        }
}
*/
void solve(int x)
{
    cout << "Case #" << x << ": ";
    string s;
    cin >> s;

    for(int i=0;i+1<s.length();++i)
    {
        int a = s[i]-'0';
        int b = s[i+1]-'0';
        if(a<=b) continue;
        while(i && s[i]==s[i-1])i--;
        s[i]='0'+(a-1);
        for(int j=i+1;j<s.length();++j)
            s[j]='9';
        break;
    }

    if(s[0]=='0')
        cout << s.substr(1,s.length()-1) << "\n";
    else
        cout << s << "\n";

}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int t1 = 1; t1 <= t; ++t1)
        solve(t1);
    return 0;
}
