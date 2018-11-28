#include <cstdio>
#include <iostream>
#include <string>

using namespace std;


void solve(int test) {
    char s1[1005];
    string s;
    int K;
    scanf("%s %d\n", s1, &K);

    s = string(s1);

    int cnt = 0;
    for (int i = 0; i < s.size() - K + 1; i++) 
    {
        if (s[i] == '-') {
            cnt++;
            for (int j = i; j < i + K; j++)
            {
                s[j] = s[j] == '+' ? '-' : '+';
            }
        }
    }

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '-') {
            cout << "CASE #" << test << ": IMPOSSIBLE" << endl;
            return;
        }
    }

    cout << "CASE #" << test << ": " << cnt << endl;
}

int main()
{
    int T;

    freopen("pancake.in", "r", stdin);
    freopen("pancake.out", "w", stdout);

    scanf("%d ", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
}
