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

int div_up(int n, int d) {
    return n/d + (n%d>0 ? 1 : 0);
}

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int n, c, m;  // seats, customers, tickets
    std::cin >> n >> c >> m;

    vector<std::map<int, int>> customers(c);
    vector<int> c_tickets(c, 0);
    vector<int> sum_p(n);
    for (int i = 0; i < m; ++i) {
        int p, b; // position, buyer
        std::cin >> p >> b;
        b--, p--; // rebase to zero
        
        customers[b][p]++;
        c_tickets[b]++;
        sum_p[p]++;
    }
    
    int rides = *max_element(c_tickets.begin(), c_tickets.end());

    int sump_tillp = 0;
    for (int i = 0; i < n; ++i) {
        sump_tillp += sum_p[i];
        int needed = div_up(sump_tillp, i+1);
        rides = max(rides, needed);
    }
    
    int promotions = 0;
    for (int i = 0; i < n; ++i) {
        promotions += max(0, sum_p[i] - rides);
    }
    
    cout << rides << " " << promotions << "\n";
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