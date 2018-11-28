#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin >> t;
    for (ll i = 1; i <= t; i++) {
        string h;
        cin >> h;
        int k;
        cin >> k;
        string ans;
        for (int j = 0 ; j < h.size(); j++)
            ans.push_back('+');
        queue<pair<string,int>> q;
        q.push({h,0});
        set<string> s;
        s.insert(h);
        bool f = false;
        while (!q.empty())
        {
            string v = q.front().first;
//            cout << v << endl;
            int p = q.front().second;
            if (v == ans)
            {
                cout << "Case #" << i << ": " << p << endl;
                f = true;
                break;
            }
            q.pop();
            for (int j = 0; j < h.size()-k+1; j++)
            {
                string io = v;

                for (int y = j; y < j+k; y++)
                    io[y] = (io[y] == '+' ? '-' : '+');
//                cout << v << " " << io << endl;
                if (s.find(io) == s.end())
                {
//                    cout << "+" << endl;
                    q.push({io,p+1});
                    s.insert(io);
                }
            }
        }
        if (!f)
        {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}