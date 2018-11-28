#include <bits/stdc++.h>
using namespace std;
#define max 1000000
struct btree{
      long long data;
      struct btree *b1,*b2;
};
struct btree *head,*other,**queue;
long long k;
struct btree** createQueue(int *front, int *rear)
{
    struct btree **queue =
        (struct btree **)malloc(sizeof(struct btree*)*max);

    *front = *rear = 0;
    return queue;
}
void enQueue(struct btree **queue, int *rear, struct btree *new_node)
{
    queue[*rear] = new_node;
    (*rear)++;
}
struct btree *deQueue(struct btree **queue, int *front,int* rear)
{
    struct btree *temp=((struct btree*)malloc(sizeof(struct btree)));
    long long max1=queue[*front]->data;
    int maxi=*front;
    for(long long i=*front+1;i<*rear;i++)
    {
    if(max1<queue[i]->data)
    {
        max1=queue[i]->data;
        maxi=i;
    }
    }
    temp=queue[*front];
    queue[*front]=queue[maxi];
    queue[maxi]=temp;
    (*front)++;
    return queue[*front - 1];
}
void cmp(struct btree* h)
{
    long long l,r;
    k--;
    head=h;
    int front,rear;
    struct btree **queue = createQueue(&front, &rear);
    while(k--)
    {
    struct btree *bt1,*bt2;
    bt1=(struct btree*)malloc(sizeof(struct btree));
    bt2=(struct btree*)malloc(sizeof(struct btree));
    head->b1=bt1;
    head->b2=bt2;
    if(head->data%2!=0||head->data==0)
    {
        bt1->data=head->data/2;
        bt2->data=head->data/2;
    }
    else
    {
        bt1->data=head->data/2-1;
        bt2->data=head->data/2;
    }
    enQueue(queue, &rear, bt2);
    enQueue(queue, &rear, bt1);
    head = deQueue(queue, &front, &rear);
    }
    struct btree *bt1,*bt2;
    bt1=(struct btree*)malloc(sizeof(struct btree));
    bt2=(struct btree*)malloc(sizeof(struct btree));
    head->b1=bt1;
    head->b2=bt2;
    if(head->data%2!=0||head->data==0)
    {
        bt1->data=head->data/2;
        bt2->data=head->data/2;
    }
    else
    {
        bt1->data=head->data/2-1;
        bt2->data=head->data/2;
    }
    cout<<bt2->data<<" "<<bt1->data<<endl;
        return;
}
int main()
{
    std::ios::sync_with_stdio(false);
    freopen("a.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    long long n;
    cin>>t;
    for(int lc=1;lc<=t;lc++)
    {
        struct btree *h;
        h=(struct btree*)malloc(sizeof(struct btree));
        cin>>n>>k;
        h->data=n;
        h->b1=NULL;
        h->b2=NULL;
        cout<<"Case #"<<lc<<": ";
        cmp(h);
    }

    return 0;
}
