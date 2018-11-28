#include <iostream>
#include <string>

using namespace std;

int getAnswer(string inputStr, int flipNum) {
    int targetArr[inputStr.length()];
    bool notFound = false;
    int pos = 0, cnt = 0;
    string blank = "-";
    for (int i = 0; i < inputStr.length(); i++) {
        if (inputStr.compare(i, 1, blank) == 0) {
            targetArr[i] = 0;
        } else {
            targetArr[i] = 1;
        }
    }
    while (true) {
        if (pos + flipNum > inputStr.length()) {
            break;
        }
        if (targetArr[pos] == 0) {
            for (int i = 0; i < flipNum; i++) {
                targetArr[pos+i] = (targetArr[pos+i]+1) % 2;
            }
            cnt++;
        }
        pos++;
    }
    for (int i = 0; i < inputStr.length(); i++) {
        if (targetArr[i] == 0) {
            notFound = true;
            break;
        }
    }
    if (notFound) {
        return -1;
    } else {
        return cnt;
    }
    /*for (int i = 0; i < inputStr.length(); i++) {
        cout << targetArr[i] << " ";
    }
    cout << endl;
    return 1;*/
}

int main(){
    string inputStr;
    int testCase, inputNum, result;
    cin >> testCase;
    for (int i = 0; i < testCase; i++) {
        cin >> inputStr >> inputNum;
        cout << "Case #" << i+1 << ": ";
        result = getAnswer(inputStr, inputNum);
        if (result == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << result << endl;
        }
    }
}