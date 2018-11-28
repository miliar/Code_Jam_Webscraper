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
 
int kase;
void solve() {
    int aH,aS,bH,bS,B,D;
    read(aH);read(aS);read(bH);read(bS);read(B);read(D);
    int res=(int)(1e9);
    REP(u,0,bS) REP(v,0,bH) {
        int ah=aH,as=aS,bh=bH,bs=bS;
        int cnt=0,fl=1;
        REP(i,1,u) {
            if(max(0,bs-D)>=ah) {
                ++cnt;ah=aH;ah=max(0,ah-bs);
                if(ah<=0) {
                    fl=0;break;
                }
            } 
            bs=max(bs-D,0);ah=max(0,ah-bs);++cnt;
            if(ah<=0) {
                fl=0;break;
            }
        }
        if(!fl) continue;
        REP(i,1,v) {
            if(bs>=ah) {
                ++cnt;ah=aH;ah=max(0,ah-bs);
                if(ah<=0) {
                    fl=0;break;
                }
            }
            as+=B;ah=max(0,ah-bs);++cnt;
            if(ah<=0) {
                fl=0;break;
            }
        }
        if(!fl) continue;
        while(bh) {
            if(as>=bh) {
                ++cnt;bh=max(0,bh-as);break;
            }
            if(bs>=ah) {
                ++cnt;ah=aH;ah=max(0,ah-bs);
                if(ah<=0) {
                    fl=0;break;
                }
            }
            bh=max(0,bh-as);ah=max(0,ah-bs);++cnt;
            if(ah<=0) {
                fl=0;break;
            }
        }
        if(!fl) continue;
        res=min(res,cnt);
    } 
    printf("Case #%d: ",++kase);
    if(res==(int)(1e9)) printf("IMPOSSIBLE\n"); else printf("%d\n",res);
}

int main() {
    int T;
    read(T);
    while(T--) solve();
    return 0;
}