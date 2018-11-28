#include<iostream>
#include<string>
#include<array>
#include<cstdlib>
using namespace std;

int ctoi(char c){
	switch (c){
	case '1': return 1;
	case '2': return 2;
	case '3': return 3;
	case '4': return 4;
	case '5': return 5;
	case '6': return 6;
	case '7': return 7;
	case '8': return 8;
	case '9': return 9;
	case '0': return 0;
	default:return -1;
	}
}

char itoc(int c){
	switch (c){
	case 1: return '1';
	case 2: return '2';
	case 3: return '3';
	case 4: return '4';
	case 5: return '5';
	case 6: return '6';
	case 7: return '7';
	case 8: return '8';
	case 9: return '9';
	case 0: return '0';
	default:return '-1';
	}
}
bool check(int *num){
	for (int i = 0; i < 20; i++){
		if (*(num + i) < 0)
			return false;
	}
	return true;
}

int main(){
	int t;
	cin >> t;
	getchar();
	string *output;
	output = new string[t];
	for (int i = 0; i < t; i++)
		output[i] = "";
	for (int k = 0; k < t; k++){
		string input;
		cin >> input;
		getchar();
		int num[20] = { 0 };

		for (int i = 0; i < (signed)input.length(); i++){
			num[i] = ctoi(input.at(i));
		}
		num[input.length()] = 114514;
		for (int n = 0; n < 20; n++){
			for (int j = 0; num[j + 1] != 114514; j++){
				if (num[j] > num[j + 1]){
					num[j] --;
					for (int l = j + 1; num[l] != 114514; l++)
						num[l] = 9;
				}
			}
			while (!check(&num[0])){
				for (int i = 0; i < 20; i++){
					if (num[i] < 0){
						num[i - 1]--;
						num[i] += 10;
					}
				}
			}
		}
		bool nature = false;
		for (int i = 0; i < (signed)input.length(); i++){
			if (num[i] != 0)
				nature = true;
			if (nature)
				output[k] += itoc(num[i]);
		}
	}

	for (int i = 0; i < t; i++){
		cout << "Case #" << i + 1 << ": " << output[i] << "\n";
	}
	getchar();
	getchar();
	return 0;
}