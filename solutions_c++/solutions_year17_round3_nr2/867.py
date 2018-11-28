#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
	int ac,aj;
	int c[100];
	int d[100];
	int j[100];
	int k[100];
	scanf("%d%d",&ac,&aj);
	for(int i=0;i<ac;i++){
	    scanf("%d%d",c+i,d+i);
	}
	for(int i=0;i<aj;i++){
	    scanf("%d%d",j+i,k+i);
	}
	if(ac == 1 || aj == 1){
	    printf("Case #%d: 2\n",t);
	}
	else if(ac == 2){
	    int t1 = 60*24 - max(c[0],c[1]) + min(d[0],d[1]);
	    int t2 = - min(c[0],c[1]) + max(d[0],d[1]);
	    if (t1 <= 30*24 || t2 <= 30 *24)
		printf("Case #%d: 2\n",t);
	    else
		printf("Case #%d: 4\n",t);
	}
	else{
	    int t1 = 60*24 - max(j[0],j[1]) + min(k[0],k[1]);
	    int t2 = - min(j[0],j[1]) + max(k[0],k[1]);
	    if (t1 <= 30*24 || t2 <= 30 *24)
		printf("Case #%d: 2\n",t);
	    else
		printf("Case #%d: 4\n",t);
	}

    }
    return 0;
}
