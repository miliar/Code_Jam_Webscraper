//
//  main.cpp
//
//
//  Created by dmp on 5/3/13.
//  Copyright (c) 2013 dmp. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <functional>   // std::greater

using namespace std;

const bool bTestRun = false;

void decrement( string& s,  int pos)
{
	if( s[pos] == '0') {
		s[pos] = '9';
		decrement(s, pos + 1);
		return;
	}
	
	s[pos]--;
	if((s[pos] == '0') && (pos == s.length() - 1)) {
		s.pop_back();
	}
}

void processCase()
{
	string s;
	cin >> s;
	
	s = string(s.rbegin(), s.rend());
	

	int pos = 0;
	
	// at least 2 digits
	while( pos + 2 <= s.length() ) {
		
		if( s[pos] < s[pos + 1]) {
			decrement(s, pos + 1);
			for(int i = 0; i <= pos; i++) {
				s[i] = '9';
			}
		}
		
		pos++;
	}
	
	string r = string(s.rbegin(), s.rend());
	cout << r;
}


void tests()
{
	string s = "0001";
	
	decrement(s, 3);
}

int main(int argc, const char * argv[])
{
	int T;
	streambuf	*cinbuf;
	ifstream	*in;
	
	
	tests();
	
	srand((int)time(0));
	std::ios::sync_with_stdio(false);

	if(bTestRun) {
		in = new ifstream("TestCase.in");
		cinbuf = std::cin.rdbuf(); //save old buf
		cin.rdbuf(in->rdbuf());
		cerr << "\n******: Using data from TestCase.in ******\n\n";
	}
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		processCase();
		printf("\n");
	}
	
	if(bTestRun) {
		cin.rdbuf(cinbuf);   //reset to standard input again
	}
	
    return 0;
}
