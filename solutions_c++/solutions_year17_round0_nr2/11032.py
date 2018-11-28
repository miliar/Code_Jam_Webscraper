#include<bits/stdc++.h>

using namespace std;

int main(){
	
	int a;
	cin >> a;
	
	int vet[a], vetRes[a];
	
	for(int j = 0; j < a; j++){
		cin >> vet[j];	
		for(int i = vet[j]; i > 0; i--){
			if(i == 1000){
				vetRes[j] = 999;
				break;
			}
			
			if(i <= 999 && i >= 100){
				int a, b, c;
				
				a = i%10;
				b = (i/10)%10;
				c = (i/100)%10;
				if(a >= b && b >= c){
					vetRes[j] = i;	
					break;
				}
			}
			
			if(i <= 99 && i >= 10){
				int a, b, c;
				
				a = i%10;
				b = (i/10)%10;
				if(a >= b){
					vetRes[j] = i;
					break;	
				}
			}
			
			if(i <= 9 && i >= 1){
				vetRes[j] = i;
				break;
			}
		}
	}
	
	for(int i = 0; i < a; i++){
		cout << "Case #" << i+1 << ": " <<vetRes[i] << endl;
	}
}
