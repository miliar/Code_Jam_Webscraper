#include<stdio.h>
#include<stdlib.h>
#include<stack>
#include<queue>
#include<vector>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define F(i,L,R) for(int i=L;i<R;i++)
#define FE(i,L,R) for(int i=L;i<=R;i++)
#define RF(i,l,r) for(int i=r;i>l;i--)
#define RFE(i,l,r) for(int i=r;i>=l;i--)
#define getI(i) scanf("%d",&i)
#define getII(i,j) scanf("%d%d",&i,&j)
#define getIII(i,j,k) scanf("%d%d%d",&i,&j,&k)
#define VgetI(i) int (i);scanf("%d",&(i));
#define VgetII(i,j) int (i),(j);scanf("%d%d",&(i),&(j));
#define VgetIII(i,j,k) int (i),(j),(k);scanf("%d",&(i),&(j),&(k));
#define EoF(n) int(n);while(~getI(n))
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define abs(n) (n>0?n:(-n))
#define INF 2147483647
#define nINF -2147483648
bool test(int n){
	stack<int> s;
	while(n/10){
		s.push(n%10);
		n/=10;
	}
	s.push(n);
	while(!s.empty()){
		//printf("%d ",s.top());
		int now=s.top();
		s.pop();
		if(!s.empty()&&now>s.top()) return 0;
	}
	return 1;
}
int main(){
	freopen("D:\\Roland\\2program\\cpp\\B-small.in","r",stdin);
	freopen("D:\\Roland\\2program\\cpp\\B-small.out","w",stdout);
	VgetI(t);
	FE(cases,1,t){
		VgetI(n);
		printf("Case #%d: ",cases);
		if(test(n)){
			printf("%d\n",n);
			continue;
		}
		while(n--){
			//printf("%d:",n);
			if(test(n)){
				printf("%d\n",n);
				break;
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
}

