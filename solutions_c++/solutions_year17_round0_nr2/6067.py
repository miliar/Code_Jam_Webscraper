#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	int test_case;
	cin >> test_case;

	for(int c = 1; c <= test_case; c++){
		string str;
		int index = 0;
		int num[19];
		cin >> str;

		cout << "Case #" << c << ": ";

		if(str.size() == 1){
			cout << str << endl;
			continue;
		}

		index = str.size();

		for(int i = 0; i < index; i++){
			char n = str[i];
			num[i] = atoi(&n);
		}

		reverse(num, num+index);

		for(int i = 0; i < index-1; i++){
			if(num[i] < num[i+1]){
				num[i+1]--;
				num[i] = 9;
				for(int j = 0; j < i; j++){
					num[j] = 9;
				}
			}
		}
		if(num[index-1] > 0)
			cout << num[index-1];

		for(int i = index-2; i >= 0; i--){
			cout << num[i];
		}
		cout << endl;
		
	}
	return 0;
}