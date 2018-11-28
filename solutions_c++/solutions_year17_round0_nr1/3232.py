#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <algorithm>
#include <vector>


using namespace std;

int T;
string str;
int K;

inline bool done(string s) {
    return find(s.begin(), s.end(), '-') == s.end();
}

bool isImpossible() {
    int a = str.size() - K;
    int b = K;
    
    int s1 = 0;
    int s2 = 0;
    for(int i = a; i < b; i++) {
        if(str[i] == '+') s1++;
        if(str[i] == '-') s2++;
    }
    
    return (s1 != 0) && (s2 != 0);
}

string flip(string s, int p) {
    for(int i = 0; i < K; i++) {
        s[p+i] = (s[p+i] == '+' ? '-' : '+');
    }
    
    return s;
}

int main() {
    ifstream in("inA.txt");
    ofstream out("outA.txt");
    
    in >> T;
    
    for(int t = 1; t <= T; t++) {
        in >> str >> K;
        
        queue<string> q;
        q.push(str);
        bool flag = true;
        int x = -1;
        vector<string> v;
        v.push_back(str);
        
        out << "Case #" << t << ": ";
        
        if(isImpossible()) {
            out << "IMPOSSIBLE" << endl;
            continue;
        }
        
        while(!q.empty() && flag) {
            x++;
            cout << x << endl;
            int L = q.size();
            for(int l = 0; l < L; l++) {
                string s = q.front();
                q.pop();
                
                if(done(s)) {
                    flag = false;
                    break;
                }
                
                for(int p = 0; p <= s.size() - K; p++) {
                    string x = flip(s, p);
                    if(find(v.begin(), v.end(), x) == v.end()) {
                        q.push(x);
                        v.push_back(x);
                    }
                }
            }
        }
        
        if(flag)
            out << "IMPOSSIBLE" << endl;
        else
            out << x << endl;
    }
    
    return 0;
}
