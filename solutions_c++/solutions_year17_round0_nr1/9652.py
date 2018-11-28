#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <climits>
#include <map>
#include <set>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <deque>
#include <string> 
#include <sstream>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>

using namespace std;

string x;
int k;

bool ok(){
    for (int i = 0; i < (int)x.size(); ++i){
        if(x[i] == '-') return 0;
    }
    return 1;
}
int main(){
    ios::sync_with_stdio(false); cin.tie(0);
    int t; cin >> t;
    for (int caso = 1; caso <= t; ++caso){
        cin >> x >> k;
        int ans = 0;
        int r = 0;
        for (int i = 0; i < (int)x.size()-k+1; ++i){
            if(x[i] == '-'){
                r++;
                for (int j = i; j < i+k; ++j){
                    if(x[j] == '+'){
                        ans--;
                        x[j] = '-';
                    }else{
                        ans++;
                        x[j] = '+';
                    }
                }
            }
        }
        cout << "Case #" << caso << ": ";
        if(ok()) cout << r << "\n";
        else cout <<"IMPOSSIBLE\n";
    }
    return 0;
}

