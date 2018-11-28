#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int main(){
	int t;
	int c,j,ans,t1,t2,t3,t4;
	scanf("%d\n", &t);
	for (int _=1; _<=t; _++){
		scanf("%d %d\n", &c, &j);
		if (c<2 && j<2){
			for(int i=0; i<c; i++) 		scanf("%d %d\n", &t1, &t2);
							for(int i=0; i<j; i++) 		scanf("%d %d\n", &t1, &t2);
		printf("Case #%d: %d\n", _, 2); 

		}
		else{
			scanf("%d %d\n", &t1, &t2);
			scanf("%d %d\n", &t3, &t4);
			if (t2<t1){
				t2+=1440;
				t3+=1440;
				t4+=1440;
			}
			if(t4<t3){
				t1+=1440;
				t2+=1440;
				t4+=1440;
			}
			int d;
			// if(t3>t1) d = t4-t1;
			// else d=t2-t3;
			int d1 = t4-t1, d2=t2-t3;
			if (d1<0) d1+=1440;
			if (d2<0) d2+=1440;
			if (d1<=720||d2<=720)
			
		printf("Case #%d: %d\n", _, 2); 
	else
		printf("Case #%d: %d\n", _, 4); 

		}
	}
}