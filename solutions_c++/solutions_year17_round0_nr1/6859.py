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

void flip(string &s, size_t t, size_t k )
{
	for(size_t i = t, c = 0; c < k; c++, i++)
	{
		if(s[i] == '+') s[i] = '-'; else s[i] = '+';
	}
}

void processCase()
{
	string s;
	int K;
	
	cin >> s;
	cin >> K;
	
	int flips = 0;
	
	for( size_t i = 0; i < s.length() - K; i++) {
		if( s[i] == '+') continue;
		flip(s, i, K);
		flips++;
	}
	
	char c = s[s.length() - K ];
	
	for( int i = 1; i < K; i++) {
		if( c != s[s.length() - K + i]) {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	
	if(c == '-') flips++;
	
	cout << flips;
}

int main(int argc, const char * argv[])
{
	int T;
	streambuf	*cinbuf;
	ifstream	*in;
	
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
