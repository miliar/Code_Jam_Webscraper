/*************************************************************************
 > File Name: A.cpp
 > Author: makeecat
 ************************************************************************/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
const int maxn = 1010;
int T,D,N;
int K[maxn],S[maxn];
double t[maxn];
struct node{
	int K,S;
	bool operator <(const node&rhs)const{
		return (K<rhs.K ||(K==rhs.K && S<rhs.S));
	}
}a[maxn];

int main(){
	//freopen("A.in","r",stdin);
	scanf("%d",&T);
	for (int kase=1;kase<=T;kase++){
		double ans=0;
		scanf("%d%d",&D,&N);
		for (int i=0;i<N;i++){
			scanf("%d%d",&a[i].K,&a[i].S);
			//t[i]=(double)(D-K[i])/(double)(S[i]);
		}
		sort(a,a+N);
		double tmp = double(D-a[N-1].K)/double(a[N-1].S);
		for (int i=N-2;i>=0;i--){
			tmp = max(double(D-a[i].K)/(double)(a[i].S),tmp);
		}

		printf("Case #%d: %.7lf\n",kase,(double)(D)/tmp);
	}
	return 0;
}
