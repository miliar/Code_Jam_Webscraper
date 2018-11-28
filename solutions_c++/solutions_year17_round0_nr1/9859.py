//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Akshay Mathur on 08/04/17.
//  Copyright © 2017 Akshay Mathur. All rights reserved.
//



#include <iostream>
#include <string>
#include<algorithm>
#include<iterator>
using namespace std;


void flip(string::iterator &i, int m){
    std::transform(i , i+m, i, [&](char i){
        if(i == '+')
            return '-';
        else
            return '+';
    });
}

int distance(string str, int m){
    int count = 0 ;
    auto i = str.begin();
    while(i != str.end()){
        if(*i == '+'){
            i++;
            continue;
        }
        else if(i+m <= str.end()){
            flip(i, m);
            count ++;
        }
        i++;
    }
    auto itr = find_if(str.begin(), str.end(), [](char c){
        if(c== '-')
            return true;
        else
            return false;
    });
    if(itr != str.end())
        count = -1;
    return count;
}

int main(int argc, const char * argv[]) {
	int t, m;
	string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> s >> m;  // read n and then m.
    int ans = distance(s, m);
    if(ans < 0)
    cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    else
    cout << "Case #" << i << ": " << ans << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
    return 0;
}
