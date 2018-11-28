#include<iostream>

using namespace std;

int currNumTidy = 0;
int tidy[1111];

bool isTidy(int num) {
    if (num < 10) return true;
    int prevDig = 10;
    while (num != 0) {
        if (num % 10 > prevDig) return false;
        else prevDig = num % 10;
        num -= num % 10;
        num /= 10;
    }
    return true;
}

void calcTidy() {
    for (int i = 1; i <= 1111; i++) {
        if (isTidy(i)) {
            tidy[currNumTidy] = i;
            currNumTidy += 1;
        }
    }   
}

int calcPrevTidy(int num) {
    for (int i = 0; i < currNumTidy; i++) {
        if (tidy[i] > num) return tidy[i - 1];
    }
}

int main() {
    calcTidy();
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        int num;
        cin >> num;
        if (num < 10) cout << num << endl;
        else cout << calcPrevTidy(num) << endl;        
    }   
}
