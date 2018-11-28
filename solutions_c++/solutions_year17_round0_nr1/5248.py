// ConsoleApplication5.cpp : Defines the entry point for the console application.
//

#include <stdio.h>>
#include "stdafx.h"
#include <iostream>
#include <fstream>

#define MAX_SIZE 100
using namespace std;

int func(char* istr, int istrl, int k)
{
	int rv = 0;
	for (int i = 0; i < istrl; i++)
	{
		cout << istr << " " <<rv<< endl;
		if (istr[i] == '-')
		{
			for (int j = 0; j < k; j++)
			{
				if (istr[i + j] == '-') istr[i + j] = '+';
				else if (istr[i + j] == '+') istr[i + j] = '-';
				if (i + j >= istrl) 	{cout << istr <<" "<< -1 << endl << endl; return -1;}
			}
			rv++;
		}
	}
	cout << istr<<" " <<rv<< endl<< endl;
	return rv;
}
int main()
{
	int t;
	
	char str[MAX_SIZE];
	
	ifstream inFile("A-small-attempt3.in");
	inFile.getline(str,100);
	t=atoi(str);
	int* rv = new int[t];
	for (int i = 1; i <= t; ++i) {
		inFile.getline(str, 100);
		int len = strlen(str);
		cout << "Case #" << i<<" "<< endl;
		rv[i] = func(str, len - 2, atoi(&str[len - 2]));
		
	}
	inFile.close();

	ofstream outFile("output.txt");

	for (int i = 1; i <= t; i++) {
		if (rv[i] >= 0) outFile << "Case #" << i << ": " << rv[i] << endl;
		else outFile << "Case #" << i << ": IMPOSSIBLE" << endl;
	}

	outFile.close();
	return 0;
}

