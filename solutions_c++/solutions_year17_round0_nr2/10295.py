#include <iostream>

using namespace std;

bool check_tidy(int number) {
    int aux = number;
    int num = 0;
    int num2 = 0;
    //cout << number/10 << endl;
    if (number / 10 <= 0)
        return true;
    num = aux % 10;
    aux /= 10;
    while (aux > 0) {
        num2 = aux % 10;

        if (num < num2)
            return false;

        num = num2;
        aux /= 10;
    }
    return true;
}


int main() {
    int T, N;
    int tidy = 0;

    cin >> T;

    for(int i = 0; i < T; i++) {
        cin >> N;
        tidy = N;
        while(!check_tidy(tidy)) {
            tidy -= 1;
        }
        cout << "Case #" << i+1 << ": " << tidy << endl;
    }

    return 0;
}