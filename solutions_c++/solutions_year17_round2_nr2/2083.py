#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

void print(int i)
{
    char c;
    switch (i) {
        case 0: c = 'R'; break;
        case 2: c = 'Y'; break;
        case 4: c = 'B'; break;
    }
    printf("%c", c);
}

bool solve()
{
    int n;
    scanf("%d",&n);
    int a[6];
    set <pair<int, int>> s;
    bool f = false;;
    for (int i = 0; i < 6; ++i) {
        scanf("%d", &a[i]);
        if (n / 2 < a[i]) {
            f = true;
        }
        if (a[i])
            s.insert({a[i], i});
    }
    if (f) {
        puts("IMPOSSIBLE");
        return false;
    }
    while (!s.empty()) {
        auto it = s.rbegin();
        auto p1 = *it;
        s.erase(p1);
        while (p1.first) {
            print(p1.second);
            p1.first--;
            if (!s.empty()) {
                auto p2 = *s.rbegin();
                print(p2.second);
                s.erase(p2);
                if (p2.first > 1) {
                    s.insert({p2.first - 1, p2.second});
                }
            }
        }
    }
    puts("");
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
