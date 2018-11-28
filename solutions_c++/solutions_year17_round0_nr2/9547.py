#include <iostream>

using namespace std;

int power(int a, int b){
	
	int sum = 1;
	
	for (int i = 0 ; i < b ; i++){
	
		sum = sum*a;
	}

	return sum;
}

int main (){

	int T;

	cin >> T;

	for ( int h = 0 ; h < T ; h++ ){
		
		int N;
		int g = 1;
		cin >> N;

		int a,b, k = 0, i ;

		for (i = N ; i != 0 ; i--){

			int flag = 0;

			for (int j = 0; ; j++){
				
				b = ( i % power(10, j+1) )/power(10 , j);
				a = ( i % power(10, j+2) )/power(10 , j +1);
				
				if (a > b ){
					 flag = 1;
					 break;
				}

				if (i % power(10, j+2) == i) break;

			}

			if (flag == 0) break;
		}

		g++;
		cout << "Case #"<< h+1 << ": "<< i << endl;

	}


	return 0;
}
