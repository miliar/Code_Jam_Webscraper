//
//  main.cpp
//  CodeJam1
//
//  Created by Krunoslav Zaher on 4/8/17.
//  Copyright © 2017 Bellabeat. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <map>
#include <cassert>
using namespace std;

auto inputFilename = "/Users/kzaher/Projects/codejam/CodeJam1/Stalls/Test1.txt";
auto outputFilename = "/Users/kzaher/Projects/codejam/CodeJam1/Stalls/Test1.output.txt";

FILE *input = fopen(inputFilename, "rb");
FILE *output = fopen(outputFilename, "wb");

#define IN(...) fscanf(input, ##__VA_ARGS__)
#define OUT(...) fprintf(output, ##__VA_ARGS__)

pair<long long, long long> solve(long long space, long long howMany) {
    map<long long, long long> map;

    map[space] = 1;

    while (howMany > 0) {
        auto max = map.rbegin()->first;

        auto smaller_bucket = (max - 1) / 2;
        auto larger_bucket = (max - 1) - smaller_bucket;

        auto max_bucket_space = map.rbegin()->second;
        if (howMany <= max_bucket_space) {
            return make_pair(larger_bucket, smaller_bucket);
        }
        else {
            howMany -= max_bucket_space;

            map.erase(prev(map.end()));

            if (map.find(smaller_bucket) != map.end()) {
                map[smaller_bucket] = map[smaller_bucket] + max_bucket_space;
            }
            else {
                map[smaller_bucket] = max_bucket_space;
            }

            if (map.find(larger_bucket) != map.end()) {
                map[larger_bucket] = map[larger_bucket] + max_bucket_space;
            }
            else {
                map[larger_bucket] = max_bucket_space;
            }
        }
    }

    assert(false);
    
    return make_pair(0, 0);
}

int main(int argc, const char * argv[]) {

    int count;
    IN("%d\n", &count);

    for (int i = 0; i < count; ++i) {
        long long space;
        long long howMany;
        IN("%lld %lld", &space, &howMany);
        auto result = solve(space, howMany);
        OUT("Case #%d: %lld %lld\n", i + 1, get<0>(result), get<1>(result));
    }

    fclose(output);
    fclose(input);
    
    return 0;
}
