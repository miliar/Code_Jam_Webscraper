#include<stdio.h>
#include<cstring>
#include<algorithm>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T, P, N, G[102], M[5], cases,i ,j;
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++){
	    scanf("%d%d",&N,&P);
	    memset(M,0,sizeof(M));
	    for(i=1;i<=N;i++){
	        scanf("%d",&G[i]);
	        M[G[i]%P]++;
	    }
		
		int an=0;
	if(P==2){
	    an = M[0] + M[1]/2 + M[1]%2;
	}
	else if(P==3){
	    int m = min(M[1],M[2]);
	    an = M[0] + m;
	    M[1]-=m;
	    M[2]-=m;
	    an += M[1]/3;
	    an += M[2]/3;
	    if(M[1]%3)an++;
	    if(M[2]%3)an++;
	}
	else if(P==4){
	    int m = min(M[1],M[3]);
	    an = M[0] + m;
	    M[1]-=m;
	    M[3]-=m;
	    an += M[2]/2;
		M[2]%=2;
		if(M[2]){
		    if(M[1]>2){
		        an++;
		        M[1]-=2;
		        M[2]=0;
		    }
		    if(M[3]>2){
		        an++;
		        M[3]-=2;
		        M[2]=0;
		    }
		}
	    an += M[1]/4;
	    an += M[3]/4;
	    if(M[1]%4)an++;
	    else if(M[3]%4)an++;
	    else if(M[2])an++;
		

	}
	
	printf("Case #%d: %d\n",cases, an);
	}
	
	
    return 0;
} 
