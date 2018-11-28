#include <iostream>

using namespace std;

long lastNumber(long n){
    long last = n;
    long divisor = 10;
    while(true){       
    long mod1 = n%divisor;
    long aux2 = n/10;
    if(aux2 == 0) break;
    long mod2 = aux2%divisor;
    if(mod1 < mod2){
        last--;n = last; continue;
    }
    n = aux2;
 }
 return last;
}

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        long n;
        cin >> n;
        if(n/10 == 0){ cout << "Case #" << (i+1) << ": " << n << endl; continue;}
        long out = lastNumber(n);
        cout << "Case #" << i+1 << ": " << out << endl;
    }
    return 0;
}