#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

int main(){
	int T;
	unsigned long long int N, K;
	unsigned long long int min, max;
	unsigned long long int pot2, Prestantes, Wrestantes;
	long double meandist;
	double dec;
	/*
	pot2 = 1;
	for(int i=0;i<63;i++){
		cout<<pot2<<endl;
		pot2=pot2<<1;
	}
	*/
	
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> N >> K;
		pot2 = 1;
		while(pot2-1<K) pot2=pot2<<1;
		pot2=pot2>>1;
		//cout<<pot2<<endl;
		Prestantes = K - (pot2 - 1);
		Wrestantes = N - (pot2 - 1);
		meandist = 1.0 * Wrestantes / pot2;
		//cout<<Prestantes<<" "<<Wrestantes<<" "<<meandist<<endl;
		//dec = meandist - (meandist % 1);
		dec = (meandist-1)/2 - floor((meandist-1)/2);
		//cout<<dec<<endl;
		if(dec>0.5){
			unsigned long long int x, y;
			x = round((1.0*Wrestantes-1.0*pot2*floor(meandist))/(1.0*ceil(meandist)-1.0*floor(meandist)));
			y = pot2 - x;
			if(Prestantes<=x){
				min = ceil((meandist-1)/2.0);
				max = ceil((meandist-1)/2.0);
			}
			else{
				min = floor((meandist-1)/2.0);
				max = ceil((meandist-1)/2.0);
			}
		}
		else if(dec<0.5){
			unsigned long long int x, y;
			x = round((1.0*Wrestantes-1.0*pot2*floor(meandist))/(1.0*ceil(meandist)-1.0*floor(meandist)));
			y = pot2 - x;
			if(Prestantes<=x){
				min = floor((meandist-1)/2.0);
				max = ceil((meandist-1)/2.0);
			}
			else{
				min = floor((meandist-1)/2.0);
				max = floor((meandist-1)/2.0);
			}
		}
		else{
			max = ceil((meandist-1)/2.0);
			min = floor((meandist-1)/2.0);
		}
		
		cout << "Case #" << i+1 << ": " << max << " " << min << endl;
	}
	
}
