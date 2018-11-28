#include<iostream>
#include<cmath>

int main(){
	int casos, cajas, gente, exp, magic, grupo;
	std::cin >> casos;
	for(int i=0; i<casos; i++){
		std::cin >> cajas >> gente;
		exp = (int) (std::log(gente)/std::log(2));
		magic = pow(2, exp);
		gente = gente - magic + 1;
		cajas = cajas - magic +1;
		if(gente>(cajas%magic)){
			grupo=cajas/magic;
		} else {
			grupo=(cajas/magic)+1;
		}
		std::cout <<"Case #"<< i+1 << ": "<< grupo/2 << " " << (grupo-1)/2 << '\n';

	}
}
