//
//  main.cpp
//  OversizedPancake
//
//  Created by Loïs Paulin on 08/04/2017.
//  Copyright © 2017 Loïs Paulin. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
	ifstream in ("A.in");
	ofstream out ("A.out");
	int N;
	in >> N;
	int w = 1;
	while(w <= N){
		string s;
		in >> s;
		int flipSize;
		in >> flipSize;
		int nb = 0;
		for (int i=0; i < (int)s.size() - flipSize + 1; ++i){
			if (s[i] == '-'){
				++nb;
				for (int j = i; j < i + flipSize; ++j){
					s[j] = (s[j] == '-') ? '+' : '-';
				}
			}
		}
		bool succ = true;
		for (int i = max(0, (int)s.size() - flipSize + 1); i < (int)s.size(); ++i){
			succ = succ && (s[i] == '+');
		}
		
		out << "Case #" << w << ": ";
		if (succ){
			out << nb << endl;
		}else{
			out << "IMPOSSIBLE" << endl;
		}
		++w;
	}
}
