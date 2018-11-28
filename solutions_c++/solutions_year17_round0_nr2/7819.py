//
//  main.cpp
//  tidyNumbers
//
//  Created by Loïs Paulin on 08/04/2017.
//  Copyright © 2017 Loïs Paulin. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
	
	int N;
	cin >> N;
	int w = 1;
	while(w <= N){
		string s;
		cin >> s;
		
		int i = 1;
		while((s[i] >= s[i-1]) && i < (int)s.size()){
			++i;
		}
		
		if (i == (int)s.size()){
			cout << "Case #" << w << ": " << s << endl;
			++w;
			continue;
		}
		
		--i;
		
		while(i > 0 && s[i] == s[i-1])
			--i;
		
		s[i] -= 1;
		
		for (i = i+1; i < (int)s.size(); ++i){
			s[i] = '9';
		}
		cout << "Case #" << w << ": ";
		
		i = 0;
		while(s[i] == '0')
			++i;
		
		while (i < (int)s.size()){
			cout << s[i];
			++i;
		}
		cout << endl;
		
		++w;
	}
    return 0;
}

