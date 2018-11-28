#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<ctime>
#include<vector>
#include<fstream>
#include<list>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define ms(s) memset(s,0,sizeof(s))

const double PI = 3.141592653589;
const int INF = 0x3fffffff;

string in;

void re(int idx) {
    if(in[idx] == '+')
        in[idx] = '-';
    else
        in[idx] = '+';
}

int main() {
//            freopen("/Users/really/Documents/code/A-small-attempt2.in","r",stdin);
//            freopen("/Users/really/Documents/code/output","w",stdout);
    ios::sync_with_stdio(false);
    
    int t, k;
    cin >> t;
    for(int i = 1; i <= t; i++) {
        cin >> in >> k;
        int ans = 0;
        bool flag = true;
        
        for(int j = 0; j < in.size()-k+1; j++) {
            if(in[j] == '-') {
                for(int temp = j; temp < j+k; temp++) {
                    re(temp);
                }
                ans++;
            }
        }
        
        for(int j = 0; j < in.size(); j++) {
            if(in[j] == '-')
                flag = false;
        }
        if(flag)
            cout << "Case #" << i << ": " << ans << endl;
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
    
    return 0;
}