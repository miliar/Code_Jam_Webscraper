// Compile with MinGW-64 (6.3.0) in MSYS2
// Compile switches: -std=c++11 -Wall -Wconversion -Werror

#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

const char kCakeEmpty = '?';

bool isRowOccupied(const string& s) {
    for (char c : s) {
        if (c != kCakeEmpty) return true;
    }
    return false;
}

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ":\n";

    int r, c;
    std::cin >> r >> c;
    string junk;
    std::getline(std::cin, junk);
    std::vector<string> cake;
    std::vector<bool> is_occupied;

    for (int i = 0; i < r; ++i) {
        string s;
        std::getline(std::cin, s);
        
        cake.push_back(s);
        is_occupied.push_back(isRowOccupied(s));
    }
    
    // if occupied, set ? in each row to initials
    for (int i = 0; i < r; ++i) {
        if (!is_occupied[i]) continue;

        char fill = kCakeEmpty;
        for (int x = 0; x < c; ++x) {
            if (cake[i][x] == kCakeEmpty) {
                cake[i][x] = fill; // okay even if fill is empty
            } else if (fill == kCakeEmpty) {
                fill = cake[i][x];
                for (int x1 = 0; x1 < x; ++x1)
                    cake[i][x1] = fill;
            } else {
                fill = cake[i][x];
            }
        }
        
        if (fill == kCakeEmpty) cerr << "Error #1"; // assert
    }
    
    // set unoccupied rows
    int last_occupied_row = -1;
    for (int i = 0; i < r; ++i) {
        if (!is_occupied[i]) {
            if (last_occupied_row != -1)
                cake[i] = cake[last_occupied_row];
        } else if (last_occupied_row == -1) {
            last_occupied_row = i;
            for (int i1 = 0; i1 < i; ++i1) {
                cake[i1] = cake[last_occupied_row];
            }
        } else {
            last_occupied_row = i;
        }
    }
    
    // output results
    for (string s : cake)
        cout << s << "\n";
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for (int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}