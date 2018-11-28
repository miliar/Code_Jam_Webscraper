#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	for (int l = 1; l<= t; l++){
		long long int n;
		cin >> n;
		long long int naux;
		int anterior;
		bool seguir = true;
		long long int despl;
		long long int resta;
		while(seguir && n != 0){
			despl = 1;
			naux = n;
			anterior = naux % 10;
			naux = naux / 10;
			resta = 0;
			while(anterior >= (naux % 10) && naux >= 10){
				anterior = naux % 10;
				naux = naux / 10;
				despl = despl * 10;
				resta += anterior * despl;
			}
			if (anterior >= naux)
				seguir = false;
			else
				n -= resta + 1;
			
		}

		cout << "Case #" << l << ": " << n << endl;

	}


return 0;
}
