#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <bitset>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <iostream>
#include <algorithm>
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define PER(i,a,b) for(int i=(a);i>=(b);i--)
#define RVC(i,S) for(int i=0;i<(S).size();i++)
#define RAL(i,u) for(int i=fr[u];i!=-1;i=e[i].next)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
    
template<class T> inline
void read(T& num) {
    bool start=false,neg=false;
    char c;
    num=0;
    while((c=getchar())!=EOF) {
        if(c=='-') start=neg=true;
        else if(c>='0' && c<='9') {
            start=true;
            num=num*10+c-'0';
        } else if(start) break;
    }
    if(neg) num=-num;
}
/*============ Header Template ============*/

char s[55][55];
int b[55];
int kase;

void solve() {
    int n,m;
    read(n);read(m);
    memset(b,0,sizeof(b));
    REP(i,1,n) {
        scanf("%s",s[i]+1);
        REP(j,1,m) if(s[i][j]!='?') b[i]=1;
    }
    REP(i,1,n) if(b[i]) {
        int ps=0;char c;
        REP(j,1,m) if(s[i][j]!='?') {
            REP(k,1,j-1) s[i][k]=s[i][j];
            ps=j+1;c=s[i][j];break;
        }
        REP(j,ps,m) if(s[i][j]!='?') c=s[i][j]; else s[i][j]=c;
    }
    int pt=0,now=0;
    REP(i,1,n) if(b[i]) {
        REP(j,1,i-1) REP(k,1,m) s[j][k]=s[i][k];pt=i+1;now=i;break;
    }
    REP(i,pt,n) if(b[i]) now=i; else {
        REP(j,1,m) s[i][j]=s[now][j];
    }
    printf("Case #%d:\n",++kase);
    REP(i,1,n) printf("%s\n",s[i]+1);
}

int main() {
    int T;
    read(T);
    while(T--) solve();
    return 0;
}
 