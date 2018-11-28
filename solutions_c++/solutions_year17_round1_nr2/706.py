//
//  main.cpp
//  question 2
//
//  Created by Shuying Sun on 4/14/17.
//  Copyright © 2017 Shuying Sun. All rights reserved.
//

#include <iostream>
using std::cout; using std::endl; using std::cin;
using std::max; using std::min;
using std::string;
using std::ostream;
using std::pair;
using std::make_pair;
#include <fstream>
using std::ofstream;
using std::ifstream;
#include <unordered_map>
using std::unordered_map;
#include <queue>
using std::queue;
#include <stack>
using std::stack;
#include <map>
using std::map;
#include <vector>
using std::vector;
#include <set>
using std::vector;
#include <unordered_set>
using std::unordered_set;
using std::multiset;
using std::unordered_multiset;

using std::priority_queue;

int lower(int& gram, int& base){
    float a = gram/1.1/base;
    if (a == int(a)) return a;
    return int(a)+1;
}

int upper(int& gram, int& base){
    float a = gram/0.9/base;
    return a;
}


int maximum_kits(vector<vector<int>>& packages, vector<int>& bases, int& num){
    //vector< priority_queue< pair<int,int>,vector<pair<int,int>>,std::greater<pair<int,int>>> > servings(num);
    vector<vector<pair<int,int>>> servings(num);
    
    for (int i = 0; i < num; ++i){
        for (int j = 0; j < packages[0].size(); ++j){
            int l =lower(packages[i][j],bases[i]), r = upper(packages[i][j],bases[i]);
            if (l <= r) servings[i].push_back(make_pair(l,r));
        }
    }
    for (int i = 0; i < num; ++i){
        sort(servings[i].begin(),servings[i].end());
    }
    /*
    for (int i = 0; i < num; ++i){
        cout << "for ingredient " << i << endl;
        for (int j = 0; j < servings[i].size(); ++j){
            cout << servings[i][j].first << "\t" << servings[i][j].second << endl;
        }
    }
    */
    int res = 0;
    vector<int> indices(num,0);
    while (true){
        for (int i = 0; i < num; ++i) if (indices[i] == servings[i].size()) return res;
        int right = servings[0][indices[0]].second, left = servings[0][indices[0]].first;
        bool found = true;
        for (int i = 1; i < num; ++i){
            if (servings[i][indices[i]].second < left){
                indices[i]++;
                found = false;
                break;
            }
            if (servings[i][indices[i]].first > right){
                for (int prev = 0; prev < i; ++prev) indices[prev]++;
                found = false;
                break;
            }
            right = max(right,servings[i][indices[i]].second);
            left = min(left,servings[i][indices[i]].first);
        }
        if (found){
            res += 1;
            for (int i =0; i < num; ++i) indices[i]++;
        }
    }
    return res;
    
    
}





int main(int argc, const char * argv[]) {
    int T = 0;
    ifstream file;
    file.open("/Users/shuyingsun/Downloads/B-large.in-2.txt");
    file >> T;
    ofstream output;
    output.open("/Users/shuyingsun/Desktop/q2_output.txt");
    for (int i = 1; i <= T; ++i){
        int N, P;
        file >> N >> P;
        vector<vector<int>> packages(N);
        vector<int> bases{};
        for (int i = 1; i <= N; ++i){
            int temp;
            file >> temp;
            bases.push_back(temp);
        }
        for (int i = 1; i <= N; ++i){
            for (int j = 1; j <= P; ++j){
                int temp;
                file >> temp;
                packages[i-1].push_back(temp);
            }
        }
        int res = maximum_kits(packages, bases, N);
        output << "Case #" << i<<": " << res << "\n";
    }
    file.close();
    output.close();
    return 0;
    
}
