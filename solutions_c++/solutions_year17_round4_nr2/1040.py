#include <stdio.h>
#include <vector>
using namespace std;

int P[1005], B[1005];
int a[1005][1005];
int mrk[1005][1005];
int done[1005][1005];

int main(){
    int T;
    scanf("%d", &T);
    for(int tc=1; tc<=T; tc++){
        int N, C, M;
        scanf("%d%d%d", &N, &C, &M);
        vector<int> v[1005], vr[1005];
        for(int i=1; i<=M; i++){
            scanf("%d%d", &P[i], &B[i]);
            v[B[i]].push_back(P[i]);
            vr[P[i]].push_back(B[i]);
        }
        int l=1, r=M;
        for(int i=1; i<=C; i++) if(v[C].size() > l) l = (int)v[C].size();
        int res1=-1, res2=-1;
        while(l<=r){
            int m = (l+r)>>1;
            int rem = M;
            int trial = 0;
            int promoted = 0;
            for(int i=1; i<=N; i++) for(int j=1; j<=m; j++) a[i][j] = 0;
            for(int i=1; i<=m; i++) for(int j=1; j<=C; j++) mrk[i][j] = 0;
            for(int i=1; i<=N; i++) for(int j=0; j<vr[i].size(); j++) done[i][j] = 0;
            vector< pair<int, int> > vt;
            for(int i=1; i<=N; i++) vt.push_back(make_pair(-(int)vr[i].size(), i));
            sort(vt.begin(), vt.end());
            while(rem && trial < N){
                for(int x=0; x<N; x++){
                    int i = vt[x].second;
                    if(i-trial < 1) continue;
                    for(int j=0; j<vr[i].size(); j++){
                        int people = vr[i][j];
                        int opposite = 1;
                        if(people == 1) opposite = 2;
                        if(done[i][j]) continue;
                        int ok = 0;
                        for(int k=1; k<=m; k++){
                            if(a[i-trial][k] || mrk[k][people] || mrk[k][opposite]) continue;
                            a[i-trial][k] = 1;
                            mrk[k][people] = 1;
                            if(trial) promoted++;
                            rem--;
                            ok = 1;
                            done[i][j] = 1;
                            break;
                        }
                        if(ok) continue;
                        for(int k=1; k<=m; k++){
                            if(a[i-trial][k] || mrk[k][people]) continue;
                            a[i-trial][k] = 1;
                            mrk[k][people] = 1;
                            if(trial) promoted++;
                            rem--;
                            done[i][j] = 1;
                            break;
                        }
                    }
                }
                trial++;
            }
            if(rem == 0) r = m-1, res1 = m, res2 = promoted;
            else l = m+1;
        }
        printf("Case #%d: %d %d\n", tc, res1, res2);
    }
    return 0;
}