#include <bits/stdc++.h>
using namespace std;
vector<pair<int, int>> vc[1010];
void Solve(){
    int N, C, M;
    scanf("%d%d%d", &N, &C, &M);
    for(int i = 0 ; i <= N ; i++)
        vc[i].clear();
    vector<bool> mvis(M);
    vector<int> cnt(C + 1);
    for(int i = 0 ; i < M ; i++){
        int p, b;
        scanf("%d%d", &p, &b);
        cnt[b]++;
        vc[p].push_back({i, b});
    }
    for(int i = 1 ; i <= N ; i++){
        sort(vc[i].begin(), vc[i].end(), [&](const pair<int, int>& a, const pair<int, int>& b){return cnt[a.second] > cnt[b.second];});
    }
    vector<int> pros(N + 1, 0);
    vector<int> last_pro1(N + 1, 0);
    vector<int> last_pro2(N + 1, 0);
    vector<bool> last_nvis(N + 1);
    int op = 0, pro = 0;
    while(M){
        last_pro2 = last_pro1;
        fill(last_pro1.begin(), last_pro1.end(), 0);
        vector<bool> cvis(C + 1);
        vector<bool> nvis(N + 1);
        int last = 0;
        for(int i = 1 ; i <= N ; i++){
            if(!vc[i].size())continue;
            sort(vc[i].begin(), vc[i].end(), [&](const pair<int, int>& a, const pair<int, int>& b){return cnt[a.second] > cnt[b.second];});
            int now = i;
            for(auto t : vc[i]){
                if(mvis[t.first])continue;
                if(cvis[t.second])continue;
                if(now != i)pros[i]++;
                //printf("%d %d %d %d\n", t.first, i, t.second, now);
                M--;
                mvis[t.first] = true;
                cvis[t.second] = true;
                nvis[now] = true;
                cnt[t.second]--;
                last_pro1[i]++;
                while(now && nvis[now]) now--;
                //printf("next %d\n", now);
                if(now == 0)break;
            }
            if(now != i)last = i;
        }
        last_nvis = nvis;
        op++;
        //puts("===");
    }
    if(op >= 2){
        for(int i = 1 ; i <= N ; i++){
            if(last_nvis[i] == false && last_pro2[i] > 1)
                pro--;
        }
    }
    pro = 0;
    for(int i = 1 ; i <= N ; i++){
        pro += min(max((int)vc[i].size() - op, 0), pros[i]);
    }
    printf("%d %d\n", op, pro);
}
int main(){
    int T;
    scanf("%d", &T);
    for(int i = 1 ; i <= T ; i++){
        printf("Case #%d: ", i);
        Solve();
    }
    return 0;
}
