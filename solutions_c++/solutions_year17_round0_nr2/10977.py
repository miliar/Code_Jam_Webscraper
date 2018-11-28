//
//  main.cpp
//  Tidy
//
//  Created by Muhammad Ashar on 4/9/17.
//  Copyright © 2017 Muhammad Ashar. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {
	const char* inputFileName = "/users/muhammadashar/desktop/input.txt";
	const char* outputFileName = "/users/muhammadashar/desktop/output.txt";
	FILE* inputFile = fopen(inputFileName, "r");
	FILE* outputFile = fopen(outputFileName, "w");
	if(inputFile == NULL || outputFile == NULL) {
		return 0;
	}
	char line[100];
	fgets(line, sizeof(line), inputFile);
	int t = atoi(line);
	for(int index = 0; index < t; index++) {
		fgets(line, sizeof(line), inputFile);
		long long n = atoll(line);
		for(long long subIndex = n; subIndex >= 1; subIndex--) {
			sprintf(line, "%llu", subIndex);
			int size = (int) strlen(line);
			bool found = true;
			for(int i = size - 2; i >= 0; i--) {
				if(line[i] <= line[i + 1]) {
					continue;
				} else {
					found = false;
					break;
				}
			}
			if(found) {
				sprintf(line, "Case #%d: %llu\r\n", index + 1, subIndex);
				printf("%s", line);
				fwrite(line, strlen(line), 1, outputFile);
				break;
			}
		}
	}
	fclose(inputFile);
	fclose(outputFile);
	return 0;
}
