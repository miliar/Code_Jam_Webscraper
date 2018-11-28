// B_Tidy_Numbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
using namespace std;

void printmas(int mas[],int count) {
	for (int i = 0; i < count; i++) {
		cout << mas[i] << endl;
	}
	cout << endl;
}

void over999(int n[],int j, int count) {
	int b = j;
	for (int j=b; j < count; j++) {
		n[j] = 9;
	}
}

void underscroll(int n[], int *count) {
	int i;
	for (i = 0; i < *count - 1; i++) {
		n[i] = 9;
	}
	n[i] = 10;
	*count -= 1;
}

void clearmas(int mas[])
{
	for (int i = 0; i < 19; i++) {
		mas[i] = 10;
	}

}

int main()
{
	long long N, td;
	char tidy[20];
	int count = 0, n[19],T;

	ifstream output("input.txt");
	output >> T;
	ofstream write("output.txt");
	for (int q = 0; q < T; q++) {
		clearmas(n);
		td = 0;
		N = 0;
		count = 0;

		output >> tidy;

		for (int i = 0; i < 19; i++) {
			if (tidy[i] != '\0') {
				n[i] = (int(tidy[i]) - 48);
				N = N*10 + (int(tidy[i]) - 48);
				count++;
			}
			else {
				break;
			}
		}
		n[count] = 10;

		//printmas(n,count);cout << endl; 
		for (int d = 0; d < 19; d++) {
			for (int j = 0; j < count; j++) {
				if (n[j] > n[j + 1] && n[j + 1] < 10) {
					if (n[j] == 1 && j == 0) {
						underscroll(n, &count);
					}
					else {
						n[j] -= 1;
						over999(n, j + 1, count);
					}
				}
			}
		}
		if (n[0] == 0)
			underscroll(n, &count);

		//digit = 1;
		for (int i = 0; i < count; i++) {
			if (0 <= n[i] < 10) {
				td = td*10 + n[i];
			}
		}
		//printmas(n, count); cout << endl;
		cout << N << ' ' << td << endl;
		write << "Case #" << q + 1 << ": " << td << endl;
	}

write.close();
output.close();

return 0;
}

