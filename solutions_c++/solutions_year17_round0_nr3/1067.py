#include<bits/stdc++.h>
using namespace std;

pair<long long,long long> l[1000005];

void f(int& j,long long n,long long k){
	if(l[j].first==n) l[j].second+=k;
	else l[++j]=make_pair(n,k);
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,_,i,j;
	long long n,m,n1,n2,k;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%I64d%I64d",&n,&m);
		l[0]=make_pair(n,1),i=j=0;
		while(m>0){
			n=l[i].first-1,k=l[i].second;
			m-=k,n1=(n+1)/2,n2=n/2,i++;
			f(j,n1,k);f(j,n2,k);
		}
		printf("Case #%d: %I64d %I64d\n",_,n1,n2),
		fprintf(stderr,"Case #%d: %I64d %I64d\n",_,n1,n2);
	}
	return 0;
}
