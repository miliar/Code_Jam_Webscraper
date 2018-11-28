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
		string k;
		cin >> k;
		for(int j = k.length() - 1; j > 0; j--){
			if(k[j] < k[j-1]){
				for(int l = j; l < k.length(); l++){
					if(k[l] == '9'){
						break;
					}
					k[l] = '9';
				}
				k[j-1] = k[j-1]-1;
			}
		}
		cout << "Case #" << (i+1) << ": ";
		int j = 0;
		while(k[j] == '0'){
			j++;
		}

		if(j == k.length()){
			cout << 0;
		}else{
			for(;j<k.length();j++){
				cout << k[j];
			}
		}
		cout << '\n';
	}
	return 0;

}


