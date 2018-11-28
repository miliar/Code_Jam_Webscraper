#include <set>
#include <map>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define FIN freopen("C-small-2-attempt0.in", "r", stdin)
#define FOUT freopen("C-small-2-attempt0.out", "w", stdout)

const int N = 1e2 + 5;

bool vis[N];

int f_ls(int x) {
    int l = 0;
    while(x >= 0 && !vis[x]) {
        --x;
        ++l;
    }
    return l - 1;
}

int f_rs(int x) {
    int r = 0;
    while(x < N && !vis[x]) {
        ++x;
        ++r;
    }
    return r - 1;
}

bool cmp(int a, int b) {
    int a_ls = f_ls(a);
    int a_rs = f_rs(a);
    int b_ls = f_ls(b);
    int b_rs = f_rs(b);
    if(min(a_ls, a_rs) > min(b_ls, b_rs)) {
        return true;
    }
    else if(min(a_ls, a_rs) < min(b_ls, b_rs)) {
        return false;
    }
    else if(max(a_ls, a_rs) > max(b_ls, b_rs)) {
        return true;
    }
    else if(max(a_ls, a_rs) < max(b_ls, b_rs)) {
        return false;
    }
    else if(a < b){
        return true;
    }
    else {
        return false;
    }
}

void pre(int n) {
    memset(vis, false, sizeof(vis));
    vis[0] = true;
    vis[n + 1] = true;

    for(int i = 1; i <= n; i++) {
        vector<int> vec;
        for(int j = 1; j <= n; j++) {
            if(!vis[j]) {
                vec.push_back(j);
            }
        }
        sort(vec.begin(), vec.end(), cmp);
        int chose = vec[0];
        int ls = f_ls(chose);
        int rs = f_rs(chose);
        printf("#the %dth chosen: %d, <%d, %d>#\n", i, chose, max(ls, rs), min(ls, rs));
        vis[chose] = true;
    }
}

int get_top_of_set(set<long long> &s) {
    set<long long>::iterator it = s.end();
    --it;
    return *it;
}

int main() {
    FIN;
    FOUT;
    //pre(100);
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        long long n, k;
        scanf("%I64d%I64d", &n, &k);
        set<long long> s;
        map<long long, long long> m;
        s.insert(n);
        m[n] = 1;
        int kk = 0;
        pair<long long, long long> ans;
        while(kk < k) {
            long long mmax = get_top_of_set(s);
            s.erase(mmax);
            long long cnt = m[mmax];
            long long x = (mmax - 1) / 2;
            long long y = (mmax - 1) - x;
            s.insert(x);
            s.insert(y);
            m[x] += cnt;
            m[y] += cnt;
            kk += cnt;
            //printf("<%I64d, %I64d> -> (%I64d, %I64d)\n", mmax, cnt, x, y);
            ans = make_pair(y, x);
        }
        printf("Case #%d: %I64d %I64d\n", ++ncase, ans.first, ans.second);
    }
    return 0;
}
