#include <iostream>
#include <string>
using namespace std;

int main(){
	int test_case;
	cin >> test_case;

	for(int c = 1; c <= test_case; c++){
		cout << "Case #" << c << ": ";
		string cake;
		int flipper;
		cin >> cake >> flipper;

		int count = 0;

		for(int i = 0; i < cake.size(); i++){
			if(cake[i] == '+'){
				count++;
			}
		}
		if(count == cake.size()){
			cout << "0" << endl;
			continue;
		}
		else if(count == 0 && cake.size() == flipper){
			cout << "1" << endl;
			continue;
		}

		count = 0;

		for(int i = 0; i < cake.size()-1; i++){
			if(cake[i] == '-'){
				if(i + flipper > cake.size())
					break;
				for(int j = 0; j < flipper; j++){
					if(cake[i+j] == '-')
						cake[i+j] = '+';
					else
						cake[i+j] = '-';
				}
				count++;
			}
		}

		bool ret = true;

		for(int i = 0; i < cake.size(); i++){
			if(cake[i] == '-')
				ret = false;
		}
		if(ret)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}