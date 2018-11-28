#include <bits/stdc++.h>
using namespace std;

template <typename T>
string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}

bool check (int n)
{
    string s=NumberToString (n);
    string t=s;
    sort (t.begin(),t.end());
    if (t!=s)
        return false;
    for (int i=0;i<s.size();++i)
    {
        if (s[i]=='0')
            return false;
    }
    return true;
}

int main()
{
    freopen ("B-small-attempt3.in","rt",stdin);
    freopen ("A-small-practice.txt","wt",stdout);
    int t;
    cin >> t;
    for (int tc=1; tc<=t; tc++)
    {
        int n;
        cin >> n;
        //cout << n << ends;
        while (1)
        {
            if (check(n)==true)
                break;
            else
                n--;
        }
        cout << "Case #" << tc << ": " << n << endl;
    }
}
