#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
bool chk(int k){
    int last = 10;
    while(k > 0 && k % 10 <= last){
        last = k % 10;
        k /= 10;
    }
    return k == 0;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    int n;
    for(int f = 1; f <= T; f++){
        cin >> n;
        while(chk(n) == false) --n;
        cout << "Case #" << f << ": " << n << endl;
    }

    return 0;
}
