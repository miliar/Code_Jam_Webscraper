#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <ctime>

double K[1024],S[1024],U[1024],V[1024];

int search_spd(double *spd,int D){
	
}

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int T,ct,i,j,N,index;
	double spd,mspd,v,D,t,mt;

	cin >> T;
	for (ct = 1; ct <= T; ++ct) {
		cin >> j; D = (double)j; 
		cin >> N;
		for(i=0;i<N;i++){
			cin >> j; K[i] = (double)j; 
			cin >> j; S[i] = (double)j;
		}
//		for(i=0;i<N;i++) printf("%lf %lf\n",K[i],S[i]);
		/*
		for(i=0;i<N;i++){
			if(K[i]<D)
				break;
		}
		mspd = (K[i] - D)/S[i];
		for(i=0;i<N;i++){
			if(K[i] >= (double)D)
				continue;
			spd = (D - K[i])/S[i];
			if(spd < mspd)
				mspd = spd;
		}
		spd = mspd;
		search_spd(&spd,D);
		*/
		index = 0;
		mt = (D - K[0])/S[0];
//		printf("KSt: %lf %lf %lf\n",K[0],S[0],mt);
		for(i=1;i<N;i++){
			t = (D-K[i])/S[i];
//			printf("KSt: %lf %lf %lf\n",K[i],S[i],t);
			if(t > mt){
				mt = t; index = i;
			}
		}
//		cout << "index: "<<index<<endl;
		for(i=0;i<N;i++){
			if(i==index){
				U[i] = 0;
				continue;
			}
			if(K[i] > K[index]) {
				U[i] = -1;
				continue;
			}
			U[i] = (K[i] - K[index])/(S[index] - S[i]);
//			V[i] = K[i] + U[i]*S[i];
			/*
			if(U[i] < 0){
				printf("D: %lf\n",D);
				printf("%lf %lf on %lf %lf\n",K[i],S[i],K[index],S[index]);
				exit(-1);
			}
			*/
		}

		mspd = D*S[index]/(D-K[index]);
		for(i=0;i<N;i++){
			if(i==index)
				continue;
			if(U[i]<0)
				continue;
			spd = (K[i] + S[i]*U[i])/U[i];
			if(spd < mspd)
				mspd = spd;
		}
	
		//cout << "Case #" << ct <<": "<< mspd <<endl;
		printf("Case #%u: %.10lf\n",ct,mspd);
	}
}