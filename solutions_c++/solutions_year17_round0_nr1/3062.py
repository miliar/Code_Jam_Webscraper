#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>

using namespace std;

int solveCase(string &s, int k) {
    int flips = 0;
   for(int i= 0 ; i < s.length();i++) {
       if(s[i] == '-') {
           ++flips;
           if(i+k-1 < s.length()) {
               for(int j=i;j<i+k;j++) {
                   s[j] = (s[j]=='+')?'-':'+';
               }
           }
           else {
               return -1;
           }
       }
   }
    return flips;
}

int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        string s; int k;
        cin >> s >> k;
        int ans = solveCase(s,k);
        string ans_str = ans==-1?"IMPOSSIBLE": std::to_string(ans);
        cout << "Case #" << (i+1) << ": " << ans_str << endl;
    }

}