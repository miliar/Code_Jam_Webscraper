// GoogleJam2017.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

void clearmas(char mas[])
{
	for (int i = 0; i < 1000; i++) {
		mas[i] = ' ';
	}

}

int main()
{
	const int N = 1000;
	char  pancake[N];
	int flipper = 0, flips = 0, i = 0, T;
	bool possible = true;
	clearmas(pancake);

	ifstream output("input.txt");
	output >> T;
	ofstream write("output.txt");
	for (int q = 0; q < T; q++) {

		output >> pancake;
		output >> flipper;

		for (i = 0; i < 1000; i++) {
			if (pancake[i] == '-') {
				if (i + flipper - 1 < N && pancake[i + flipper] != ' ') {
					for (int j = i; j < i + flipper; j++) {
						if (pancake[j] == '-') {
							pancake[j] = '+';
						}
						else
						{
							pancake[j] = '-';
						}
					}
					flips++;
				}
				else
				{
					cout << "Impossible!" << endl;
					possible = false;
					break;
				}
			}
		}
		//cout << "Result: "; printmas(pancake); cout << " Flips: " << flips << endl;
		if (possible) {
			write << "Case #" << q + 1 << ": " << flips << endl;
		}
		else
		{
			write << "Case #" << q+1 << ": " << "IMPOSSIBLE" << endl;
		}
		
		cout << " Flips: " << flips << endl;
		clearmas(pancake);
		flips = 0;
		possible = true;
	}
	
	write.close();
	output.close();

	return 0;
}