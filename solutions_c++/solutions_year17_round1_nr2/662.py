#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>

const int mod=1000000007;

using namespace std;

int t;
int n, p;
int r[60];
int q[60][60];
bool used[60][60];

struct bounder
{
    int down;
    int up;
};

bounder findBounder(int Q, int R)
{
    bounder ret;
    double cur=(double)Q/(double)R;
    int d=cur/1.1-1;
    int u=cur/0.9-1;
    for(int i=0;i<5;i++){
        if(d*11*R>=Q*10){
            ret.down=d;
            break;
        }
        d++;
    }
    for(int i=0;i<5;i++){
        if(u*9*R<=Q*10){
            ret.up=u;
        }
        u++;
    }
    if(ret.down>ret.up){
        ret.down=ret.up=-1;
    }
    return ret;
}

bounder intersect(bounder A, bounder B)
{
    bounder ret;
    if(A.down<B.down) ret.down=B.down;
    else ret.down=A.down;
    if(A.up>B.up) ret.up=B.up;
    else ret.up=A.up;
    if(ret.down>ret.up){
        ret.down=ret.up=-1;
    }
    return ret;
}

bool dfs(int down, int up, int deep)
{
    //printf("%d %d %d\n", down, up, deep);
    if(down>up||down<0) return 0;
    if(deep>=n) return 1;
    for(int i=0;i<p;i++){
        if(used[deep][i]) continue;
        used[deep][i]=1;
        bounder bd=findBounder(q[deep][i], r[deep]);
        if(bd.down>up){
            used[deep][i]=0;
            return 0;
        }
        bounder now;
        now.down=down;
        now.up=up;
        bd=intersect(bd, now);
        if(bd.down>0&&dfs(bd.down, bd.up, deep+1)) return 1;
        used[deep][i]=0;
    }
    return 0;
}

int main()
{
	/*int Q, R;
	while(scanf("%d %d", &Q, &R)!=EOF){
        bounder ans=findBounder(Q, R);
        printf("%d %d\n", ans.down, ans.up);
	}*/
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cases=1;cases<=t;cases++){
        scanf("%d %d", &n, &p);
        for(int i=0;i<n;i++) scanf("%d", &r[i]);
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++) scanf("%d", &q[i][j]);
        }
        for(int i=0;i<n;i++) sort(q[i], q[i]+p);
        memset(used, 0, sizeof(used));
        int ans=0;
        for(int i=0;i<p;i++){
            //printf("q %d r %d\n", q[0][i], r[0]);
            bounder bd=findBounder(q[0][i], r[0]);
            used[0][i]=1;
            if(dfs(bd.down, bd.up, 1)) ans++;
        }
        printf("Case #%d: %d\n", cases, ans);
	}
}
