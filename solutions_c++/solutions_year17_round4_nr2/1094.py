#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> p;

int T;
vector<p> v;
set<int> S[1005];
int no[1005];
int used[1005][1005]; //做过的过山车


int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    int cs = 1;
    while(T--) {
        int N, C, M;
        scanf("%d%d%d",&N,&C,&M);
        v.clear();
        for(int i = 1; i <= M; i++) {
            int t1, t2;
            scanf("%d%d",&t1,&t2);
            v.push_back(p(t1,t2));
        }
        sort(v.begin(), v.end());
        int l = 1, r = M + 1, mid;
        int res = M;
        int r2 = 0;
        while(l < r) {
            int tr2 = 0;
            mid = (l + r) / 2;
            //printf("mid=%d\n",mid);
            for(int i = 0; i < mid; i++) {
                S[i].clear();
                no[i] = 1;
            }
            for(int i = 1; i <= C; i++) {
                memset(used[i],0,sizeof(used[i]));
            }
            int gg = 0;
            for(p tp: v) {
                int t1 = tp.first, t2 = tp.second;


                int qm = 1;
                for(int i = 0; i < mid; i++) {
                    if(used[t2][i]) continue;
                    if(S[i].find(t1) == S[i].end()){
                        qm = 0;
                        used[t2][i] = 1;
                        S[i].insert(t1);
                        break;
                    }
                }
                if(qm) {
                    int gg2 = 1;
                    for(int i = 0; i < mid; i++) {
                        if(used[t2][i]) continue;
                        if(no[i] > t1) {
                            continue;
                        }
                        int gg3 = 0;
                        while(S[i].find(no[i]) != S[i].end()) {
                            no[i]++;
                            if(no[i] > t1) {
                                gg3 = 1;
                                break;
                            }
                        }
                        if(gg3) continue;
                        S[i].insert(no[i]);
                        used[t2][i] = 1;
                        tr2++;
                        gg2 = 0;
                        break;
                    }
                    if(gg2) gg = 1;
                }
                if(gg) break;
            }
            if(gg) {
                l = mid + 1;
            }
            else {
                if(mid < res) {
                    res = mid;
                    r2 = tr2;
                }
                else if(mid == res) {
                    r2 = min(r2, tr2);
                }
                r = mid;
            }
        }
        printf("Case #%d: %d %d\n",cs++,res,r2);
    }
}

