#include <bits/stdc++.h>
using namespace std;

int T;
string pancakes;
int k;
int caso = 0;

void toFlip(int i)
{
    if(pancakes[i] == '-')
        pancakes[i] = '+';
    else
        pancakes[i] = '-';
}

void solve()
{
    cin >> pancakes >> k;
    int n = pancakes.size();

    int flips = 0;
    for (int i = 0; i < n; ++i)
    {
        if(pancakes[i] == '+')
            continue;
        if(i+k > n)
            break;

        for (int j = 0; j < k; ++j)
        {
            toFlip(i+j);
        }
        flips++;
    }

    for (int i = 0; i < n; ++i)
    {
        if(pancakes[i] == '-')
        {
            cout << "Case #" << ++caso << ": IMPOSSIBLE\n";
            return;
        }
    }

    cout << "Case #" << ++caso << ": " << flips << '\n';
}

int main()
{
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        solve();
    }

    return 0;
}
