
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned ll
#define db double
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define PII pair<int, int>

const string INPUT_FILE = "input.txt";
const string OUTPUT_FILE = "a.txt";

int t,r,c;
char buf[30][30];
int lt[30],rt[30],u[30],d[30];

void init() {
    memset(buf,0,sizeof(buf));
    for (int i=0;i<30;i++) {
        lt[i]=100;
        u[i]=100;
        rt[i]=-1;
        d[i]=-1;
    }
}

void update(int i,int j,char c) {
    if (c!='?') {
        lt[c-'A']=min(lt[c-'A'],j);
        rt[c-'A']=max(rt[c-'A'],j);
        u[c-'A']=min(u[c-'A'],i);
        d[c-'A']=max(d[c-'A'],i);        
    }
}

bool check(int l,int r,int u,int d) {
    for (int x=u;x<=d;x++) {
        for (int y=l;y<=r;y++) {
            if (buf[x][y]!='?') {
                return false;
            }
        }
    }
    return true;
}

void fill(int l,int r,int u,int d,char c) {
    for (int x=u;x<=d;x++) {
        for (int y=l;y<=r;y++) {
            buf[x][y]=c;
        }
    }
}

void work() {
    for (int i=0;i<26;i++) {
        if (lt[i]!=100) {
            fill(lt[i],rt[i],u[i],d[i],i+'A');
        }
    }
    // row extension
    for (int i=0;i<26;i++) {
        if (lt[i]!=100) {
            for (int y=lt[i]-1;y>=0;y--) {
                if (check(y,y,u[i],d[i])) {
                    lt[i]=y;
                    fill(y,y,u[i],d[i],i+'A');
                } else {
                    break;
                }
            }
            for (int y=rt[i]+1;y<c;y++) {
                if (check(y,y,u[i],d[i])) {
                    rt[i]=y;
                    fill(y,y,u[i],d[i],i+'A');
                } else {
                    break;
                }
            }
        }
    }
    // col extension
    for (int i=0;i<26;i++) {
        if (lt[i]!=100) {
            for (int x=u[i]-1;x>=0;x--) {
                if (check(lt[i],rt[i],x,x)) {
                    u[i]=x;
                    fill(lt[i],rt[i],x,x,i+'A');
                } else {
                    break;
                }
            }
            for (int x=d[i]+1;x<r;x++) {
                if (check(lt[i],rt[i],x,x)) {
                    u[i]=x;
                    fill(lt[i],rt[i],x,x,i+'A');
                } else {
                    break;
                }
            }
        }
    }
}

int main() {

    freopen(INPUT_FILE.c_str(), "r", stdin);
    freopen(OUTPUT_FILE.c_str(), "w", stdout);

    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++) {
        init();
        scanf("%d%d",&r,&c);
        for (int i=0;i<r;i++) {
            scanf("%s",buf[i]);
        }
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                update(i,j,buf[i][j]);
            }
        }
        work();
        printf("Case #%d:\n",tt);
        for (int i=0;i<r;i++) {
            printf("%s\n",buf[i]);
        }
    }
}