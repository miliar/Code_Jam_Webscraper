#include <bits/stdc++.h>
#define loop(i, a, n) for(int i = a; i < n; i++)
#define cin in
#define cout out
using namespace std;

ifstream in("in.in");
ofstream out("out.txt");

void prep()
{
    static int t = 1;
    cout << "Case #" << t++ << ": ";
}

void flip(vector<bool>& pan, int index, int num)
{
    loop(i, index, index + num) pan[i] = !pan[i];
}

bool check(const vector<bool>& arr)
{
    for (auto x : arr) if (x) return false;
    return true;
}

void func()
{
    string s;
    vector<bool> pan;
    int k, count = 0;
    cin >> s >> k;
    for (auto& x : s) pan.push_back(x == '-');
    loop(i, 0, pan.size() - k + 1) if (pan[i]) flip(pan, i, k), count++;
    if (check(pan)) cout << count << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main()
{
    int t; cin >> t;
    while(t--) prep(), func();
    return 0;
}

