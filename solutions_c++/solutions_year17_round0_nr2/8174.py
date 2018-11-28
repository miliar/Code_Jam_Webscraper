//
//  main.cpp
//  GCJ 2017 Qualification Round - Problem B. Tidy Numbers
//
//  Created by Arturo Martin-de-Nicolas on 4/8/17.
//  Copyright © 2017 ___Arturo_Martin-de-Nicolas___. All rights reserved.
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;

static size_t tidy(string & S, size_t p, size_t L) {
	for(size_t i=p+1; i<L; ++i) {
		if (S[i-1] > S[i]) {
			--S[i-1];
			p = tidy(S,p,i-p);
			do { S[i++] = '9'; } while(i<L);
			return p + (S[p] == '0');
		}
	}
	return p;
}

int main()
{
    int T;
    cin >> T;

    for (int i=0; i<T; ++i)
    {
		string S;
		cin >> S;
		cout << "Case #" << (i+1) << ": " <<
			S.substr(tidy(S,0,S.length())) << '\n';
    }
}
