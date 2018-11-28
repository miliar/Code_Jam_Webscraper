// ConsoleApplication5.cpp : Defines the entry point for the console application.
//
#pragma warning(disable:4996)

#include <stdio.h>
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm> 

#define MAX_SIZE 20
using namespace std;

typedef struct rt_ {
	long long max;
	long long min;
	long long sum;
}ReturnType;
ReturnType func(int iarrl ,int num)
{
	ReturnType rv;
	if (num == 0)
	{
		rv.max = _I64_MAX;
		rv.min = _I64_MAX;
		rv.sum = _I64_MAX;
		return rv;
	}
	if (num == 1)
	{
		if (iarrl % 2 == 0) {rv.max = iarrl / 2; rv.min = iarrl / 2 - 1;}
		else {rv.max = iarrl / 2; rv.min = iarrl / 2;}
		rv.sum = rv.min + rv.max;
		return rv;
	}
	ReturnType temp;
	if (iarrl % 2 == 0)
	{
		
		if (num % 2 == 0) {
			temp = func(iarrl / 2 - 1, num / 2 - 1);
			rv = func(iarrl / 2, num / 2);
		}
		else {
			temp = func(iarrl / 2 - 1, num / 2);
			rv = func(iarrl / 2, num / 2);
		}
		if (rv.sum > temp.sum)return temp;
		else return rv;
	}
	else
	{
		if (num % 2 == 0) {
			temp = func(iarrl / 2, num / 2 - 1);
			rv = func(iarrl / 2, num / 2);
		}
		else {
			temp = func(iarrl / 2, num / 2);
			rv = func(iarrl / 2, num / 2);
		}
		if (rv.sum > temp.sum)return temp;
		else return rv;
	}
}
int main()
{
	int t;
	
	char str[MAX_SIZE];
	ifstream inFile("C-small-2-attempt0.in");
	inFile.getline(str, MAX_SIZE);
	t=atoi(str);
	ReturnType*rv = new ReturnType[t+1];
	for (int i = 1; i <= t; ++i) {
		inFile.getline(str, MAX_SIZE);
		
		int temp =atoi(strtok(str, " "));
		int temp2 = atoi(strtok(NULL, " "));
		strtok(NULL, " ");
		rv[i] = func(temp,temp2);

	}
	inFile.close();

	ofstream outFile("output.txt");
	for (int i = 1; i <= t; i++) {
		outFile << "Case #" << i << ": " << rv[i].max << " " << rv[i].min << endl;
	}
	outFile.close();
	return 0;
}

