#include<iostream>
#include<fstream>
using namespace std;
void find(int a[], int &lenght,int& start);

int main() {
	int a[19];
	int T;
	long long temp;
	ifstream input;
	ofstream output;
	input.open("h.txt");
	output.open("answers.txt");
	input >> T;
	for (int t = 1; t <= T; t++) {
		input >> temp;
		int lenght = log10(temp)+1;
		int start = 1;
		for (int l = lenght; l >0; l--) {
			a[l] = temp % 10;
			temp = temp / 10;
		}
		find(a, lenght,start);
		output << "Case #" << t << ": ";
		for (int i = start; i <= lenght; i++) {
			if (i==start && a[i]==0)
				continue;
			output << a[i];
		}
		output << endl;
	}
	system("pause");
	return 0;
}

void find(int a[], int &lenght, int& start) {
	int identical = -1;
	bool same = false;
	for (int i = 1; i < lenght; i++) {
		if (a[i + 1] == a[i] && same == false) {
			identical = i;
			same = true;
		}
		if (a[i + 1] > a[i]) {
			same = false;
			identical = -1;
		}
		if (a[i + 1] < a[i]){
			if (identical != -1)
				i = identical;

			if (i == 1 && a[i] == 1) {
				start++;
				i++;
				while (i <= lenght) {
					a[i] = 9;
					i++;
					}
				return;
			}
			else if (a[i] == 0) {
					if (i == 2 && a[1] == 1) {
						start++;
						while (i <= lenght) {
							a[i] = 9;
							i++;
						}
						return;
					}
					else {
						a[i - 1] = a[i - 1] - 1;
						while (i <= lenght) {
							a[i] = 9;
							i++;
						}
						return;
					}
				}
			else {
				a[i] = a[i] - 1;
				i++;
				while (i <= lenght) {
					a[i] = 9;
					i++;
				}
				return;
			}
		}
	}
}