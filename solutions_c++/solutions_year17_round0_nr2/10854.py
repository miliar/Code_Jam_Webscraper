// GoogleJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <string.h>
#include "stdlib.h"

using namespace std;

int compute(long imput);

int _tmain(int argc, char* argv[])
{
	
	ifstream fichier("C:\\Users\\lilian.verdier\\Downloads\\B-small-attempt0.in", ios::in);  // on ouvre le fichier en lecture
	ofstream resultat("C:\\Users\\lilian.verdier\\Downloads\\result.out", ios::out);

	int count;
	char * ligne = new char;
	long K;
	long result;

 
    if(fichier)  // si l'ouverture a réussi
	{
		fichier >> count;
		for(int i=1;i<=count;i++)
		{
			fichier >> K;

			result = compute(K);

			if(result > -1)
				resultat << "Case #" << i << ": " << result << endl;
			else
				resultat << "Case #" << i << ": " << "IMPOSSIBLE" << endl;

		}

		fichier.close();
		resultat.close();
	}


	return 0;
}

int compute(long input)
{
	while(input)
	{

		char * work_char = new char();
		itoa(input, work_char, 10);

		string work_string(work_char);

		// Verify order
		int previous = -1;
		bool tidy = true;
		for(int iString=0;iString < work_string.length();iString++)
		{
			char c = work_string[iString];
			int numberChar = atoi(&c);

			if(numberChar < previous)
			{
				tidy = false;
				break;
			}
			else
				previous = numberChar;

		}

		if(tidy)
			return input;

		//decrement
		input--;

	}

	return -1;
}