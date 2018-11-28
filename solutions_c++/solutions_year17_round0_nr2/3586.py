#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

int down(int num)
{
    stringstream ss; ss << num;
    string s = ss.str();
    int n = s.size();
    int id = n - 1;
    while (id > 0 and s[id] == s[id - 1])
        id--;
    int ret = 0;
    for (int i = 0; i < id; i++)
        ret = ret * 10 + (s[i] - '0');
    ret = ret * 10 + (s[id] - '0' - 1);
    for (int i = id + 1; i < n; i++)
        ret = ret * 10 + 9;
    return ret;
}

int go(int num)
{
    stringstream ss; ss << num;
    string s = ss.str();
    int n = s.size();
    int id = -1;
    for (int i = 0; i + 1 < n; i++)
        if (s[i] > s[i + 1])
        {
            id = i;
            break;
        }
    if (id < 0) return num;
    int now = 0;
    for (int i = 0; i <= id; i++)
        now = now * 10 + (s[i] - '0');
    int ret = down(now);
    for (int i = id + 1; i < n; i++)
        ret = ret * 10 + 9;
    return ret;
}

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int n; cin >> n;
        cout << "Case #" << tt << ": " << go(n) << "\n";
    }
    return 0;
}
