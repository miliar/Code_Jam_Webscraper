#include<iostream>

using namespace std;

bool isTidy(int  n){
    int last = 11;
    while( n > 0){
        int current = n%10;
        if (current > last)
            return false;
        n /=10;
        last = current;
    }
    return true;
}

int getLastTidy(int n){
    int last = 0;
    while( n > 0){
        if ( isTidy(n))
            return n;
        n--;
    }
}

int main(){
    int t;
    cin >> t;
    int i = 1;
    while(i <= t){
        int n;
        cin >> n;
        cout << "Case #" << i++ << ": " << getLastTidy(n) << endl;
    }
    return 0;
}