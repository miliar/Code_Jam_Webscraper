#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("test.in");
ofstream fout("rst.out");

char flip(char c) {
    if(c == '+') return '-';
    else return '+';
}

int solve(string coins, int n, int rst) {
    if(coins.size() < n) return -1;
    if(coins.size() == n) {
        for(char c : coins)
            if(c != '-') return -1;
        return rst + 1;
    }
    for(int i = 0; i < n; i++) {
        coins[i] = flip(coins[i]);
        coins[coins.size() - 1 - i] = flip(coins[coins.size() - 1 - i]);
    }
    int i = 0, j = coins.size() - 1;
    while(i < coins.size() && coins[i] == '+') i++;
    while(j >= i && coins[j] == '+') j--;
    if(i == coins.size()) return rst + 2;
    else return solve(coins.substr(i, j - i + 1), n, rst + 2);
}

int main() {
    int n;
    fin >> n;
    for(int ii = 1; ii <= n; ii++) {
        string coins;
        int n;
        fin >> coins >> n;
        int rst = 0;
        int i = 0, j = coins.size() - 1;
        while(i < coins.size() && coins[i] == '+') i++;
        while(j >= i && coins[j] == '+') j--;
        if(i == coins.size()) rst = 0;
        else rst = solve(coins.substr(i, j - i + 1), n, 0);
        fout << "Case #" << ii <<": ";
        if(rst == -1) fout << "IMPOSSIBLE";
        else fout << rst;
        fout << endl;
    }
    

    return 0;
}
