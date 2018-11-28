// Oversized Pancake Flipper

#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(){
	int t, T;
	cin >> T;

	for(t=0; t<T; t++){
		string pancake;
		int K;

		cin >> pancake >> K;

		int flips=0;

		int i, j;
		for(i=0; i<=pancake.size()-K; i++){
			if(pancake[i]=='-'){
				for(j=0; j<K; j++){
					pancake[i+j]=(pancake[i+j]=='+')?'-':'+';
				}

				flips++;
			}
		}

		bool happy=true;

		for(i=0; i<pancake.size(); i++){
			if(pancake[i]=='-')
				happy=false;
		}

		if(happy){
			cout << "Case #" << (t+1) << ": " << flips << endl;
		}else{
			cout << "Case #" << (t+1) << ": " << "IMPOSSIBLE" << endl;
		}
	}
}