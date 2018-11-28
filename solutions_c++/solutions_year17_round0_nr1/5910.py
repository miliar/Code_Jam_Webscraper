/*
 * code.cpp
 *
 *  Created on: 7/04/2017
 *      Author: cristhian
 */

#include <iostream>

using namespace std;


int main(){
	int n;
	cin >> n;

	for(int i = 0; i < n; i++){
		string ex;
		cin >> ex;
		int k;
		cin >> k;
		int count = 0;
		for(int j = 0; j <= ex.length() - k; j++){
			if(ex[j] == '-'){
				count++;
				for(int l = 0; l < k; l++){
					if(ex[j+l] == '-'){
						ex[j+l] = '+';
					}else{
						ex[j+l] = '-';
					}
				}
			}
		}
		bool flag = true;
		int lim =  (ex.length()-k);
		for(int j = ex.length()-1; j >= lim;j--){
			if(ex[j] == '-'){
				flag = false;
				break;
			}
		}
		cout << "Case #" << (i+1) << ": ";
		if(flag){
			cout << count << '\n';
		}else{
			cout << "IMPOSSIBLE" << '\n';
		}

	}
	return 0;

}


