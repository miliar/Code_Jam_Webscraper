#include <iostream>
#include <vector>

using namespace std;

unsigned long long prev_pot(unsigned long long);

int main(){
	unsigned int total;
	cin >> total;
	unsigned long long space;
	unsigned long long pot;
	unsigned long long K,N;
	for( unsigned int k = 0; k < total; k++){
		cin >> K >> N;
		pot = prev_pot(N);
		space = (K-N+pot)/pot ;
		cin.clear();
		cout << "Case #" << k+1 << ": " << space/2 << " " << (space-1)/2 << endl;	
	}
	
}

unsigned long long prev_pot(unsigned long long n){
	unsigned long long temp = n;
	int count = 0;
	while (temp !=1){
		temp /= 2;
		count++;
	}
	while(count!=0){
		temp*=2;
		count--;
	}
	return temp;
}