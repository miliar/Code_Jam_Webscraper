// round12p2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <strstream>
#include <map>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;



int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	ifstream fin("A-large.in");
	FILE *f2 = fopen("Largeoutput.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		int Npancakes,K;
		string pancakes;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> pancakes;
		char pan[1001];
		Npancakes = pancakes.length();
		pancakes.copy(pan,1001);
		int count = 0;
		bool impossible = false;
		ss >> K;
		for (int j=0;j<Npancakes;++j)
		{
			if (j<= (Npancakes-K)){
			if (pan[j]=='-') 
			{
				++count;
				for (int k=0;k<K;++k)
				{
					if (pan[j+k]=='-' ) pan[j+k]='+';
					else pan[j+k] = '-';
				}
			}
			}
			else
			{
				if (pan[j]=='-') impossible = true; 
			}
		}

		fprintf(f2,"Case #%d: ",i+1);
		//unsigned long pow2Ns = pow(2,Nsnpappers);
		if (impossible) fprintf(f2,"IMPOSSIBLE\n");
		else fprintf(f2,"%d\n",count);

		
        
	    
			
	}
	
  return 0;	
}