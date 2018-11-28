#include<iostream>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int c,j;
		int ac[102][2],aj[102][2];
		scanf("%d %d",&c,&j);
		for(int i=0;i<c;++i)
			scanf("%d %d",&ac[i][0],&ac[i][1]);
		for(int i=0;i<j;++i)
			scanf("%d %d",&aj[i][0],&aj[i][1]);

		int ans=2;
		if(c==1 || j==1)
			;
		else{
			int a,b,x,y;
			if(c==2){
				a=ac[0][0],b=ac[0][1];
				x=ac[1][0],y=ac[1][1];
			}
			else{
				a=aj[0][0],b=aj[0][1];
				x=aj[1][0],y=aj[1][1];
			}
			if(x>a){
				if(y-a<=720 || b+1440-x<=720)
					;
				else
					ans=4;
			}
			else{
				if(b-x<=720 || y+1440-a<=720)
					;
				else
					ans=4;
			}
		}
		printf("Case #%d: ",t);
		printf("%d\n",ans);
	}
}