#include <iostream>
#include <queue>

using namespace std;

void solve()
{
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    queue<int> q;
    int ans = 0;
    for(int i=0;i<n;++i)
    {
        if(!q.empty() && q.front()==i) q.pop();
        if( (s[i]=='-') ^ (q.size()%2==1) )
        {
            if(i+k>n)
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
            q.push(i+k);
            ans++;
        }
    }
    cout << ans << "\n";
}

int main()
{
    int T;
    cin >> T;
    for(int t=1;t<=T;++t)
    {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
