#include<stdio.h>
#include<string.h>


int test,heap[1000000],num;

void myswap(int *x, int *y);
void up_heap(int a);
void down_heap(int a);
int heap_solve(int n,int k);



int main()
{

    int n,k,i,j,a,b,c;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&test);


    for(i=1;i<=test;i++){
        scanf("%d %d",&n,&k);
        a=heap_solve(n,k);

        b=a/2;
        if(a%2==0)
            a=b-1;
        else a=b;

        printf("Case #%d: %d %d\n",i,b,a);
    }
    return 0;
}



void myswap(int *a, int *b){
    int tp;

    tp=*a; *a=*b; *b=tp;
}

void up_heap(int a){
    while(a>1){
        if(heap[a/2]>=heap[a]) return;
        myswap(&heap[a/2],&heap[a]);
        a /=2;
    }
}

void down_heap(int a){
    int b;
    while(1){
        b=a*2;
        if(b>num)
            return;

        if(b<num && heap[b]<heap[b+1])
         b++;
        if(heap[a]>=heap[b])
            return;

        myswap(&heap[a], &heap[b]);
        a=b;
    }
}


int heap_solve(int n,int k){
    int i,x,y;

    num=1;
    heap[num]=n;

    for(i=0;i<k-1;i++){
        if(heap[1]==1){
            return 1;
        }

        y=x=heap[1]/2;

        if(heap[1]%2==0) y--;

        heap[1]=x;
        down_heap(1);

        heap[++num]=y;
        up_heap(num);
    }

    return heap[1];

}



