#include <iostream>
#include <string>

using namespace std;

int main(){

	string input;
	int T;

	getline(cin, input);
	T = stoi(input);

	for(int i = 0; i < T; ++i){
		cout << "Case #"<<i+1<<": ";

		getline(cin, input);
		int j = 1;
		bool f = false;
		while(!f){
			if(input.size() > 1){
				for(j = 0; j < input.size() - 1; ++j){
					if(input[j] > input[j+1]){
						if(input[j] == '1' && j == 0){
							input = string(input.begin()+1, input.end());
						}else{
							input[j] = input[j] - 1;
							j++;
						}
						break;
					}
					if(j == input.size() - 2) {
						f = true;
					}
				}
				if(!f)
				for(; j < input.size(); ++j){
					input[j] = '9';
				}
			}else{
				f = true;
			}			
		}	

		cout << input << endl;
	}

}