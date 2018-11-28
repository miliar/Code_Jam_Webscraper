//============================================================================
// Name        : zadanie1.cpp
// Author      : Draxar
// Version     :
// Copyright   : Your copyright notice
// Description :
//============================================================================

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

struct panc{
	double height, radius, rvalue, hvalue;
	bool used=false;

};
panc *pancs;


int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int num;
	cin>>num;
	int stack;
	int p;
	for(int k=1;k<=num;k++)
	{
		double ret=0;
		double currentRval=0;
		cin>>p;
		cin>>stack;
		pancs=new panc[p];


		for(int i=0;i<p;i++)
		{
			cin>>pancs[i].radius;
			cin>>pancs[i].height;
			pancs[i].hvalue=pancs[i].radius*2*pancs[i].height;
			pancs[i].rvalue=pancs[i].radius*pancs[i].radius;
		}

		for(int j=stack;j>0;j--)
		{
			int chosen=-1;
			double val=0;
			for(int i=0;i<p;i++)
			{
				if(!pancs[i].used)
				{
					double thisVal=pancs[i].hvalue;
					if(currentRval<pancs[i].rvalue)thisVal+=pancs[i].rvalue-currentRval;
					if(val<thisVal)
					{

						chosen=i;
						val=thisVal;
					}
				}
			}
			if(currentRval<pancs[chosen].rvalue)currentRval=pancs[chosen].rvalue;
			pancs[chosen].used=true;
		}
		double hrval=0;
		for(int i=0;i<p;i++)
		{
			if(pancs[i].used)
			{
				ret+=pancs[i].hvalue;
				if(hrval<pancs[i].rvalue)hrval=pancs[i].rvalue;
			}
		}
		ret+=hrval;
		cout.precision(9);
		cout<<"Case #"<<k<<": "<< fixed << ret*M_PI <<"\n";
	}
}
