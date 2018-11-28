#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
bool b[1111];
int L[1111],R[1111];
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        memset(b,false,sizeof b);
        printf("Case #%d: ",_tc);
        int N,K;
        scanf("%d %d",&N,&K);
        int mnLR, mxLR, idx;
        for ( int i = 0 ; i < K ; i++ ) {
            memset(L,0,sizeof L);
            memset(R,0,sizeof R);
            for ( int j = 1 ; j <= N ; j++ ) {
                if ( b[j] ) continue;
                for ( int k = j-1 ; k >= 1 ; k-- ) {
                    if ( b[k] ) break;
                    L[j]++;
                }
                for ( int k = j+1 ; k <= N ; k++ ) {
                    if ( b[k] ) break;
                    R[j]++;
                }
            }
            mnLR=-1, mxLR=-1, idx=0;
            for ( int j = 1 ; j <= N ; j++ ) {
                if ( mnLR < min(L[j],R[j]) ) {
                    mnLR = min(L[j],R[j]);
                    mxLR = max(L[j],R[j]);
                    idx = j;
                } else if ( mnLR == min(L[j],R[j]) ) {
                    if ( mxLR < max(L[j],R[j]) ) {
                        mnLR = min(L[j],R[j]);
                        mxLR = max(L[j],R[j]);
                        idx = j;
                    }
                }
            }
            b[idx] = true;
        }
        printf("%d %d\n",mxLR, mnLR);
    }
    return 0;
}
