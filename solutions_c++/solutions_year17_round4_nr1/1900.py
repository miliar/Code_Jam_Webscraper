#include<iostream>
using namespace std;

int G[101];
int ount[10];

int total;

int main(){

	int T;
	int N, P;

	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		
		scanf("%d %d", &N, &P);
		ount[0] = 0;
		ount[1] = 0;
		ount[2] = 0;
		ount[3] = 0;

		for(int j=0;j<N;j++){
			scanf("%d", &G[j]);
			ount[G[j]%P]++ ;
		}
				
		total = ount[0];
		if(P == 2)
			total += (ount[1] + 1)/2;

		if(P == 3){
			if(ount[1] <= ount[2]){
				total += ount[1];
				ount[2] -= ount[1];
				ount[1] = 0;
				total += (ount[2] + 2)/3;
			}			
			else {

				total += ount[2];
                             
                                ount[1] -= ount[2];
                             	ount[2] = 0;
				   total += (ount[1] + 2)/3;
			}
			
		}		 
	
		if(P == 4){

			if(ount[1] <= ount[3]){
                                total += ount[1];
                                
                                ount[3] -= ount[1];
				ount[1] = 0;

				if(ount[2]%2 == 0)
					total += ount[2]/2;
				else{
					total += (ount[2]+1)/2 ;
					ount[3] -= 2;
					if(ount[3] > 0)
						total += (ount[3] + 3)/4;
				}
                                
                        }
                        else {

                                total += ount[3];
                                
                                ount[1] -= ount[3];
				ount[3] = 0;

				if(ount[2]%2 == 0)
                                        total += ount[2]/2;
                                else{
                                        total += (ount[2]+1)/2 ;
                                        ount[1] -= 2;
                                        if(ount[1] > 0)
                                                total += (ount[1] + 3)/4;
                                }
                              
                        }
		}			
		printf("Case #%d: %d\n", i, total);
	}
}
