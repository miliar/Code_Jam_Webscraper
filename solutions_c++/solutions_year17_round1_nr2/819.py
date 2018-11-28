#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int N, P;
int n[55];
int nind[55];
int ans;

class NP{
public:
    int mn, mx;
    NP( int _mn = 0, int _mx = 0): mn(_mn), mx(_mx) {}
}np[55][55];

bool cmp( NP n1, NP n2) {
    if ( n1.mn != n2.mn ) return n1.mn < n2.mn;
    return n1.mx < n2.mx;
}

bool check() {
    for (int i = 0; i < N; ++i) {
        if (nind[i] >= P)
            return false;
    }
    return true;
}


bool checklegal() {
    int minr = 0;
    int l = np[0][nind[0]].mn, r = np[0][nind[0]].mx;
    for (int i = 1; i < N; ++i) {
        l = max(l,np[i][nind[i]].mn);
        r = min(r,np[i][nind[i]].mx);
        if (np[minr][nind[minr]].mx > np[i][nind[i]].mx)
            minr = i;
    }
    //printf("---%d %d\n",l,r);
    if (l > r) {
        ++nind[minr];
        return false;
    }
    for (int i = 0; i < N; ++i)
        ++nind[i];
    ++ans;
    return true;
}



void solve() {
    int k;
    scanf("%d%d",&N,&P);
    for (int i = 0; i < N; ++i) {
        scanf("%d",&n[i]);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            scanf("%d",&k);
            np[i][j] = NP( (int)ceil((double)k*100.0/110/n[i]), (int)floor((double)k*100.0/90/n[i]) );
        }
        sort(np[i],np[i]+P, cmp);
    }
    memset(nind,0,sizeof(nind));
    ans = 0;
    while(check() == true) {
        checklegal();
    }
    printf("%d\n",ans);
}


int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
}
