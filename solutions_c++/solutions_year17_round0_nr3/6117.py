#include<cstdio>
#include <iostream>
#define N 1000000

using namespace std;

int t,heap[N],hn;

void myswap(int &x, int &y){
    int tp;

    tp=x; x=y; y=tp;
}

void upheap(int x){
    while(x>1){
        if(heap[x/2]>=heap[x]) return;
        myswap(heap[x/2],heap[x]);
        x /=2;
    }
}

void downheap(int x){
    int y;
    while(1){
        y=x*2;
        if(y>hn) return;
        if(y<hn && heap[y]<heap[y+1]) y++;
        if(heap[x]>=heap[y]) return;
        myswap(heap[x], heap[y]);
        x=y;
    }
}


int solve(int n,int k){
    int i,x,y;

    hn=1;
    heap[hn]=n;

    for(i=0;i<k-1;i++){
        if(heap[1]==1){
            return 1;
        }

        y=x=heap[1]/2;
        if(heap[1]%2==0) y--;

        heap[1]=x;
        downheap(1);
        heap[++hn]=y;
        upheap(hn);
    }

    return heap[1];

}

int main()
{
    int i,j,k,x,y,n;

    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    scanf("%d",&t);

    for(i=1;i<=t;i++){
        scanf("%d %d",&n,&k);
        x=solve(n,k);
        y=x/2;
        if(x%2==0) x=y-1;
        else x=y;

        printf("Case #%d: %d %d\n",i,y,x);
    }
    return 0;
}
