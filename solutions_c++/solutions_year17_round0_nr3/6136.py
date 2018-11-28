#include <bits/stdc++.h>

using namespace std;
multiset<int> s;

void do_something()
{
    int Max = -*s.begin() - 1;
    s.erase(s.begin());
    s.insert(-(Max / 2));
    s.insert(-(Max - Max / 2));
}

int main()
{
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int _ = 0; _ < t; ++_)
    {
        int n, k;
        cin >> n >> k;
        s.clear();
        s.insert(-n);
        for (int i = 0; i < k - 1; ++i)
            do_something();
        int Min = -*s.begin() - 1;
        if (Min == -1)
        {
            cout << "Case #" << _ + 1 << ": " << 0 << " " << 0 << endl;
        }
        else
            cout << "Case #" << _ + 1 << ": " << Min - Min / 2 << " " << Min / 2 << endl;
    }
}
