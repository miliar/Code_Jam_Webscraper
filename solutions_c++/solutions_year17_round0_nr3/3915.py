#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <cmath>
#include <random>
#include <set>
#include <cstring>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))

int n, k;

int getLeft(int size) {
    return (size-1)/2;
}
int getRight(int size) {
    return size / 2;
}

class keng {
public:
    int mi, mx, index, size, index_to_choose;
    keng(int mi_, int mx_, int index_, int size_) : mi(mi_), mx(mx_), index(index_), size(size_) {
        index_to_choose = index + (size-1) / 2;
    }
    keng(int size_, int index_) : size(size_), index(index_) {
        int left = getLeft(size);
        int right = getRight(size);
        mi = min(left, right);
        mx = max(left, right);
        index_to_choose = index + (size-1) / 2;
    }
    const bool operator < (const keng& k) const {
        if (mi == k.mi) {
            if (mx == k.mx) {
                return index_to_choose < k.index_to_choose;
            }
            return mx < k.mx;
        }
        return mi < k.mi;
    }
};

void solve()
{
    priority_queue<keng> que;
    que.push(keng(n, 1));
    for(int i = 0; i < k; ++i) {
        keng ck = que.top();
       // cout << ck.index << " " << ck.size << " " << ck.mx << " " << ck.mi << endl;
        que.pop();
        if (i == k-1) {
            printf("%d %d\n", ck.mx, ck.mi);
        }
        que.push(keng(getLeft(ck.size), ck.index));
        que.push(keng(getRight(ck.size), ck.index_to_choose+1));
    }
}

int main() {
    int cas = 0;
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T;
    cin >> T;
    while (T--) {
        printf("Case #%d: ", ++cas);
        cin >> n >> k;
        solve();
    }
    return 0;
}
