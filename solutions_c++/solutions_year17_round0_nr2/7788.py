#include <bits/stdc++.h>
using namespace std;


int main() {
    #ifdef LOCAL
        freopen("z.in", "rt", stdin);
        freopen("z.out", "wt", stdout);
    #endif

    int t, k;
    string n;
    cin >> t;
    for(int test = 1; test <= t; test++)
    {
        cin >> n;
        cout << "Case #" << test << ": ";
        int st = -1;
        for(int i = 1; i < n.length(); i++)
        {
            if(n[i] < n[i-1])
            {
                st = i;
                break;
            }
        }
        if(st != -1)
        {
            for(int i = st; i < n.length(); i++)
                n[i] = '9';
            
        }
        st--;
        while(st > 0 && n[st] == n[st-1])
        {
            n[st] = '9';
            st--;
        }
        n[st]--;
        if(n[0] == '0')
            n.erase(n.begin());
        cout << n << endl;
    }
 
    // cerr << "done";
    return 0;
}