// CodeJam_problemset_cpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<fstream>
#include<ostream>
#include<cstring>
#include<math.h>


using namespace std;

int min = -1;

char* toS(long long x)
{
	char a[20] = { 0 };
	int m = 0;
	bool s = false;
	for (size_t i = 1; i < 21; i++)
	{
		long long u = powl(10, 20 - i);
		int t = x / u;
		if (t!=0 || s)
		{
			s = true;
			a[m] = t+48;
			x %= u;
			m++;
		}
		
	}
	return a;
}

long long SuggestTidy(long long x) {

	char* str = (char*)malloc(20);
	strcpy(str, toS(x));
	//sprintf(str, "%l", x);
	// itoa(x, str,10);
	
	 int len = strlen(str) - 1;
	 
	for (int i = 0; i < len; i++)
	{
		 char a[] = { str [ i],0 };
		 char b[] = { str [ i+1],0 };
		
		if (atoi( a)>atoi(b))
		{
			
			long long mod = x%((long long)powl(10, len - i));
			mod++;
			return x - mod;
		}
	}
	return x;
}

int main() {

	ifstream myReadFile;
	myReadFile.open("B-large.in");
	ofstream outFile;
	outFile.open("out.txt");
	const int len = 10000;
	char output[len];
	int i = 1;
	myReadFile.getline(output, len);

	int T= atoi(output );
	if (myReadFile.is_open()) {
		while (!myReadFile.eof() && i <= T) {

			myReadFile.getline(output, len);
			//char* Str = strtok(output, " ");
			long long N = atoll(output);
			//double S = atoi(strtok(NULL, " "));
			outFile << "Case #" << i << ": ";
		
			while (N >0)
			{
				long long tmp = SuggestTidy(N);
				if (tmp==N)
				{
					break;
				}
				N = tmp;
				
			}
			
			outFile <<N<< endl;
			i++;
		}
	}
	myReadFile.close();
	outFile.close();
	return 0;
}
