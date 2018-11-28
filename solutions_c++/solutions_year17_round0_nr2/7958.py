#include <bits/stdc++.h>
using namespace std;

unsigned long long m[20][20];

void rec(int v, int len, long long n, long long &cur, int lst)
{
    //cout << cur << endl;
    if(v > len) return;
    for(int i = 9; i >= lst; --i)
    {
        if(cur + m[i][len-v+1] <= n)
        {
            cur += m[i][len-v+1] - m[i][len-v];
            rec(v+1, len, n, cur, i);
            break;
        }
    }
}

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for(int j = 0; j <= 9; ++j)
    {
        unsigned long long x = 0;
        for(int i = 1; i <= 18; ++i)
        {
            x *= 10;
            x += j;
            m[j][i] = x;
        }
    }
    int t;
    cin >> t;
    for(int q = 0; q < t; ++q)
    {
        long long n, x, cur = 0;
        cin >> n;
        //cout << n << endl;
        x = n;
        int len = 0;
        while(x > 0)
        {
            len++;
            x /= 10;
        }
        //cout << len << endl;
        rec(1, len, n, cur, 0);
        cout << "Case #" << q+1 << ": " << cur << '\n';
    }
}
