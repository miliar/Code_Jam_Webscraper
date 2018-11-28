#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
typedef long long ll;
struct bathroom{
    ll num, fre;
    bathroom(ll num, ll fre){
        this->num = num;
        this->fre = fre;
    }
};
struct cmp{
    bool operator ()(bathroom x, bathroom y){
        return x.num < y.num;
    }
};
int main(){
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++){
        ll n, k;
        scanf("%lld%lld",&n, &k);
        priority_queue<bathroom, vector<bathroom>, cmp> q;
        bathroom tmp(n, 1);
        q.push(tmp);
        int tot = 0;
        while (tot < k){
            tmp = q.top();
            q.pop();
            tot += tmp.fre;
            if (tmp.num & 1){
                bathroom left((tmp.num - 1) / 2, tmp.fre * 2);
                q.push(left);
            }
            else{
                bathroom left(tmp.num / 2, tmp.fre), right(tmp.num / 2 - 1, tmp.fre);
                q.push(left);
                q.push(right);
            }
        }
        printf("Case #%d: ", z);
        if (tmp.num & 1) printf("%lld %lld\n", (tmp.num - 1) / 2, (tmp.num - 1) / 2);
        else printf("%lld %lld\n", tmp.num / 2, tmp.num / 2 - 1);
    }
    return 0;
}