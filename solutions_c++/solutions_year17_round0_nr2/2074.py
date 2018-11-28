#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>
#include <unordered_map>
#include <fstream>
#define ll long long
#define F first
#define S second
#define MOD 1000000007
#define MAX 200001
#define BUGGY 0
using namespace std;
bool isTidy(string s) {
    for (int i = 1;i < s.length(); ++i) if (s[i] < s[i - 1]) return false;
    return true;
}
string getAllNines(int l) {
    string s = "";
    while(l--) s += "9";
    return s;
}
long long solve(string s) {
    long long intVal = atoll(s.c_str());
    if (isTidy(s)) {
        return intVal;
    }
    long long mx = -1;
    int l = s.length();
    string cnv;
    for (int i = 0;i < l; ++i) {
        cnv = s.substr(0, i + 1) + getAllNines(l - i - 1);
        if (isTidy(cnv) && atoll(cnv.c_str()) <= intVal) mx = max(mx, atoll(cnv.c_str()));
        if (s[i] > '0') {
            cnv = s.substr(0, i) + (char)(s[i] - 1) + getAllNines(l - i - 1);
            if (isTidy(cnv) && atoll(cnv.c_str()) <= intVal) mx = max(mx, atoll(cnv.c_str()));
        }
    }
    return mx;
}
int main(){
    ifstream cin("/Users/shikhar.s/Downloads/B-large.in");
    //ifstream cin("/Users/shikhar.s/Desktop/Competitive/Competitive/a.txt");
    ofstream cout("/Users/shikhar.s/Desktop/Competitive/Competitive/b.txt");
    int t;
    cin >> t;
    int T = 1;
    while (t--) {
        string s;
        cin >> s;
        cout << "Case #" << T++ << ": " << solve(s) << "\n";
    }
    printf("Done!");
    return 0;
}

