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
bool isTidy(int x)
{
	if (x==1000) return false;
	int x1 = x%10;
	int x2 = (x/10)%10;
	int x3 = ((x/10)/10)%10;
	if (x2 > x1 || x3 >x1) return false;
	if (x3 > x2) return false;
	return true;
}
bool isTidy(char *x,int len)
{
for (int i=len-1;i>=0;--i)
	for (int j=i-1;j>=0;--j)
	{
		if (x[j]>x[i]) return false;
	}
return true;
}

/*bool decrement(char *x,int len)
{
	bool done = false; int i=len-1;
while (!done)
{
	if (x[i]>='1') {x[i]=x[i]-1;done=true;}
	else {
		x[i]='9';--i;
	}
}
	if (x[0]=='0'){
		for (int j=0;j<=len-1;++j)
		{
			x[j]=x[j+1];
		}
		return true;
	}
	else return false;

}*/

bool decrement(char *x,int len)
{
	int i =0;
	while ((i < (len-1)) && x[i+1]>=x[i] ) ++i;
	if (i != (len-1)){

		for (int j=i+1;j<len;++j){x[j]='9';}
		

			bool done = false; int k=i;
while (!done && k>=0)
{
	if (x[k]>='1') {x[k]=x[k]-1;done=true;}
	else {
		x[k]='9';--k;
	}
}
	if (x[0]=='0'){
		for (int j=0;j<=len-1;++j)
		{
			x[j]=x[j+1];
		}

		}
	}
	return true;
}

int main(int argc, char* argv[])
{
	int numCases;
	int i,j,k,l,m;
	//ifstream fin("B-large.in");
	ifstream fin("B-large.in");
	FILE *f2 = fopen("B-large.out.txt","w");
	char temp[2000];
	fin >> numCases;
	fin.getline(temp,2000);
	for (i=0;i<numCases;++i)
	{
		int Len;
		char digits[200];
		string dgs;
		fin.getline(temp,2000);
		strstream ss;
		ss << temp;
		ss >> dgs;
		dgs.copy(digits,200);
	
		Len = dgs.length();
			digits[Len]=0;
		string output;
	while(1)
		{
		 if (isTidy(digits,strlen(digits)) ){output.append(digits); break;};
		 decrement(digits,strlen(digits));
			
		}
		
	
		fprintf(f2,"Case #%d: ",i+1);
		//unsigned long pow2Ns = pow(2,Nsnpappers);
		fprintf(f2,output.c_str());
		fprintf(f2,"\n");

		
        
	    
			
	}
	
  return 0;	
}