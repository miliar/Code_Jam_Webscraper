#include<iostream>
#include<string>
using namespace std;

int main(){
	int c;
	cin >> c;
	int *output;
	output = new int[c];
	getchar();
	for (int l = 0; l < c; l++){
		string input;
		int flipper = 0;
		int p = 0, n = 0;
		int count = 0;
		cin >> input;
		cin >> flipper;
		bool clear2 = false;
		for (int k = 0; k < 50 && clear2 == false; k++){
			for (int i = 0; i < (signed)input.length() - flipper; i++){

				if (input.at(i) == '-'){
					for (int j = 0; j < flipper; j++){
						if (input.at(j + i) == '+')
							input.at(j + i) = '-';
						else
							input.at(j + i) = '+';
					}
					count++;
				}

			}
			
			bool last = false;
			for (int j = 0; j < flipper; j++){
				if (input.at((unsigned)input.length() - flipper + j) == '-')
					last = true;
			}
			if (last){
				for (int j = 0; j < flipper; j++){
					if (input.at(j + (unsigned)input.length() - flipper) == '+')
						input.at(j + (unsigned)input.length() - flipper) = '-';
					else
						input.at(j + (unsigned)input.length() - flipper) = '+';
				}
				count++;
			}

			bool clear = true;
			for (int i = 0; i < (signed)input.length(); i++)
				if (input.at(i) == '-')
					clear = false;
			if (clear){
				clear2 = true;
			}
		}
		if (clear2 == false)
			output[l] = 114514;
		else
			output[l] = count;
	}
	
	for (int i = 0; i < c; i++){
		if (output[i] == 114514)
			std::cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
		else
			std::cout << "Case #" << i + 1 << ": " << output[i] << "\n";
	}
	getchar();
	getchar();
	return 0;
}