#include <iostream>
#include <map>

using namespace std;

int main() {
    long long ins, cur, pep;

    cin >> ins;

    for (int i=0;i<ins;i++) {
        cin >> cur;
        cin >> pep;
        
        map<long long, long long> stalls;
        
        stalls[cur] = 1;
        
        for(map<long long, long long>::reverse_iterator iter = stalls.rbegin();iter != stalls.rend(); ++iter) {
            long long b = iter->first;
        
            if (stalls.find(b) != stalls.end()) {
                long long max, min;
                
                if (b%2 == 1) {
                    min = b/2;
                    max = b/2;
                } else {
                    min = (b/2)-1;
                    max = b/2;
                } 
                
                //cout << pep << " " << b << "\n";
                
                //cout << "stalls: " << max << " " << min << "\n"; 
            
                if (pep<=stalls[b]) {
                    cout << "Case #" << i+1 << ": " << max << " " << min << "\n"; 
                    
                    break;
                } else {
                    if (stalls.find(max) != stalls.end()) {
                        stalls[max]+=stalls[b];
                    } else {
                        stalls[max]=stalls[b];
                    }
                    
                    if (stalls.find(min) != stalls.end()) {
                        stalls[min]+=stalls[b];
                    } else {
                        stalls[min]=stalls[b];
                    }
                    
                    pep-=stalls[b];
                }
            }
        }
    }
}
