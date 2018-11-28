//============================================================================
// Name        : zadanie3.cpp
// Author      : Draxar
// Version     :
// Copyright   : My CR :)
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
		int pisuary, ludzie, pom;
		cin>>pisuary;
		cin>>ludzie;
		pom=1;
		while((pom-1)<ludzie)pom*=2;
		pom/=2;
		pom--;
		int luka=(pisuary-pom)/(pom+1);
		int wluk=(pisuary-pom)%(pom+1);
		ludzie-=pom;
		if(ludzie<=wluk&&ludzie!=0)luka++;
		cout<<"Case #"<<i<<": ";
		//if(ludzie>0)
		//{
			if(luka%2==0)cout<<luka/2<<" "<<luka/2-1<<"\n";
			else cout<<luka/2<<" "<<luka/2<<"\n";
		//}
		//else
		//{
		//	if(luka%2==0)cout<<luka<<" "<<luka<<"\n";
		//	else cout<<luka+1<<" "<<luka<<"\n";
		//}

	}
	return 0;
}
