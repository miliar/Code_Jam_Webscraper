//
//  main.cpp
//  CodeJam1
//
//  Created by Krunoslav Zaher on 4/8/17.
//  Copyright © 2017 Bellabeat. All rights reserved.
//

#include <stdio.h>
#include <vector>
using namespace std;

auto inputFilename = "/Users/kzaher/Projects/codejam/CodeJam1/TidyNumbers/Test1.txt";
auto outputFilename = "/Users/kzaher/Projects/codejam/CodeJam1/TidyNumbers/Test1.output.txt";

FILE *input = fopen(inputFilename, "rb");
FILE *output = fopen(outputFilename, "wb");

#define IN(...) fscanf(input, ##__VA_ARGS__)
#define OUT(...) fprintf(output, ##__VA_ARGS__)

int solve(vector<int> data) {
    for (int i = 0; i < data.size() - 1; ++i) {
        if (data[i] > data[i + 1]) {
            for (int j = i + 1; j < data.size(); ++j) {
                data[j] = 9;
            }
            data[i] = data[i] - 1;
            if (i >= 1) {
                i -= 2;
            }
        }
    }

    int i = 0;
    while (data[i] == 0 && i < data.size()) {
        ++i;
    }
    
    for (; i < data.size(); ++i) {
        OUT("%c", data[i] + '0');
    }
    return 0;
}

int main(int argc, const char * argv[]) {

    int count;
    IN("%d\n", &count);

    for (int i = 0; i < count; ++i) {
        vector<int> data;

        char c;
        while(1) {
            fscanf(input, "%c", &c);
            if (c == '\n') {
                OUT("Case #%d: ", i + 1);
                solve(data);
                OUT("\n");
                break;
            }

            data.push_back(c - '0');
        }
    }

    fclose(output);
    fclose(input);
    
    return 0;
}
