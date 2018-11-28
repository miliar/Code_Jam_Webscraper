#include <iostream>

using namespace std;

int power2[21] = { 1, 2, 4 ,8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};

int find_largest_power(int a){

	int i;
	
	for (i = 0 ; i < 21 ; i++){

		if (a < power2[i] ) break;

	}

	return i;
}

int main(){

	int T;

	cin >> T;

	for ( int h = 0 ; h < T ; h++){

		int N, k;
		
		cin >> N >> k;

		int no_space = find_largest_power(N + 1);		
		
		int k_power = find_largest_power(k);

		if ( k_power == no_space ) cout << "Case #" << h + 1 << ": " << 0 << " " << 0 << endl;

		else{

			int max = 0 , min = 0;


			int sum = N*power2[k_power];

			for( int g = 0 ; g < k_power ; g++){

				sum = sum - (N + 1)*power2[k_power - g -1 ];
			}

			int x,y;

			x = sum / power2[k_power-1];
			y = sum % power2[k_power-1];

			if ( x % 2 == 1) {
				max = x / 2 + 1;
				min = x / 2; 
				
				if (k <= power2[k_power-1] + y - 1) min++;
			}

			else {
				max = x / 2;
				min = x / 2;
				
				if (k <= power2[k_power-1] + y - 1) max++;
			}
		
			cout << "Case #" << h + 1 << ": " << max << " " << min << endl;

		}

	}

	return 0;
}