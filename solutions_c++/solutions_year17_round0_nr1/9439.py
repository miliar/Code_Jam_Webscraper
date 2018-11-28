#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef double T;
typedef vector<T> VT;
typedef vector<VT> VVT;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    freopen("A.txt", "r", stdin);
    freopen("A.largeOut", "w", stdout);
    
    int t;
    cin >> t;
    
    for(int a = 1; a <= t; a++){
        string s;
        cin >> s;
        int num;
        cin >> num;
        
        int counter = 0;
        
        for(int i = 0; i <= s.size() - num; i++){
            if(s[i] == '-'){
                for(int j = i; j < i + num; j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                counter++;
            }
        }
        
        bool bad = false;
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '-'){
                bad = true;
                break;
            }
        }
        
        if(bad)
            cout << "Case #" << a << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << a << ": " << counter << endl;
    }
    
    return 0;
}


