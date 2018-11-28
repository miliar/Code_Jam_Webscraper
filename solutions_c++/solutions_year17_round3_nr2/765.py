#include <bits/stdc++.h>
using namespace std;
int T, ans;
int a[2], allow[2];
struct activity{
    int s, e, id;
    activity() {}
    activity(int _s, int _e, int _id) {
        s = _s;
        e = _e;
        id = _id;
    }
};
typedef vector<activity> va;
typedef vector<int> vi;

bool cmp(activity x, activity y) {
    return x.s < y.s;
}
vector<va> v;
va w;
vector<vi> gaps;

int main() {
    scanf("%d", &T);
    for(int t=1;t<=T;t++) {
        scanf("%d %d", &a[0], &a[1]);
        v.assign(2, va());
        w.clear();
        
        for(int i=0;i<2;i++) {
            allow[i] = 720;
            v[i].assign(a[i], activity());
            for(int j=0;j<a[i];j++) {
                scanf("%d %d", &v[i][j].s, &v[i][j].e);
                v[i][j].id = i;
                allow[i] -= (v[i][j].e-v[i][j].s);
            }

            sort(v[i].begin(), v[i].end(), cmp);
            if(v[i].size() > 0) v[i].push_back(activity(v[i][0].s+1440, v[i][0].e+1440, i));
            for(int j=0;j<v[i].size();j++) w.push_back(v[i][j]);
        }

        sort(w.begin(), w.end(), cmp);
        gaps.assign(2, vi());
        
        ans=0;
        for(int i=1;i<w.size();i++) {
            if(w[i].id == w[i-1].id) {
                gaps[w[i].id].push_back(w[i].s-w[i-1].e);
            } else {
                ans++;
            }
        }
        if(ans) ans--;


        for(int id=0;id<2;id++) {
            int allowance = allow[id];
            sort(gaps[id].begin(), gaps[id].end());
            for(int i=0;i<gaps[id].size();i++) {
                int cur = gaps[id][i];
                if(allowance-cur >= 0) allowance -= cur;
                else {
                    ans += 2*(gaps[id].size()-i);
                    break;
                }
            }
        }
        
        printf("Case #%d: %d\n", t, ans);

    }

}
