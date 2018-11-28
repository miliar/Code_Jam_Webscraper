#include <iostream>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll; 
ofstream fout("QB.out");
ifstream fin("QBlarge.in"); 

ll power(int i){
    ll num = 1; 
    while (i > 0){
        num *= 10; 
        i--; 
    }
    return num; 
}

ll tidy(ll a) {
    for (int i = 0; power(i) < a; i++){
        ll bp = power(i+1); 
        ll sp = power(i); 
        ll p1 = a/bp; 
        p1 %= 10; 
        ll p2 = a/sp; 
        p2 %= 10; 
        if (p1 > p2){
            a /= bp; 
            a *= bp; 
            ll num = a-1; 
            return tidy(num);             
        }
    }
    return a; 
}

int main() {
    ll N,T; 
    fin >> T; 
    for (int i = 1; i<= T; i++){
        fin >> N; 
        fout << "Case #" << i << ": " << tidy(N) << endl; 
    }
}
