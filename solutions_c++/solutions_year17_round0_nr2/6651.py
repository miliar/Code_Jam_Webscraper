#include <bits/stdc++.h>
using namespace std;

int main(){
    long long int n, m, sl, l, mul, add, t, i;

    cin >> t;

    for(i = 1; i <= t; i++){
        cin >> n;
        l = n % 10;
        m = l;
        n = n / 10;
        sl = n % 10;
        mul = 10;
        add = 9;

        while(n){
            n = n / 10;

            if(sl > l){
                sl--;
                m = sl * mul + add;
            }
            else
                m = sl * mul + m;

            l = sl;
            sl = n % 10;
            add = (add * 10) + 9;
            mul = mul * 10;
        }

        cout << "Case #" << i << ": " << m << endl;
    }
}
