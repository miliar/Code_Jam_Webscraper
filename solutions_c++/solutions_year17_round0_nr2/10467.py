// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

#include <iostream>
using namespace std;
#define ll long long int

bool solve(ll num)
{
    ll next=num%10;
    num=num/10;
    while(num)
    {
        ll digit=num%10;
        if (digit>next)
            return false;
        next=digit;
        num=num/10;
    }
    return true;
}
int main() {
	std::ifstream fin("input.txt");
	std::ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++)
	{
		ll n;
		fin>>n;
		for(ll j=n;j>=0;j--)
		{
			bool flag=solve(j);
			if(flag==true)
			{
				fout<<"Case #"<<i<<": "<<j<<"\n";
				break;
			}
		}
	}
	return 0;
}
