//
//  main.cpp
//  codejam1b02
//
//  Created by hyspace on 4/22/17.
//  Copyright © 2017 hyspace. All rights reserved.
//

#include <iostream>
#include <set>
#include <queue>
#include <map>

using namespace std;

string cal(int N, int R, int O, int Y, int G, int B, int V){
    if(R > B + Y) return "IMPOSSIBLE";
    if(Y > B + R) return "IMPOSSIBLE";
    if(B > R + Y) return "IMPOSSIBLE";
    
    multimap<int, char> l;
    l.insert(make_pair(R, 'R'));
    l.insert(make_pair(B, 'B'));
    l.insert(make_pair(Y, 'Y'));
    
    
    int n1, n2, n3;
    char c1, c2, c3;
    string res;
    auto p = l.begin();
    n3 = p->first; c3 = p->second; p++;
    n2 = p->first; c2 = p->second; p++;
    n1 = p->first; c1 = p->second;
    
    for(int i = 0; i < n1; ++i){
        res.push_back(c1);
        if(n2 - i > 0)res.push_back(c2);
        int j = n1 - i;
        if((n3 - j) >= 0)res.push_back(c3);
    }
    return res;
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        int N, R, O, Y, G, B, V;
        cin >> N;
        cin >> R;
        cin >> O;
        cin >> Y;
        cin >> G;
        cin >> B;
        cin >> V;

        cout << "case #" << i + 1 << ": ";
        
        cout << cal(N, R, O, Y, G, B, V) << endl;
    }
    return 0;
}
