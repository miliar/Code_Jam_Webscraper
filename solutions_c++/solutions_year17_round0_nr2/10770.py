#include <bits/stdc++.h>

using namespace std;

bool solve (int x)
{
    vector<int> v ;
    while (x)
    {
        int t = x%10;
        v.push_back(t);
        x/=10;
    }
    reverse(v.begin(),v.end());
    for (int i=1;i<v.size();i++)
    {
        if (v[i] < v[i-1]) return false;
    }
    return true;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int tc ;
    cin >> tc ;
    for (int t = 1;t<=tc;t++)
    {
        int x,ans;
        cin >> x;
        while (1)
        {
            if (solve(x))
            {
                ans = x;
                break;
            }
            x--;
        }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
