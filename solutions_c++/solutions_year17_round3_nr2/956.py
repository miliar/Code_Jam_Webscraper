#include<bits/stdc++.h>
using namespace std;
struct P{
	int s,e;
}C[100],J[100];
bool comp(P aa,P bb){
	return aa.s!=bb.s?aa.s<bb.s:aa.e>bb.e;
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int n,m;
		scanf("%d%d",&n,&m);
		for(int j=0;j<n;j++)scanf("%d%d",&C[j].s,&C[j].e);sort(C,C+n,comp);
		for(int j=0;j<m;j++)scanf("%d%d",&J[j].s,&J[j].e);sort(J,J+m,comp);
		if(n+m==1)printf("Case #%d: %d\n",i+1,2);
		else{
			if(n==2){
				if(C[1].e-C[0].s<=720||1440-C[1].s+C[0].e<=720)printf("Case #%d: %d\n",i+1,2);
				else printf("Case #%d: %d\n",i+1,4);
			}
			else if(m==2){
				if(J[1].e-J[0].s<=720||1440-J[1].s+J[0].e<=720)printf("Case #%d: %d\n",i+1,2);
				else printf("Case #%d: %d\n",i+1,4);
			}
			else{
				printf("Case #%d: %d\n",i+1,2);
			}
		}
	}
}
/*#include<bits/stdc++.h>
using namespace std;
struct P{
	int s,e;
}C[100],J[100];
int BS(int S,int E){
	if(S==E)return S;
	int m=(S+E)/2;

}
bool comp(P aa,P bb){
	return aa.s!=bb.s?aa.s<bb.s:aa.e>bb.e;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int n,m;
		scanf("%d%d",&n,&m);
		for(int j=0;j<n;j++)scanf("%d%d",&C[j].s,&C[j].e);sort(C,C+n,comp);
		for(int j=0;j<m;j++)scanf("%d%d",&J[j].s,&J[j].e);sort(J,J+m,comp);
		printf("Case #%d: %d",i+1,BS(2,1440));
	}
}*/
