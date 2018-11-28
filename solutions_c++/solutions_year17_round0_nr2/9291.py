#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

void main(){
	int t;
	string number;
	cin >> t;
	getline(cin, number);
	for (int i = 1; i <= t; ++i){
		getline(cin, number);
		string str(number);
		if (number.length() > 1){
			bool changes = true;
			while (changes){
				changes = false;
				for (int it = 0; it < number.length() - 1; ++it){
					if (number[it] > number[it + 1]){
						changes = true;
						number[it] = number[it] - 1;
						
						for (int ite = it + 1; ite < number.length(); ++ite)
							number[ite] = 57;
						if (number[0] == 48){
							number.erase(number.begin() + 0);
						}
					}
					
				}
				

			}
		}
		cout << "Case #" << i << ": " << number << endl;
	}

}