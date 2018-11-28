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
#include <map>
#define rep(i,a,b) for(i=a;i<b;i++)
#define repz(i,n) rep(i,0,n)


using namespace std;



int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	ifstream fin("C-large.in");
	FILE *f2 = fopen("C-large.out.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		long long unsigned N,K,count,output;
		count = 0;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> N;
		ss >> K;
		std::map<long long unsigned,long long unsigned> gaps;
		gaps.insert(std::pair<long long unsigned,long long unsigned>(N,1));
		bool found = false;
		if (K == N) {count = K;output=1;}
		
		while (count<K)
		{
			std::map<long long unsigned,long long unsigned>::reverse_iterator it1 = gaps.rbegin();
	
			std::vector<long long unsigned> keys,values;
			long long unsigned x=0;
			for (it1=gaps.rbegin(); it1!=gaps.rend(); ++it1)
			{
				keys.push_back(it1->first);
				values.push_back(it1->second);
				x += (it1->first*it1->second);
			}
	
			x += count;
			for (int i=0;i<keys.size();++i)
			{
	
			 long long unsigned gp = keys[i];
			 long long unsigned cnts = gaps[gp];
			 long long unsigned newgp1 = (gp-1)/2;
			 long long unsigned newgp2 = gp-1-newgp1;
			 gaps.erase(keys[i]);
	
			 count+= cnts;
			 if (count >= K) {output = gp;found=true;break;}
			  
			std::map<long long unsigned,long long unsigned>::iterator it = gaps.begin();		 
			 it = gaps.find(newgp1);
			 if (it != gaps.end())  {
				 gaps[newgp1] += cnts;
			}
			
			 else
			 {
				if (newgp1>0) gaps.insert(std::pair<long long unsigned,long long unsigned>(newgp1,cnts));
			 }
			 it = gaps.find(newgp2);
			 if (it != gaps.end())  {
				 gaps[newgp2] += cnts;
			}
			 else
			 {
				 if (newgp2>0) gaps.insert(std::pair<long long unsigned,long long unsigned>(newgp2,cnts));
			 }
		
					
			}
			if (found) break;
		}


		long long unsigned op1,op2;
		op1= (output-1)/2;
		op2= output-1-op1;

		fprintf(f2,"Case #%d: ",i+1);
		fprintf(f2,"%llu %llu\n",op2,op1);

		
        
	    
			
	}
	
  return 0;	
}