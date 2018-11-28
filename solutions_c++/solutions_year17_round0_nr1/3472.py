#include<bits/stdc++.h>
using namespace std;

string imp = "IMPOSSIBLE";

void solve(int t)
{
    int k,cnt = 0;
    string s;
    cin >> s >> k;
    bool flip = true;
    for(int i=0; i<s.length() ;i++)
    {
        if(s[i] == '-')
        {
            if(i+k > s.length()) {flip = false; break;}

            for(int j=i;j<i+k;j++)
                s[j] = s[j] == '+' ? '-' : '+';
            cnt++;
        }
    }

    cout <<"Case #" << t << ": ";
    if(!flip)
        cout << imp << endl;
    else
        cout << cnt << endl;

}

int main(void)
{
    int T;
    cin >> T;
    for(int tc = 1; tc<=T; tc++)
        solve(tc);

    return 0;
}
