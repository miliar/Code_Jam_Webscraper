#include "stdio.h"
#include "algorithm"

int t,n,mx;
int r,o,y,g,b,v;

void printR(){
	putchar('R');
}

void printY(){
	putchar('Y');
}

void printB(){
	putchar('B');
}

void printYB(int x){
	for(int i = 0; i < x; i++){
		printY();
		printB();
	}
}

int main(){
	scanf("%d",&t);
	for(int te = 1; te <= t; te++){
		scanf("%d %d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		
		mx = std::max(r,std::max(y,b));
		if(2*mx>r+y+b){
			printf("Case #%d: IMPOSSIBLE\n",te);
		}else{
			printf("Case #%d: ",te);
			if(r==0){
				printYB(y);
			}else{
				for(int i = 0; i+1 < r; i++){
					printR();
					if(y>b){
						printY();
						y--;
					}else{
						printB();
						b--;
					}
				}
				printR();
				if(y==b){
					printYB(y);
				}else if(y>b){
					printYB(b);
					printY();
				}else{
					//b>y
					printB();
					printYB(y);
				}
			}
			printf("\n");
		}
	}
}