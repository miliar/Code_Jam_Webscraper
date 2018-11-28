//
// Created by huklee on 08/04/2017.
//
// google code jam 2017 QT B
//  : array solution O(logN)

#include <map>
#include <queue>
#include <string>
#include <bitset>
#include <fstream>
#include <iostream>
using namespace std;

int digit_count(long long int N){
    int max_digit = 0;
    while (N){
        N/= 10;
        max_digit++;
    }
    return max_digit;
}

long long int solve(long long int N){
    // 01. int -> vector<int>
    vector<int> arr;
    int max_digit = digit_count(N);
    for (int i=0; i < max_digit; i++){
        arr.push_back(N%10);
        N /= 10;
    }

    // 02. find the largest tidy number
    int prev = arr[arr.size() - 1];
    for (int i=arr.size() - 2; i >= 0; i--){
        if (arr[i + 1] > arr[i]){
            int digit = i + 1;
            arr[digit]--;
            for (int j=0; j <= i; j++)
                arr[j] = 9;

            while (digit < arr.size() - 1 && arr[digit] < arr[digit + 1]){
                arr[digit + 1]--;
                arr[digit] = 9;
                digit++;
            }
            break;
        }
        prev = arr[i];
    }

    // 03. vector<int> -> int
    long long int result = 0, digit = 1;
    for (int i=0; i < arr.size(); i++){
        result += arr[i]*digit;
        digit *= 10;
    }
    return result;
}

int main() {
    long long int T, N;
    cin >> T;
    for (int tc=1; tc <= T; tc++){
        cin >> N;
        cout << "Case #" << tc << ": ";
        cout << solve(N) << endl;
    }
}
