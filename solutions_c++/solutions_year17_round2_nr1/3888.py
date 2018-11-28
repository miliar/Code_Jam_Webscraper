#include <stdio.h>
#include <math.h>
#define PRINT 0
int N;
double D;



int main(){
	

	FILE* input = fopen("in.txt","r+");
	FILE* output = fopen("out.txt","w");

	int TT;
	fscanf(input,"%d",&TT);

	for(int T=1; T<=TT; T++){

		//READ
		fscanf(input,"%lf %d",&D,&N);
		long horses[N][2];
		for(int n=0; n<N; n++){
			double k,s;
			fscanf(input,"%lf %lf",&k,&s);
			horses[n][0] = k;
			horses[n][1] = s;
		}
		for(int n=0; n<N; n++){
					printf("horse %d: k=%ld\t s=%ld TTG=%f\n",n+1,horses[n][0],horses[n][1],(float)(D-horses[n][0])/horses[n][1]);
					if((float)(D-horses[n][0])/horses[n][1] <= 0)printf("ZEROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n");
			}
		printf("D = %lf\n",D);

		//SOLVE

		//solution 1
		//find the horse who will get there last
		double tmax = -1;
		int horse=0;
		for(int n=0; n<N; n++){

			double tD = (D-horses[n][0])/horses[n][1];
			if(tD > tmax && tD > 0) {
				tmax = tD;
			}

		}

		if(tmax<=0) tmax=0.000001;
		double v = D/tmax;

		//PRINT
		printf("d = %lf",v*tmax);
		printf("Case #%d: %lf    \n",T,v);
		fprintf(output,"Case #%d: %f\n",T,v);
		//fprintf(output,"Case #%d: %f\n",T,answer);
		//fprintf(output,"Case #%d: %f\n",T,v);

		



	}// for T

	fclose(input);
	fclose(output);

	return 0;

}