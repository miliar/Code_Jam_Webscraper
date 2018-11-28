#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define repp(a,b,c,d) for(int a=b; a<=c; a+=d)
#define rep(a,b,c) repp(a,b,c,1)
#define revv(a,b,c,d) for(int a=b; a>=c; a-=d)
#define rev(a,b,c) revv(a,b,c,1)
typedef long long ll;

ll n,pp;
ll dat[200005];
int cnt;
struct tdata{
	int num;
	struct tdata *next;
}*head;

bool isEmpty()
{
	if(head==NULL) return true;
	return false;
}

void push(int x)
{
	struct tdata *node=(struct tdata*)malloc(sizeof(struct tdata));
	node->num=x;
	node->next=NULL;
	if(isEmpty())
	{
		head=node;
	}
	else
	{
		struct tdata *curr=head;
		while(curr->next!=NULL && curr->num > node->num) curr=curr->next;
		if(curr==head && curr->num < node->num)
		{
			node->next=curr;
			head=node;
		}
		else
		{
			node->next=curr->next;
			curr->next=node;
		}
	}
	cnt++;
}

int front()
{
	return head->num;
}

int size()
{
	return cnt;
}
void pop()
{
	if(size()==1)
	{
		head=NULL;
	}
	else
	{
		head=head->next;
	}
	cnt--;
}

void reset()
{
	while(!isEmpty()) pop();
}

int main()
{
	int t,tmp;
	scanf("%d",&t);
	rep(tc,1,t)
	{
		scanf("%lld %lld",&n,&pp);
		reset();
		cnt=0;
		push(n);
		rep(i,1,pp)
		{
			tmp=front()/2;
			dat[i*2-1]=tmp;
			if(front()%2==0 && front()>0) dat[i*2]=tmp-1;
			else dat[i*2]=tmp;
			push(dat[i*2-1]);
			push(dat[i*2]);
			pop();
		}
		printf("Case #%d: %d %d\n",tc,dat[pp*2-1],dat[pp*2]);
	}
	return 0;
}
