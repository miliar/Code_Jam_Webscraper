#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int gap(int N,int K)
{
    if (K==0) return N;
    int left,right;
    if (N%2==1){
        left=right=(N-1)/2;
    }else{
        right=N/2;
        left=right-1;
    }
    K--;
    if (K%2==0){
        return max(gap(left,K/2),gap(right,K/2));
    }else{
        return max(gap(left,K/2),gap(right,K/2+1));
    }
}
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C_output_small_1.txt","w",stdout);
    int T,N,K;
    scanf("%d",&T);
    int left,right;
    for (int index=1;index<=T;index++)
    {
        scanf("%d%d",&N,&K);
        int W=gap(N,K-1);
        if (W%2==1){
            left=right=(W-1)/2;
        }else{
            right=W/2;
            left=right-1;
        }
        printf("Case #%d: %d %d\n",index,right,left);
    }
    return 0;
}
