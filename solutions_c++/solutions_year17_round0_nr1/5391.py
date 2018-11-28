#include <iostream>
#include <string>
#include <list>
#include <map>
using namespace std;

int is_happy(string s) {
    for(int i =0;i<s.size();i++) {
        if(s[i]!='+')
            return i;
    }
    return -1;
}

string flip(string s, int i, int k) {
    //cout << "\tFLIP: S:" << s << " i:" << i << " k:" << k;
    for(int x=0;x<k;x++)
        s[i+x] = '-' + '+' - s[i+x];
    //cerr << " RES:" << s << endl;
    return s;
}

long solve(string s, int k) {  
    int l = s.size();
    
    map<string, bool> m;
    int cnt = 0;
    
    int ix = is_happy(s);
    while(ix >= 0) {
        if(m.find(s) != m.end()) {
            //found! 
            return -1;
        }

        m[s] = true;

        if(ix > l-k) {
            return -1;
        }

        s = flip(s, ix, k);
        ix = is_happy(s);
        cnt++;
    } 

    return cnt;
}



int main() {
    int T;
    cin >> T;
    for(int i=0;i<T;i++) {
        string S;
        int K;

        cin >> S >> K;
        
        long ans = solve(S, K);
        if(ans >=0) {
            cout << "Case #" << i+1 << ": " << ans << endl;
        } else {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
}
