#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int foo(vector<int>& s){
    size_t sum = 0, ret = 0;
    for (size_t i=1; i< s.size(); i++){
        sum += s[i];
        size_t tmp = sum / i;
        if (sum % i) tmp++;
        if (tmp > ret) ret = tmp;
    }
    return ret;
}

int main (){
    int T;
    scanf("%d", &T);
    for (int t=1;t<=T;t++){
        int n, c, m;
        scanf("%d%d%d", &n,&c,&m);
        vector<vector<int>> v(c+1);
        vector<int> s(n+1);
        int ms = 0;
        for (int i=0;i<m;i++){
            int p, b;
            scanf("%d%d", &p, &b);
            v[b].push_back(p);
            s[p] ++;
            if (ms < (int)v[b].size())
                ms = v[b].size();
        }
        int re = foo(s);
        int ans1 = max(ms, re);
        int ans2 = 0;
        for (int x : s)
            if (x > ans1)
                ans2 += x - ans1;
        printf("Case #%d: %d %d\n", t, ans1, ans2);
    }
}
