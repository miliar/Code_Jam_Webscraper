#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

#define LOCAL 1

//Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/A-small-attempt0.in

vector<long long> V;

void dfs(int nxt, int pre_num, long long num){
    if(nxt == 18){
        V.push_back(num);
        return;
    }
    for(int i = pre_num; i <= 9; i++){
        dfs(nxt+1, i, num*10+pre_num);
    }
}

int main()
{
#ifdef LOCAL
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/B-small-attempt0.in","r",stdin);
    freopen("/Users/angelzouxin/Desktop/Code/ACM/ACM/ACM/B-small-attempt0.out","w",stdout);
#endif
    dfs(1, 0, 0);
    sort(V.begin(), V.end());
    auto it = unique(V.begin(), V.end());
    V.resize( distance(V.begin(),it));
//    cout << V.size() << endl;
    int t;
    scanf("%d", &t);
    for(int _cas = 1; _cas <= t; ++_cas){
        printf("Case #%d: ", _cas);
        long long n;
        scanf("%lld", &n);
        auto it = lower_bound(V.begin(), V.end(), n);
        printf("%lld\n", *((*it) == n? it : --it));
    }
    
    return 0;
}
