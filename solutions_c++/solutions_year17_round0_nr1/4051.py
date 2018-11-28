#include <bits/stdc++.h>

using namespace std;

int main()
{
        ios_base::sync_with_stdio(false);
//        freopen("a.txt", "r", stdin);
//        freopen("a.out", "w", stdout);
        int Q;  cin >> Q;
        for (int _case_ = 1; _case_ <= Q; _case_++)
        {
                string s;       cin >> s;
                int n = s.length();
                int k;          cin >> k;

                vector <int> a(n+1);
                for (int i = 1; i < n; i++)
                        a[i] = s[i] != s[i-1];
                a[0] = s[0] != '+';
                a[n] = s[n-1] != '+';

//                for (auto i : a) cout << i << ' ';
//                cout << endl;
                int res = 0;
                for (int i = 0; i <= n && res > -1; i++) if ( a[i] )
                {
                        int j;
                        for (j = i+k; j <= n; j += k) if ( a[j] )
                        {
                                a[j] = a[i] = 0;
                                res += (j-i) / k;
                                break;
                        }
                        if ( j > n ) res = -1;
                }


                cout << "Case #" << _case_ << ": ";
                if ( res == -1 )
                        cout << "IMPOSSIBLE\n";
                else
                        cout << res << "\n";
        }
        return 0;
}
