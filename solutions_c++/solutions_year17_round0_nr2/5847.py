#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("test.in");
ofstream fout("rst.out");

vector<int> sovle(string _num) {
    int n = _num.size();
    vector<int> num(n);
    for(int i = 0; i < n; i++)
        num[i] = _num[i] - '0';
    
    int i = 0;
    for(; i < n - 1; i++) {
        if(num[i] > num[i+1]) break;
    }
    if(i != n-1) {
        int j = i;
        num[i++]--;
        for(; j >= 1; j--) {
            if(num[j] < num[j-1]) {
                num[j] = 9;
                num[j-1]--;
            }
        }
        int carry = 10;
        for(; i < n; i++) {
            num[i] += carry;
            carry = 0;
            if(num[i] > 9) {
                num[i] = 9;
                carry = 10;
            }
        }
    }
    i = 0;
    while(i < n) {
        if(num[i] != 0) break;
        i++;
    }
    vector<int> rst(num.begin() + i, num.end());
    return rst;
}

int main() {
    int n;
    fin >> n;
    for(int i = 1; i <= n; i++) {
        string _num;
        fin >> _num;
        vector<int> num = sovle(_num);
        fout << "Case #" << i <<": ";
        for(int n : num)
            fout << n;
        fout << endl;
    }
    

    return 0;
}
