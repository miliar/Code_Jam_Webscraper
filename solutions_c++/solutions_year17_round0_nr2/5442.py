#include <iostream>
#include <cstdio>

using namespace std;

bool isTidy(long long n){
    int last = n%10;
    n/=10;
    while (last >= n%10 && n > 0){
        last = n%10;
        n/=10;
    }

    if (n==0)
        return true;

    return false;
}

long long tidyNumber(long long n){
    long long pow = 10;

    while (!isTidy(n)){
        n = n/pow*pow - 1;
        pow*=10;
    }

    return n;
}

int main(){
    long long n;
    int cases;

    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> cases;

    for (int i = 0; i < cases; i++){
        cin >> n;
        cout << "Case #" << i+1 << ": " << tidyNumber(n) << endl;
    }

    return 0;
}
