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
		int segmentos[10000];
		memset(segmentos, 0, 10000);
		int k;
		cin >> k;
		segmentos[n]+=1;
		for (int s = 0; s < k; s++){
			if (segmentos[n] > 0)
				segmentos[n]-=1;
			else{

				if (segmentos[n - 1] > 0 ){
					n--;
					segmentos[n]-=1;
					//cout << "Entro por aqui 1" << endl;
				}
				else{
						//te quedas con el mayor
						n = n - (((n - 1)/2) + 1);
						if (segmentos[n + 1] > 0)
							n++;
						segmentos[n]-=1;
						//cout << "Entro por aqui 2" << endl;
				}
			}
			//cout << "Valor: " << n  << "Contador: " << s + 1  << "Segmento actual: " << segmentos[n]  << "Segmento superior: " << segmentos[n + 1] <<  "valor segmento superior: " << n + 1 <<  endl;
			//primer segmento
			segmentos[(n - 1)/2]+=1;
			//segundo segmento
			segmentos[n - (((n - 1)/2) + 1)]+=1;

		}
		
		cout << "Case #" << l << ": " << n - (((n - 1)/2) + 1) << " " << (n - 1)/2<< endl;


	}

return 0;
}
