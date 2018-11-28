//  Created by Luna_Z on 17/4/6.
//  Copyright © 2017 Luna_Z. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include "math.h"
using namespace std;

static int case_count;
char const* input_path = "C:\\Users\\Luna\\Desktop\\input.in";
char const* output_path = "C:\\Users\\Luna\\Desktop\\output.out";

std::string func(int R, int C, vector<string> arg) {
	int a,b;
	vector<string> tmp;
	vector<int> filled(R, 0);
	int to_fill, front, last_filled = 0;
	char filler = '?';
	
	
	for(a = 0; a< R; a ++){
		string s = arg[a];
		front = 0;
		for(b = 0; b < C; b++){
			if(s[b] != '?'){
				filled[a] = 1;
				filler = s[b];
				for(to_fill = front; to_fill < b; to_fill++){
					s[to_fill] = s[b];
				}
				front = b+1;
			}
			if(b == C - 1){
			 if( filled[a] == 1){
				for (to_fill = front; to_fill < C; to_fill++) 
					s[to_fill] = filler;
				}
			}
		}
		arg[a] = s;
	}
	front = 0;
	for(a = 0; a < R; a ++){	
		if(filled[a] != 0){
			for (to_fill = front; to_fill < a; to_fill++){
				arg[to_fill] = arg[a];
			}
			front = a+1;
			last_filled = a;
		}
		if(a == R - 1)
			for (to_fill = front; to_fill < R; to_fill++) {
				arg[to_fill] = arg[last_filled];
		}	
	}

	string ans;
	for(a = 0; a < R; a ++){
		ans += arg[a];
		ans += '\n'; 
	}
	return ans;
}

int main() {

	//read the input file and pass the arguemnt to function

	FILE *inf = fopen(input_path, "r");
	if(inf == NULL){
		printf("Could not find input file! \n");
		getchar();
		return 1;
	}

	FILE *of = fopen(output_path, "w");
	if (of == NULL) {
		printf("The path of output file has errors! \n");
		getchar();
		return 1;
	}
	
	fscanf(inf, "%d", &case_count);

	int cnt, i, j;
	int R,C;
	char arg1[30];	
	vector<string> cake;
	
	for (cnt = 1; cnt < case_count + 1; cnt++) {
		//write output
		fscanf(inf, "%d", &R);
		fscanf(inf, "%d", &C);
		cake.clear();
		for(i = 0; i < R; i++){
			fscanf(inf, "%s", arg1);
			cake.push_back(arg1);	
		}
		fprintf(of, "Case #%d:\n%s", cnt, func(R,C, cake).c_str());
	}
	fclose(inf);
	fclose(of);

	return 0;
}
