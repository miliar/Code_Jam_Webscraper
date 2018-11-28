#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	string pan;
	int k;
	int flips = 0;
	int c;
	bool t = true;

	cin >> c;

	for (int v = 1; v <= c; v++){
		flips = 0;
		t = true;
		cin >> pan;
		cin >> k;

		for (int i = 0; i < pan.length(); i++){
			if (pan[i] == '-'){
				for (int j = i; j < i+k && i+k-1 < pan.length(); j++){
					(pan[j] == '-') ? pan[j] = '+' : pan[j] = '-';
				}
				flips++;
			}
		}



		for (int i = 0; i < pan.length(); i++){
			if (pan[i] == '-'){
				t = false;
				break;
			}
		}

		t ? printf("Case #%d: %d\n" ,v ,flips) : printf("Case #%d: IMPOSSIBLE\n" ,v);

	}

	




	return 0;
}