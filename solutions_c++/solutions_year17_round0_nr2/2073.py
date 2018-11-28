#include <iostream>
#include <stdio.h>

typedef long long ll;
typedef float flt;

using namespace std;

void print(int test_number, const string &str)
{
    cout << "Case #" << test_number << ": " << str << endl;
}

void solve(int test_number)
{
    string s;
    cin >> s;
    int n = s.size();
    for (int q = 0; q < n - 1; ++q)
        if (s[q] > s[q + 1])
        {
            for (int i = q + 1; i < n; ++i)
                s[i] = '9';
            bool ok = false;
            for (int i = q; i > 0 and not ok; --i)
            {
                --s[i];
                if (s[i] < '0')
                {
                    s[i] = '9';
                    for (int j = i + 1; j < n; ++j)
                        s[j] = '9';
                    ok = true;
                }
                else if (s[i] >= s[i - 1])
                {
                    ok = true;
                }
                else
                {
                    s[i] = '9';
                    // go to the previous character
                }
            }
            if (ok)
                print(test_number, s);
            else
            {
                --s[0];
                if (s[0] > '0')
                    print(test_number, s);
                else
                    print(test_number, string(n - 1, '9'));
            }
            return;
        }
    print(test_number, s);
}

int main()
{
//  /*
    freopen("btest.in", "r", stdin);
    freopen("btest.out", "w", stdout);
//  */
    
    int cnt_queries;
    cin >> cnt_queries;
    
    for (int _q = 0; _q < cnt_queries; ++_q)
        solve(_q + 1);
    
    
    
    return 0;
}
