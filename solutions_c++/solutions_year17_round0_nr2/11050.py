#include <iostream>
#include <vector>

using namespace std;

bool checkTidy (unsigned long long int N) {
    vector<unsigned long long int> reversedDigit;

    do {
        reversedDigit.push_back(N%10);
        N /= 10;
    } while(N);

    int lastOrder = 0;
    for(int i = reversedDigit.size()-1; i >= 0 ; i--) {
        if(reversedDigit[i] < lastOrder) return false;
        lastOrder = reversedDigit[i];
    }
    return true;
}

int main() {
    unsigned long long int n;
    cin >> n;
    unsigned long long int *arr = new unsigned long long int[n];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for(int i = 0; i < n; i++) {
        while(!checkTidy(arr[i])) arr[i]--;
        cout << "Case #" << (i+1) << ": " << arr[i] << "\n";
    }

    return 0;
}
