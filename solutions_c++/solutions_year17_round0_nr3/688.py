//
//  main.cpp
//  test
//
//  Created by Shuying Sun on 2/28/17.
//  Copyright © 2017 Shuying Sun. All rights reserved.
//

#include <iostream>
using std::cout; using std::endl; using std::cin;
using std::string;
using std::ostream;
using std::pair;
using std::make_pair;
#include <fstream>
using std::ofstream;
using std::ifstream;


#include <queue>
using std::priority_queue;
#include <map>
using std::map;



pair<long,long> get_last_one(long N, long K){
    map<long,long> cnt{};
    cnt[N] = 1;
    long arranged = 0;
    while (arranged < K){
        if (cnt.empty()) return make_pair(0,0);
        pair<long,long> largest = *cnt.rbegin();
        arranged += largest.second;
        if (arranged  >= K){
            if (largest.first % 2 == 1) return make_pair(largest.first/2, largest.first/2);
            else return make_pair(largest.first/2,largest.first/2-1);
        }
        cnt.erase(largest.first);
        if (largest.first % 2 ==1 && largest.first  != 1){
            cnt[largest.first/2] += 2*largest.second;
        }
        if (largest.first % 2 == 0){
            cnt[largest.first/2] += largest.second;
            if (largest.first != 2) cnt[largest.first/2-1] += largest.second;
        }
    }
    return make_pair(0,0);
}
int main(int argc, const char * argv[]) {

    int T = 0;
    ifstream file;
    file.open("/Users/shuyingsun/Downloads/C-large.in.txt");
    file >> T;
    ofstream output;
    output.open("/Users/shuyingsun/Desktop/bathroom_output_large.txt");
    for (int i = 1; i <= T; ++i){
        long N, K;
        file >> N >> K;
        pair<long,long> res = get_last_one(N,K);
        output << "Case #" << i<<": " << res.first<<" " << res.second << "\n";
    }
    file.close();
    output.close();
    return 0;
    
}
