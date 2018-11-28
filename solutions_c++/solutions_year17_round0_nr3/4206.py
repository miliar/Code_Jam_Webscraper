#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
int t,n,k,j,l,c,m,i,n1,n2,m1,m2,mi;
int min(int a,int b){return a<b?a:b;}
int max(int a,int b){return a>b?a:b;}
struct kk
{
  int max1,max2,maxi,l,r;
};

struct Comp{
    bool operator()(const kk& A, const kk& B){
        return (A.max1<B.max1)||(A.max2<B.max2&&A.max1==B.max1)||(A.max2==B.max2&&A.max1==B.max1&&A.maxi>B.maxi);
    }
};

priority_queue<kk, vector<kk>, Comp> q;

int main()
{
  freopen("c.out","w",stdout);
  scanf("%d",&t);
  for (int kase=1;kase<=t;kase++)
  {
    while (!q.empty()) q.pop();
    scanf("%d%d",&n,&k);
    m1=-2;m2=-2;mi=0;
    c=(n+2)/2-1;
    for (m=1;m<=3;m++)
    {
	  n1=min(c,n+1-c)-1;
	  if (n1<m1) continue;
	  n2=max(c,n+1-c)-1;
	  if (n1>m1) {m1=n1;m2=n2;mi=c;}
	  else 
	  {
	    if (n2<m2) continue;
	    if (n2>m2) {m2=n2;mi=c;}
	    else if (c<mi) {mi=c;}
	  }
	  c++;
    }
    kk a;
    a.l=0;a.r=n+1;a.max1=m1;a.max2=m2;a.maxi=mi;
    q.push(a);
    for (i=1;i<k;i++)
    {
      kk a=q.top(); 
      q.pop();
      if (a.l+1<a.maxi)
      {
	 m1=-2;m2=-2;mi=0;
        c=(a.l+a.maxi+1)/2-1;
        for (m=1;m<=3;m++)
        {
	  n1=min(c-a.l,a.maxi-c)-1;
	  if (n1<m1) continue;
	  n2=max(c-a.l,a.maxi-c)-1;
	  if (n1>m1) {m1=n1;m2=n2;mi=c;}
	  else 
	  {
	    if (n2<m2) continue;
	    if (n2>m2) {m2=n2;mi=c;}
	    else if (c<mi) {mi=c;}
	  }
	  c++;
        }
        kk b;
	b.l=a.l;b.r=a.maxi;b.max1=m1;b.max2=m2;b.maxi=mi;
	q.push(b);
      }
      if (a.maxi+1<a.r)
      {
	m1=-2;m2=-2;mi=0;
        c=(a.maxi+a.r+1)/2-1;
        for (m=1;m<=3;m++)
        {
	  n1=min(c-a.maxi,a.r-c)-1;
	  if (n1<m1) continue;
	  n2=max(c-a.maxi,a.r-c)-1;
	  if (n1>m1) {m1=n1;m2=n2;mi=c;}
	  else 
	  {
	    if (n2<m2) continue;
	    if (n2>m2) {m2=n2;mi=c;}
	    else if (c<mi) {mi=c;}
	  }
	  c++;
        }
        kk b;
	b.l=a.maxi;b.r=a.r;b.max1=m1;b.max2=m2;b.maxi=mi;
	q.push(b);
      }
    }
    kk b=q.top();
    printf("Case #%d: %d %d\n",kase,b.max2,b.max1);
  }
  fclose(stdout);
}
