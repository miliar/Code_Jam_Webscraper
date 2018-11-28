#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
//#include <unordered_map>
#include <list>
#include <bitset>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <fstream>
#include <bitset>

using namespace std;

const int me = 1025;

long long T, N;

long long convert(string s){
    long long v = 0;
    for(char i : s)
        v = 10 * v + i - '0';
    return v;
}
bool good(long long N){
    string s = to_string(N);
    for(int i = 1; i < (int)s.size(); i ++)
        if(s[i] < s[i - 1])
            return false;
    return true;
}

int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> N;
        while(!good(N)){
            string s = to_string(N);
            int pos = -1;
            for(int i = 1; i < (int)s.size(); i ++)
                if(s[i] < s[i - 1]){
                    pos = i;
                    break;
                }
            for(int i = pos; i < (int)s.size(); i ++)
                s[i] = '0';
            N = convert(s) - 1;
        }
        cout << "Case #" << c + 1 << ": " << N << endl;
    }
    
    return 0;
}
