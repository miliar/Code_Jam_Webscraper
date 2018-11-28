//============================================================================
// Name        : zadanie2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void) {
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int num;
	cin>>num;
	for(int i=1;i<=num;i++)
	{
		string temp;
		int pos=0;
		cin>>temp;
		int size=temp.size();
		int highest=0;
		bool active=true;
		while(pos<size&&active)
		{
			if(temp[pos]-48>=highest)highest=temp[pos]-48;
			else
			{
				pos--;
				while(temp[pos]-48==highest)pos--;
				pos++;
				temp[pos]=highest+47;

				active=false;
			}
			pos++;
		}
		while(pos<size)
		{
			temp[pos]=9+48;
			pos++;
		}
		if(temp[0]==48&&temp.size()!=1)temp.erase(0,1);
		cout<<"Case #"<<i<<": "<<temp<<"\n";

	}
	return 0;
}
