// Question 2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<string.h>
#include<conio.h>
using namespace std;
int main()
{
	ifstream fin("B-small-attempt0.in",ios::in);
	ofstream fout("A-small.out",ios::out);
	int tcase,k,j,u,l;
	char arr[20],tarr[20];
	fin>>tcase;
	for(int i=0;i<tcase;i++)
	{
		j=0;
		fin>>arr;
		for(int j=strlen(arr)-1;j>=0;)
		{
			k=atoi(arr);
			u=arr[j]-'0';
			l=arr[j-1]-'0';
			if(u>=l)
				j--;
			else
			{
				k--;
				itoa(k,tarr,10);
				if(strlen(tarr)<strlen(arr))
					j--;
				itoa(k,arr,10);
			}
		}
		fout<<"Case #"<<i+1<<": "<<k<<endl;
	}
	fin.close();
	fout.close();
	getch();
}