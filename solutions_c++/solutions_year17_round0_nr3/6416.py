#include<cstdio>
#include<queue>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

typedef long long LL;

struct QST{
	LL len,num;
	QST(LL LEN=0,LL NUM=0) {len=LEN, num=NUM;}
};
bool operator < (const QST &a,const QST &b) {return a.len<b.len;}

LL n,k;

priority_queue<QST> Q;
int T;
int main()
{
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%I64d %I64d",&n,&k);
		
		while (!Q.empty()) Q.pop();
		Q.push(QST(n,1));
		while (k)
		{
			QST tp=Q.top(); Q.pop();
			while (!Q.empty() && Q.top().len==tp.len)
			{
				QST t1=Q.top(); Q.pop();
				tp.num+=t1.num;
			}
			
			LL lmin=(tp.len-1)/2, lmax=tp.len-1-lmin;
			
			if (tp.num>=k) printf("%I64d %I64d\n",lmax,lmin), k=0;
				else k-=tp.num;
			
			Q.push(QST(lmax,tp.num));
			Q.push(QST(lmin,tp.num));
		}
	}
}