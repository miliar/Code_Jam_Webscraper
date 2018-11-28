#include<iostream>
using namespace std;

bool check(int);

int main(){

    int a, n;
    cin >> a;
    for(int t = 1; t<=a; t++) {
        cin >> n;

        while(true){
            bool ans = check(n);
            if(n/10 <1){
                cout << "Case #" << t << ": " << n << endl;
                break;
            }

            if(ans){
                cout << "Case #" << t << ": " << n << endl;
                break;
            }
            n--;
        }
    }

    return 0;
}

bool check(int n){
    int r = n%10;
    while(n/10 > 0){
        n = n/10;
        if(n%10 > r)
            return false;
        r = n%10;

    }
    return true;
}