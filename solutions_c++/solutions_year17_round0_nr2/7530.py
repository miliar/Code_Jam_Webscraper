//
//  main.cpp
//  Tidy
//
//  Created by Volodymyr Tkachuk on 4/8/17.
//  Copyright © 2017 Volodymyr Tkachuk. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

const auto inputFile = "/Users/volodymyr/Downloads/B-large.in";
const auto outputFile = "/Users/volodymyr/Downloads/out.txt";

int main() {
    ifstream input(inputFile);
    ofstream output(outputFile);

    int T;
    input >> T;
    for (auto t = 1; t <=T; ++t) {
        long long n;
        input >> n;
        long long d = 1;
        long long ans = 0;
        long long pc = 9;
        while (n > 0) {
            long long cc = n%10;
            if (cc > pc) {
                --cc;
                ans = d-1;
            }
            pc = cc;
            ans += cc*d;
            d *= 10;
            n /=10;
        }
        output << "Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
