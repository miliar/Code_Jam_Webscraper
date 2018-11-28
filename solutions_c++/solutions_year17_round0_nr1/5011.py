#include <bits/stdc++.h>
using namespace std;
void solve(int tt)
{
    string s;
    int i,k,l = 0,ans=-1;
    cin >> s >> k;
    string t = s;
    for(int i = 0;i < s.length() - k + 1;i++)
    {
        if(s[i]=='-')
        {
            l++;
            for(int j = i ; j < i + k ; j++)
            {
                if(s[j]=='-')  s[j]='+';
                else s[j]='-';
            }
        }
    }
    for(i = 0; i < s.length();i++)if(s[i]=='-') break;
    if(i==s.length()) ans=l;
    cout << "Case #" << tt << ": ";
    if(ans == -1) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;

}
int main()
{
    int T;
    freopen("test.in","r",stdin);
    freopen("res.txt","w",stdout);
    cin >> T;
    for(int i = 1; i <= T ; i++)
        solve(i);
    return 0;
}
