// ConsoleApplication5.cpp : Defines the entry point for the console application.
//

#include <stdio.h>>
#include "stdafx.h"
#include <math.h>
#include <iostream>
#include <fstream>

#define MAX_SIZE 20
using namespace std;

void minch(char* istr,int i)
{
	if (istr[i] == '0')
	{
		istr[i] = '9'; 
		
		if(i!=0)minch(istr, i - 1);
	}
	else
		istr[i]--;
}
string func(char* istr, int istrl)
{
	char origin[MAX_SIZE];strcpy_s(origin,MAX_SIZE*sizeof(char), istr);


	
	for (int j = 0; istrl - 1 >= j; j++)
	{
		if (istrl == 1) return string(&istr[0]);
		for (int i = istrl - 1; i >= 1; )
		{
			if (istr[i] == '0' ) {
				minch(istr, i);
			}
			else if (istr[i - 1] == '9' && origin[i-1]!='9')
				istr[i] = '9';
			while (istr[i] < istr[i - 1])
			{
				minch(istr, i);
			}
			i--;
		}
	}
	return string(istr);
}
int main()
{
	int t;
	
	char str[MAX_SIZE];
	
	ifstream inFile("B-large.in");
	inFile.getline(str, MAX_SIZE);
	t=atoi(str);
	string* rv = new string[t+1];
	for (int i = 1; i <= t; ++i) {
		inFile.getline(str, MAX_SIZE);
		rv[i] = func(str, strlen(str));
	}
	inFile.close();

	ofstream outFile("output.txt");
	for (int i = 1; i <= t; i++) {
		if (rv[i].at(0) == '0') rv[i].erase(0, 1);
		outFile << "Case #" << i << ": " << rv[i].c_str() << endl;
	}
	outFile.close();
	return 0;
}

