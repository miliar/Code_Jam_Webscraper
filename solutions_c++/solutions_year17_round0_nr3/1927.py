#include<bits/stdc++.h>
using namespace std;

map<long long, long long> cnt;
queue<long long> que;

int main() {

    long long n,k,t,ls,rs,tr,res_rs,res_ls;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {

        scanf("%lld%lld", &n, &k);

        cnt.clear();
        while(!que.empty()) que.pop();

        tr = 0;
        que.push(n);
        cnt[n] = 1;

        while(1) {

            t = que.front();
            que.pop();

            rs = t/2;
            ls = t-rs-1;

            if (tr + cnt[t] >= k) {
                res_ls = ls;
                res_rs = rs;
                break;
            }

            tr += cnt[t];

            if (cnt.count(rs) == 0) {
                que.push(rs);
                cnt[rs] = cnt[t];
            } else {
                cnt[rs] += cnt[t];
            }

            if (cnt.count(ls) == 0) {
                que.push(ls);
                cnt[ls] = cnt[t];
            } else {
                cnt[ls] += cnt[t];
            }
        }


        printf("Case #%d: %lld %lld\n", tt, res_rs, res_ls);
    }

    return 0;
}
