#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

bool check(int num[], int len) {
	int c = num[0];

	for (int i = 1; i < len; i++) {
		if (c > num[i])	
			return false;

		c = num[i];
	}
	return true;
}

int main()
{
	// Vars
	int ncases;
	int num[19];
	int strlen;
	int max, maxi, temp;
	bool start;
	string numstr;

	// Input/Output
	ifstream in;
	ofstream out;

	in.open("B_files/B-large.in");
	out.open("B_files/B-large-results.out");

	// Solution
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		memset(num, -1, sizeof(int) * 18);
		in >> numstr;

		strlen = numstr.length();
		for (int i = 0; i < strlen; i++) {
			num[i] = numstr.at(i) - '0';
		}

		out << "Case #" << t << ": ";
		if (check(num, strlen)) {
			// same as N
			out << numstr;
		}
		else {
			max = num[0];
			maxi = 0;
			for (int i = 1; i < strlen; i++) {
				if (num[i - 1] > num[i]) {
					temp = i - 1;
					if (num[i - 1] > max) {
						maxi = temp;
					}
					break;
				}
				else if (max < num[i]) {
					max = num[i];
					maxi = i;
				}
			}
			num[maxi]--;

			for (int i = maxi + 1; i < strlen; i++) {
				num[i] = 9;
			}
			
			start = false;
			for (int i = 0; i < strlen; i++) {
				if (start) {
					out << num[i];
				}
				else {
					if (num[i] != 0) {
						out << num[i];
						start = true;
					}
				}
			}
		}

		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}