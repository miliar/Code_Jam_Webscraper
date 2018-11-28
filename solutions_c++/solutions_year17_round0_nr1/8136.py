// GoogleCodeJam.cpp : Defines the entry point for the console application.
//
// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int myswap(string& S, int i,int k)
{
	int total = k + i;

	//string S = Str;
   for(int count=i; count<total;count++)
   {  
	//   if (S.at(count) == 'a')
	   S[count] = (S[count]=='-' )? S[count] = '+' : S[count] = '-';
   }
   return 0;
}

int main()
{
	int numbers[1000];
	int numbercount;
	int casecount;
	int k;
	string line;
	cin >> casecount;
	getline(cin, line);

	for (int i=0; i < casecount; i++)
	{
		getline(cin, line);
		int swapcount = 0;
		string sub;
		string s; 
		istringstream iss(line);
		iss >> sub;
		s = sub;
		iss >>  sub;
		k=stoi(sub);
		int npancakes = s.length();
		int totalj = (npancakes + 1 - k);
		for (int j = 0; j < totalj; j++)
		{
			if(s[j]=='-') 
			{
				
				myswap(s, j, k);
				swapcount++;
			}

		}
		int icount = totalj;
		bool bstop = false;
		do 
		{
			bstop = (s[icount] == '-') ;
			icount++;
		
		} while (!bstop & (icount <= npancakes));
		if (bstop)
     		cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		else 
			cout << "Case #" << i + 1 << ": " << swapcount << endl;

	}
	return 0;
}

