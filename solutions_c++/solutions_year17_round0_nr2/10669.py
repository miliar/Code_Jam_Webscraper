// Google Code Jam 2017 Practicing.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <fstream>

//#define _CRT_SECURE_NO_WARNINGS


using namespace std;

bool isTidy(unsigned long long int n) {
	int digit = 9, digitHolder;
	do
	{
		digitHolder = n % 10;
		if (digitHolder > digit) {
			return false;
		}
		else {
			digit = digitHolder;
			n /= 10;
		}
	} while (n != 0);
	return true;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.in", "w", stdout);

	bool isDecreasing;
	unsigned long long int n, holder;
	unsigned int t;
	cin >> t;
	
	for (unsigned int i = 1; i <= t; i++) {
		isDecreasing = true;
		cin >> n;
		for (unsigned long long int y = n; y >= 1; y--) {
			isDecreasing = isTidy(y);
			if (isDecreasing == true) {
				cout << "Case #" << i << ": " << y << endl;
				break;
			}
			else;
		}
	}
}

/*bool one = false, two = false, three = false, four = false, five = false, six = false, seven = false, eight = false, nine = false, zero = false;

cin >> n;

int holder;
int l;
for (int j = 1; true; j++) {
holder = j*n;
for (int k = 1; holder != 0; k++) {
l = holder % 10;
holder /= 10;
switch (l)
{
case 1:
one = true; break;
case 2:
two = true; break;
case 3:
three = true; break;
case 4:
four = true; break;
case 5:
five = true; break;
case 6:
six = true; break;
case 7:
seven = true; break;
case 8:
eight = true; break;
case 9:
nine = true; break;
case 0:
zero = true; break;
default:
break;
}
}

if (one && two && three && four && five && six && seven && eight && nine && zero) {
cout << "Case #" << i << ": ";
cout << j*n << endl;
break;
}
if (j > 1000000000) {
cout << "Case #" << i << ": ";
cout << "INSOMNIA" << endl;
break;
}
}*/