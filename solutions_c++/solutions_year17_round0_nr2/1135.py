#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Expects 0 <= i < d.size()
bool borrow(vector<int> & d, int i) {
    //Got enough
    if(d[i] > 0) {
        d[i]--;
        return true;
    }
    //Can't borrow from next
    //This should not happen
    //The most significant digit should not be zero
    if(i == 0) return false;

    if(borrow(d, i - 1)){
        //Borrowed a 10, then -1
        d[i] = 9;
        return true;
    }
    return false;
}

int main() {
    int T;
    vector<int> d;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> ws;
        string temp;
        cin >> temp;
        d.clear();
        for(char &c : temp) {
            d.push_back(c - '0');
        }
        //for(int &i : digits) cerr << i << endl;
        bool success = true;
        for(int i = d.size() - 1; i >= 0; i--) {
            if(i == 0) break;
            //In order
            if(d[i-1] <= d[i]) continue;

            //Borrow one from the next digit
            borrow(d, i-1);
            //Now this and all the lower significant digits are 9
            for(int j = i; j < d.size(); j++) {
                d[j] = 9;
            }
        }

        cout << "Case #" << (t+1) << ": ";
        for(int &digit : d) {
            if(digit != 0)
                cout << digit;
        }
        cout << endl;
    }
}
