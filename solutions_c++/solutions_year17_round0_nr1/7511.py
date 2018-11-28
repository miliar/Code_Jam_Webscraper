//
//  cakeFlip.cpp
//  GoogleCodeJam2017
//
//  Created by nastia on 08/04/2017.
//  Copyright © 2017 Anastasiia Soboleva. All rights reserved.
//

#include <stdio.h>
#include <fstream>
using namespace std;

int flips(char *pancakes, int flipper_size) {
	
	int string_size = (int)strlen(pancakes);
	
	int result = 0;
	
	for (int i = 0; i < string_size - flipper_size + 1; i++) {
		if (*(pancakes + i) == '-') {
			for (int j = i; j < i + flipper_size; j++) {
				*(pancakes + j) = *(pancakes + j) == '+' ? '-' : '+';
			}
			result += 1;
			
		}
	}
	
	for (int k = 0; k < string_size; k++) {
		if (*(pancakes + k) == '-') {
			return -1;
		}
	}
	
	return result;
}

//int main_(int argc, const char * argv[]) {
//	
//	int t;
//	scanf("%d", &t);
//	
//	char *pancakes = (char *)malloc(sizeof(char) * 1000);
//	int size = 0;
//	
//	for (int i = 0; i < t; i++) {
//		
//		scanf("%s %d", pancakes, &size);
//		int result = flips(pancakes, size);
//		if (result == -1) {
//			printf("Case #%d: IMPOSSIBLE\n", i + 1);
//		} else {
//			printf("Case #%d: %d\n", i + 1, result);
//		}
//		
//	}
//	
//	free(pancakes);
//	
//	return 0;
//}

int main(int argc, const char * argv[]) {
	//ifstream inputfile;
	ofstream outputFile;

	outputFile.open("/Users/nastia/Developer/GoogleCodeJam2017/res.out",std::ios_base::in);
//inputfile.open("/Users/nastia/Downloads/A-small-attempt1.in.txt");

//	int t;
//	inputfile >> t;

	int t;
	scanf("%d", &t);
	
	char *pancakes = (char *)malloc(sizeof(char) * 1000);
	int size = 0;
	
	for (int t_i = 1; t_i <= t; t_i++) {
		scanf("%s %d", pancakes, &size);

		int result = flips(pancakes, size);
		if (result == -1) {
			outputFile << "Case #" << t_i << ": " << "IMPOSSIBLE" << endl;
		} else {
			outputFile << "Case #" << t_i << ": " << result << endl;
		}
		
	}


//	inputfile.close();
	outputFile.close();

	return 0;
}
