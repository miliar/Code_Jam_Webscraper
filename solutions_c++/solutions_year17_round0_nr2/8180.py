/*
 * GCJ_17_B.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: neeraj
 */


#include<iostream>
#include <fstream>
using namespace std;
typedef long long int lli;
bool increasingDigits(lli input)
{
    int lastSeen = 10; // always greater than any digit
    int current;

    while (input > 0) {
        current = input % 10;
        if (lastSeen < current)
            return false;
        lastSeen = current;
        input /= 10;
    }
    return true;
}


int main()
{
	int t;

	ifstream fin;
	ofstream fout;
	fin.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/B-small-attempt0.in", ios::in);
	fout.open("/Users/neeraj/Documents/codeblocks/Progs New/spoj/GoogleCodeJam/B-small-out.txt",ios::trunc);

	fin>>t;
	for(int test=1;test<=t;test++)
	{
		lli num;
		fin>>num;
		lli i;
		for(i=num;i>=2;i--) {
			if(increasingDigits(i))
				break;
		}
		fout<<"Case #"<<test<<": "<<i<<endl;
	}
}
