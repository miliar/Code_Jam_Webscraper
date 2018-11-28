#include <bits/stdc++.h>

using namespace std;

typedef pair<long long, long long> PII;
typedef pair<PII,PII> PIIII;

long long t,tes,ans,i,j,n,m,x,xxx;
long long a[107][107];
long long b[107],pos[107];
bool success;

PII itung(long long index, long long cap) {
    long long kiri,kanan;
    
    long long base = 0;
    long long top = 2000000;
    while (base != top) {
        long long mid = (base + top) / 2;
        if (100 * cap <= 110 * b[index] * mid) top = mid; else base = mid+1;
    }
    kiri = top;
    
    base = 0;
    top = 2000000;
    while (base != top) {
        long long mid = (base + top) / 2 + 1;
        if (90 * b[index] * mid <= 100 * cap) base = mid; else top = mid-1;
    }
    kanan = top;
    
    return PII(kiri,kanan);
}

int main() {
    scanf("%lld",&t);
    for (tes=1 ; tes<=t ; tes++) {
        scanf("%lld%lld",&n,&m);
        for (i=0 ; i<n ; i++) scanf("%lld",&b[i]);
        for (i=0 ; i<n ; i++) {
            for (j=0 ; j<m ; j++) {
                scanf("%lld",&a[i][j]);
            }
            sort(a[i],a[i]+m);
        }
        
        ans = 0;
        for (i=0 ; i<n ; i++) pos[i] = 0;
        
        x = 1;
        success = true;
        while (success) {
            for (i=0 ; i<n ; i++) {
                while (pos[i] != m) {
                    PII tmp = itung(i,a[i][pos[i]]);
                    //printf("%d %d : %d %d\n",i,pos[i],tmp.first,tmp.second);
                    if (tmp.second < x) pos[i]++; else break;
                }
                if (pos[i] == m) success = false;
            }
            
            if (success) {
                for (i=0 ; i<n ; i++) {
                    PII tmp = itung(i,a[i][pos[i]]);
                    if (tmp.first > x || x > tmp.second) success = false;
                }
                if (success) {
                    for (i=0 ; i<n ; i++) pos[i]++;
                    ans++;
                } else {
                    x++;
                }
                
                success = true;
            }
            //printf("%d %d\n",x,success);
            if (x >= 2000000) success = false;
        }
        
        printf("Case #%lld: %lld\n",tes,ans);
    }
}
