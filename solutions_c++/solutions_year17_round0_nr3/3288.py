#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int T;
long long N, K;

int main() {
    ifstream in("inClarge.txt");
    ofstream out("outClarge.txt");
    
    in >> T;
    
    for(int t = 1; t <= T; t++) {
        in >> N >> K;
        
        long long x = 0, y = 0;
        map<long long, long long> m;
        vector<long> v;
        
        m[N] = 1;
        v.push_back(N);
        
        while(K > 0) {
            long long s = v.back();
            long long p = m[s];
            
            long long s1, s2;
            if(s % 2 == 0) {
                s1 = s/2 - 1;
                s2 = s/2;
            } else {
                s1 = s/2;
                s2 = s/2;
            }
            
            m[s] = 0;
            v.pop_back();
            
            if(m.find(s1) == m.end()) {
                m[s1] = 0;
                v.push_back(s1);
            }
            
            if(m.find(s2) == m.end()) {
                m[s2] = 0;
                v.push_back(s2);
            }
            
            m[s1] += p;
            m[s2] += p;
            
            x = s2;
            y = s1;
            
            sort(v.begin(), v.end());
            K -= p;
        }
        
        out << "Case #" << t << ": " << x << " " << y << endl;
    }
    
    return 0;
}
