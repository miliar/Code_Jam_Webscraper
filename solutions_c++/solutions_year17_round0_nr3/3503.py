#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;
struct comp {
    bool operator() (const int& a, const int&b)
    {
        return a > b;
    }
};
int main()
{
    int tc, cn;
    int n, k;
    int i, j;
    int maxlen, ls, rs;
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        multiset<int, comp> ss;
        multiset<int, comp>::iterator it;
        scanf("%d%d", &n, &k);
        ss.insert(n+1);
        while (k--) {
            it = ss.begin();
            maxlen = *it;
            ss.erase(it);
            ls = maxlen/2;
            rs = maxlen-maxlen/2;
            ss.insert(ls);
            ss.insert(rs);
        }
        printf("Case #%d: %d %d\n", cn, max(ls,rs)-1, min(ls,rs)-1);
    }
    return 0;
}
