#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
#define MAX 510

long long solve(string s){
    if(s.size()==1){
        return stoll(s);
    }
    for(int i=0;i<s.size()-1;i++){
        if(s[i]>s[i+1]){
            while(i>0&&s[i-1]==s[i]) i--;
            s[i]-=1;
            for(int j=i+1;j<s.size();j++){
                s[j]='9';
            }
            return stoll(s);
        }
    }
    return stoll(s);
}

int main() {
    //freopen("/Users/d/Documents/B-large.in", "rt", stdin);
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        string str;
        cin >> str;
        cout << "Case #" << i << ": ";
        cout << solve(str) << endl;
    }
    return 0;
}
