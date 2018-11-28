// tidy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "stdint.h"
#include <string>
#include <fstream>
using namespace std;


int main()
{

	unsigned int T,same;
	unsigned long long int N, a, b, temp,power , res, max_poz,max,max1;
	
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("B-large.out");
	in >> T;
	for (int i = 0; i < T; i++) {
		in >> N;
		int nr = 0;
		temp = N;
		while (temp) {
			temp = temp / 10;
			nr++;
		}
		
		if (N < 10)out << "Case #" << i + 1 << ": " << N << endl;
		else {
			same = 0;
			temp = N;
			for (int j = 0; j < nr - 1; j++) {
				a = temp % 10;
				temp = temp / 10;
				b = temp % 10;
				if (a >= b)  same++;

			}
			if (same == nr - 1) {
				out << "Case #" << i + 1 << ": " << N << endl;

			}
			else {
			max = 10;
				max1 = 0;
				same = 0;
				while (same != nr - 1) {
					max_poz = 0;
					power = 1;

					for (int w = 0; w < nr - 1; w++) {
						power *= 10;
					}
					temp = N;
					while (temp) {
						if ((temp / power) > max1 && (temp / power) < max) {
							max1 = temp / power;
							max_poz = power;
						}

						temp %= power;
						power /= 10;
					}
					same = 0;
					temp = N;
					res = N - (max_poz* (temp / max_poz));
					N = temp - res - 1;
					temp = N;
					for (int j = 0; j < nr - 1; j++) {
						a = temp % 10;
						temp = temp / 10;
						b = temp % 10;
						if (a >= b)  same++;

					}

					max = max1;
					max1 = 0;
				}
				if (same == nr - 1) {
					out << "Case #" << i + 1 << ": " << N << endl;

				}
			}
		}
		}

	in.close();
	out.close();


    return 0;
}

