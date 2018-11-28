#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    long cases;
    ifstream in("oversizedpancake.in");
    ofstream out("oversizedpancake.out");
    in >> cases;
    for(long q=1; q<=cases; q++){
        string s;
        in >> s;
        long n = s.length();
        long ar[n];
        for(long i = 0; i<n; i++){
            ar[i] = 0;
        }
        long tot = 0;
        long k;
        in >> k;
        long ans = 0;
        bool ok = true;
        for(long i = 0;; i++){
            if(i-k>=0){
                tot-=ar[i-k];
            }
            if(i+k-1==n){
                for(long j = i; j<n; j++){
                    if(j>i && j-k>=0){
                        tot-=ar[j-k];
                    }
                    ok &= (s[j]=='+')==(tot%2==0);
                }
                break;
            }
            if((tot%2==0)!=(s[i]=='+')){
                tot++;
                ans++;
                ar[i]++;
            }
        }
        if(ok){
            out << "Case #" << q << ": " << ans << endl;
        }
        else{
            out << "Case #" << q << ": " << "IMPOSSIBLE" << endl;
        }
        
    }
    
    
    return 0;
}