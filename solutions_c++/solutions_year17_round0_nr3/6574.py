#include<cstdio>
#include<algorithm>
#include<queue>

using namespace std;

struct przedzial{
	int begin,end;
	przedzial(int b,int e):begin(b),end(e){}
};

bool operator<(przedzial A,przedzial B){
	int a=A.end-A.begin,b=B.end-B.begin;
	if(a<b)return true;
	if(a==b)return A.begin<B.begin;
	return false;
}

void f(int cnr){
	int n,k;
	scanf("%d%d",&n,&k);
	priority_queue<przedzial> Q;
//	printf("%d %d\n",Q.top().begin,Q.top().end);
	int r,l;
	Q.push(przedzial(0,n-1));
	for(int i=0;i<k;i++){
		int b=Q.top().begin,e=Q.top().end;
		Q.pop();
		int s=(b+e)/2;
		l=s-b;
		r=e-s;
		//printf("(%d %d), l: %d r: %d)
		if(s>b)Q.push(przedzial(b,s-1));
		if(s<e)Q.push(przedzial(s+1,e));
	}
	printf("Case #%d: %d %d\n",cnr,max(l,r),min(l,r));
}

main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++)f(i);
}
