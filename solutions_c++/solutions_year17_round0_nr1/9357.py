#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios_base :: sync_with_stdio(false);
    freopen("AL.in", "r", stdin);
    freopen("AL.out", "w", stdout);

    int test, c = 0;
    cin >> test;
    while(c++ < test)
    {
        string s;
        int k, ans = 0;
        cin >> s;
        cin >> k;

        while(s.size() != k)
        {
            int ln = s.size();
            int ok = ln-k, left = 0, right = 0;

            for(int i = 0; (s[i] != '-' && i < ok); ++i)
                left++;

            for(int i = ln-1, j = 0; (s[i] != '-' && j < ok-left); --i, ++j)
                right++;

            s.erase(s.begin(), s.begin()+left);
            s.erase(s.end()-right, s.end());

            ln = s.size();
            if(ln != k)
            {
                int l = 0, r = 0;
                for(int i = 0; (s[i] != '+' && i < k); ++i) {
                    l++;
                }

                for(int i = ln-1, j = 0; (s[i] != '+' && j < k); --i, ++j) {
                    r++;
                }

                if(l >= r) {
                    for(int i = 0; i < k; ++i) {
                        if(s[i] == '-') s[i] = '+';
                        else s[i] = '-';
                    }
                }

                else {
                    for(int i = ln-1, j = 0; j < k; --i, ++j) {
                        if(s[i] == '-') s[i] = '+';
                        else s[i] = '-';
                    }
                }

                ans++;
            }

            else break;


            ln = s.size();
            ok = ln-k, left = 0, right = 0;

            for(int i = 0; (s[i] != '-' && i < ok); ++i)
                left++;

            for(int i = ln-1, j = 0; (s[i] != '-' && j < ok-left); --i, ++j)
                right++;

            s.erase(s.begin(), s.begin()+left);
            s.erase(s.end()-right, s.end());
        }

        int plu = 0, minu = 0;

        for(int i = 0; i < k; ++i) {
            if(s[i] == '+') plu++;
            else minu++;
        }

        cout << "Case #" << c << ": ";
        if(plu == k) cout << ans << "\n";
        else if(minu == k) cout << ans+1 << "\n";
        else cout << "IMPOSSIBLE\n";
    }

    return 0;
}
