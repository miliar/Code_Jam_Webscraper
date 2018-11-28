#include <bits/stdc++.h>
using namespace std;

#define pi 2.0*acos(0.0)
#define ri reverse_iterator
#define pq priority_queue
#define mp make_pair
#define ub upper_bound
#define er equal_range
#define nl '\n'
#define f first
#define lb lower_bound
#define mem(a, b) memset(a, b, sizeof(a))
#define q queue
#define s second
#define big INT_MAX
#define small INT_MIN
#define pb push_back
#define inp freopen("in.txt", "r", stdin)
#define out freopen("out.txt", "w", stdout)

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
typedef pair <long long, int> pli;

int main()
{
    ios_base :: sync_with_stdio(false);
    inp;
    out;

    int test, c = 0;
    cin >> test;
    while(c++ < test)
    {
        string s;
        int k, nadus = 0;
        cin >> s;
        cin >> k;

        while(s.size() != k)
        {

            //1st erase
            int ln = s.size();
            int ok = ln-k, left = 0, right = 0;

            for(int i = 0; (s[i] != '-' && i < ok); ++i)
                left++;

            for(int i = ln-1, j = 0; (s[i] != '-' && j < ok-left); --i, ++j)
                right++;

            s.erase(s.begin(), s.begin()+left);
            s.erase(s.end()-right, s.end());

            //flip:
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

                nadus++;
            }

            else break;


            //2nd erase
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
        if(plu == k) cout << nadus << nl;
        else if(minu == k) cout << nadus+1 << nl;
        else cout << "IMPOSSIBLE\n";
    }

    return 0;
}
