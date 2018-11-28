#include<iostream>

char comprobar(long num){
	int aux = num % 10;
	num = num/10;
	while(num>0){
		if(aux<num%10){
			return 0;
		}
		aux = num%10;
		num = num/10;
	}
	return 1;
}

int main(){
	int i, T;
	long j, num;
	std::cin >> T;
	for(i=0; i<T; i++){
		std::cin >> num;
		for(j=num; j>0; j--){
			if(comprobar(j)==1){
				std::cout << "Case #" << i+1 << ": " << j << '\n';
				break;
			}
		}
	}
}
