#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> list;

void gen(long long num, int d, int l) {
    if(l == 0) {
        list.push_back(-num);
        return;
    }
    num *= 10;
    l--;
    for(int i = d; i <= 9; i++) {
        gen(num + i, i, l);
    }
}

int main() {
    list.reserve(3124550);
    gen(0, 0, 17);
    reverse(list.begin(), list.end());
    
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        long long N;
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", t, -*lower_bound(list.begin(), list.end(), -N));
    }
    return 0;
}
