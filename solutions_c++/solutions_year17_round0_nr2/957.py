#include <iostream>
#include <string>

using namespace std;

int T;

string n;

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> n;
        int x = 0;
        while (x < n.length()-1 && n[x] <= n[x+1])
            ++x;
        if (x == n.length() - 1)
        {
            cout << "Case #" << t << ": " << n << endl;
            continue;
        }
        --n[x]; 
        for (int i = x + 1; i < n.length(); ++i)
            n[i] = '9';
        while (x > 0 && n[x] < n[x-1])
        {
            n[x] = '9';
            --n[x-1];
            --x;
        }
        if (n[0] == '0')
            n.erase(0, 1);
        cout << "Case #" << t << ": " << n << endl;
    }
    return 0;
}