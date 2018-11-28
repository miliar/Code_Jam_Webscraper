#include <iostream>
#include <string>
using namespace std;

int* newNbr;
void borrow(int n){
	int i = n;
	bool finished = false;
	while (i >= 1 && !finished){
		if (newNbr[i]>0 && newNbr[i]>newNbr[i - 1]){
			newNbr[i]--;
			finished = true;
		}
		else {
			newNbr[i] = 9;
		}
		i--;
	}
	if (!finished){
		newNbr[i]--;
		finished = true;
	}
}
void maxTheRest(int startIndex, int length){
	for (int i = startIndex; i<length; i++)
		newNbr[i] = 9;
}
void main() {
	int t, i;
	string s="";
	
	cin >> t;
	for (int c = 1; c <= t; ++c) {
		//getline(cin, s);
		cin >> s;
		const int length = s.length();
		newNbr = new int[length];
		bool finished = false;
		i = 0;

		while (i<length && !finished){
			int current = s.at(i) - (int)48;;
			if (i == 0){
				newNbr[i] = current;
			}
			else {
				if (current<newNbr[i - 1]){
					borrow(i - 1);
					maxTheRest(i, length);
					finished = true;
				}
				else {
					newNbr[i] = current;
				}
			}
			i++;
		}

		
		
		
		string newS = "";
		int j;
		if (newNbr[0] == 0)
			j = 1;
		else
			j = 0;
		

		cout << "Case #" << c << ": ";
		for (j; j < length; j++){
			//newS.append(std::to_string(newNbr[i]));
			cout << newNbr[j];
		}
		cout  << endl;
		delete[] newNbr;
	}
}

