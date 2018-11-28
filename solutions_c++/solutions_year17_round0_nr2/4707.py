#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int main( ){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        long int n,q;
        int b,m;
        b = 0;
        string s;
        cin >> n;
        s = to_string(n);
        for (int x = 0; x < s.size() - 1; x++){
            if (s[x] > s[x+1]){
                q = pow(10,(s.size()-b-1));
                n -= n%q + 1;
                break;
            }
            else if (s[x] < s[x+1]){
                b = x+1;
            }
        }
        cout << "Case #" << i+1 << ": " << n << endl;
    }
    return 0;
}
