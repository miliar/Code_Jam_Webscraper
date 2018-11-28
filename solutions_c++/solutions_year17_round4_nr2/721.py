#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

struct T {
    int p,id;
} tic[1005];

int n,c,m;
int used[1005],done[1005];

bool cmp(T a,T b) {
    return a.p < b.p;
}

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%d%d%d",&n,&c,&m);
        for (int i=0; i<m; i++) {
            scanf("%d%d",&tic[i].p,&tic[i].id);
        }
        sort(tic,tic+m,cmp);

        memset(done,0,sizeof(done));
        int cnt = m,ret = 0;
        while (cnt > 0) {
            memset(used,0,sizeof(used));
            int occ = 0;
            for (int i=0; i<m; i++) {
                if (done[i]) continue;
                //printf("train %d: %d,%d (%d)\n",ret,tic[i].p,tic[i].id,occ);
                if (occ < tic[i].p && used[tic[i].id] == 0) {
                    occ++;
                    cnt--;
                    used[tic[i].id] = 1;
                    done[i] = 1;
                }
            }
            ret++;
        }

        for (int i=1; i<=n; i++) {
            used[i] = ret;
        }
        for (int i=0; i<m; i++) {
            used[tic[i].p]--;
        }
        int res = 0;
        for (int i=1; i<=n; i++) {
            if (used[i] < 0) res -= used[i];
        }
        printf("Case #%d: %d %d\n",t,ret,res);
    }
	return 0;
}
