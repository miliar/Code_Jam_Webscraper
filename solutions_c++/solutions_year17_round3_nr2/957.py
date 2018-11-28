#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define F(i,n) for(int i=1; i<=n; i++)
#define s first
#define e second
typedef pair<int,int> P;

int Ac, Aj;
P C[105], J[105];
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	printf("Case #%d: ",cases);
    	scanf("%d %d",&Ac,&Aj);
    	F(i, Ac) scanf("%d %d",&C[i].s,&C[i].e);
    	F(i, Aj) scanf("%d %d",&J[i].s,&J[i].e);
    	
    	sort(C+1, C+1+Ac);
    	sort(J+1, J+1+Aj);
    	
    	if((Ac==1 && Aj==0) || (Ac==0 && Aj==1)) {	printf("2\n");	continue;}
    	if(Ac==2){
    		if(C[2].e-C[1].s<=720 || C[1].e+1440-C[2].s<=720) printf("2\n");
			else printf("4\n");
			continue;
		}
		if(Aj==2){
			if(J[2].e-J[1].s<=720 || J[1].e+1440-J[2].s<=720) printf("2\n");
			else printf("4\n");
			continue;
		}
		printf("2\n");
	}
    return 0;
}
