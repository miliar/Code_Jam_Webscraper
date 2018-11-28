#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>

using namespace std;

long long solveCase(long long n) {
    string n_str = to_string(n);
    int bad_index = -1;
    for(int i=0;i<n_str.length();i++) {
        if(i>0 && n_str[i] < n_str[i-1]) {
            bad_index = i;
            break;
        }
    }
    if(bad_index==-1)
        return n;

    int dec_index = -1;
    for(int i = bad_index - 1 ; i>=0 ; i--) {
        if(n_str[i]!='1' && (i==0 || n_str[i-1]< n_str[i])) {
            dec_index = i;
            break;
        }
    }

    if(dec_index!=-1) {
        n_str[dec_index]--;
        for(int j=dec_index+1;j < n_str.length();j++) {
            n_str[j]='9';
        }
        return stoll(n_str);
    } else {
        long long res = 1;
        for(int i=0;i<n_str.length()-1;i++)
            res = res * 10;
        return res - 1;
    }
}

int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        long long n;
        cin >> n;
        cout << "Case #" << (i+1) <<": " << solveCase(n) << endl;
    }

}