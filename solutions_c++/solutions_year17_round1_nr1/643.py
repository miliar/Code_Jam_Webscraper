#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair
#define var(x) cerr << #x << " = " << x << endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

string s[33];
int vis[33];

int main() {
    int N;
    cin >> N;
    for(int n=1;n<=N;n++) {
        int r, c;
        printf("Case #%d:\n", n);
        cin >> r >> c;
        for(int i=0;i<r;i++) cin >> s[i];
        memset(vis,0,sizeof(vis));
        while(1) {
            int a = 0, ax=-1, ay=-1;
            int vx, vy, vxl=r, vyl=c;
            char v;
            int e = 0;
            for(int i=0;i<r;i++) {
                for(int j=0;j<c;j++) {
                    if(s[i][j] == '?' && !a) {
                        a = 1;
                        ax = i;
                        ay = j;
                    }
                    if(s[i][j] != '?' && !vis[s[i][j]-'A']) {
                        e = 1;
                        v = s[i][j];
                        vis[v-'A'] = 1;
                        if(ax == -1) ax = i;
                        if(ay == -1) ay = j;
                        vx = i;
                        vy = j;
                        break;
                    }
                }
                if(e) break;
            }
            if(!e) break;
            for(int i=vy+1;i<c;i++) {
                if(s[vx][i] != '?' && s[vx][i] != v) {
                    vyl = i;
                    break;
                }
            }
            int f = 0;
            for(int i=ax;i<r;i++) {
                for(int j=ay;j<vyl;j++) {
                    if(s[i][j] != v && s[i][j] != '?') {
                        f = 1;
                        vxl = i;
                        break;
                    }
                }
                if(f) break;
            }
            for(int i=ax;i<vxl;i++) {
                for(int j=ay;j<vyl;j++) s[i][j] = v;
            }
        }
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) cout << s[i][j];
            cout << endl;
        }
    }
    return 0;
}

