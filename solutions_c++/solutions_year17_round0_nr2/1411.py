#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

bool valid(string& x)
{
    int p = x[0];
    for(int i = 1; i < (int)x.length(); i++)
    {
        if (p > x[i])
            return false;
        p = x[i];
    }
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int CNO = 1; CNO <= T; CNO++)
    {
        long long N;
        cin >> N;
        string s = to_string(N);
        while(!valid(s))
        {
            for(int i = 1; i < (int)s.length(); i++)
            {
                if (s[i-1] > s[i])
                {
                    s[i-1]--;
                    for(int j = i; j < (int)s.length(); j++)
                        s[j] = '9';
                    break;
                }
            }
        }
        printf("Case #%d: %lld\n", CNO, stoll(s));
    }
    return 0;
}