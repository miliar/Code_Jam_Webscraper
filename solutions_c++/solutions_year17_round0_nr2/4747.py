#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	for (int times = 1; times <= t; times++){
		string num;
		cin >> num;
		char last = '0';
		for (int i =0; i < num.size(); i++){
			if (num[i] < last){
				num[i-1]--;
				for (int j = i; j < num.size(); j++)
					num[j] = '9';
				i -= 2;
				if (i >= 0)
					last = num[i];
				else
					last = '0';
			}
			else
				last = num[i];
		}
		string editstring = "";
		for (int i =0; i < num.size(); i++)
			if (num[i] != '0')
				editstring += num[i];
		cout << "Case #" << times << ": " << editstring << endl;;
	}
	return 0;
}