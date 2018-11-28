#include<bits/stdc++.h>
using namespace std;
int T,N,R,O,Y,G,B,V,pre;

void myprint(int i){
	if (i==1){
		if (R==1) {
			for (int j=1;j<=G;j++) printf("RG");
		}
		printf("R"); pre=1;
		R--;
	} else if(i==2){
		if (Y==1) {
			for (int j=1;j<=V;j++) printf("YV");	
		}
		printf("Y"); pre=2;
		Y--;
	} else {
		if (B==1) {
			for (int j=1;j<=O;j++) printf("BO");	
		}
		printf("B"); pre=3;
		B--;	
	}
}

int main(){
	freopen("stable.in","r",stdin);
	freopen("stable.out","w",stdout);
	scanf("%d",&T);
	for (int i=1; i<=T;i++){
		scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
		printf("Case #%d: ",i);
		if (R<G || Y<V || B<O) printf("IMPOSSIBLE\n");
		else if(R!=0&& R==G){
			if (R+G==N){
				for (int j=1;j<=R;j++) printf("RG"); printf("\n");
			} else printf("IMPOSSIBLE\n");
		}else if (Y!=0 && Y==V){
			if (Y+V==N){
				for (int j=1;j<=Y;j++) printf("YV"); printf("\n");
			} else printf("IMPOSSIBLE\n");
		}else if (B!=0 && B==O){
			if (B+O==N){
				for (int j=1;j<=B;j++) printf("BO"); printf("\n");
			} else printf("IMPOSSIBLE\n");
		} else {
			R-=G; Y-=V; B-=O; N=N-2*(G+V+O);
			if (R>Y+B || Y>B+R || B>R+Y) printf("IMPOSSIBLE\n");
			else {
				int st;
				if (R>=B && R>=Y) {
					st=1; myprint(1);
				} else if(Y>=R && Y>=B) {
					st=2; myprint(2);
				} else {
					st=3; myprint(3);
				}
				for (int j=N-1;j>0;j--){
				//	printf("%d %d %d\n",R,Y,B);
					if (R==B && R==Y) {
						if (pre!=st) myprint(st);
						else myprint(st%3+1);
					}else if (R==B && R>Y){
						if (pre==1) myprint(3);
						else if (pre==3) myprint(1);
						else if (st==3) myprint(3);
						else myprint(1);
					} else if (R==Y && R>B){
						if (pre==1) myprint(2);
						else if (pre==2) myprint(1);
						else if (st==2) myprint(2);
						else myprint(1);
					} else if (B==Y &&B>R){
						if (pre==2) myprint(3);
						else if (pre==3) myprint(2);
						else if (st==3) myprint(3);
						else myprint(2);
					} else if (R>B && R>Y) {
						if (pre==1){
							if (B==Y){
								if (st==3) myprint(3);
								else myprint(2);
							} else if (B>Y) myprint(2);
							else myprint(3);
						} else myprint(1);
					} else if(Y>R && Y>B) {
						if (pre==2){
							if(Y==R){
								if (st==3) myprint(3);
								else myprint(1);
							} else if (R>Y) myprint(1);
							else myprint(3);
						} else myprint(2);
					} else {
						if (pre==3){
							if(B==R){
								if (st==2) myprint(2);
								else myprint(1);
							}else if (R>B) myprint(1);
							else myprint(2);
						} else myprint(3);
					}					
				}
				printf("\n");
			}
		}
	}
	return 0;
}
