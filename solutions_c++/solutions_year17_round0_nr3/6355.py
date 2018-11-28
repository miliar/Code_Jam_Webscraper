#ifdef F
#include <fstream>
std::ifstream cin("input.txt");
std::ofstream cout("output.txt");
#else
#include <iostream>
using std::cin;
using std::cout;
#endif
#include <sstream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        long n, k;
        priority_queue<long> p;
        cin >> n >> k;
        p.push(n);
        //cout <<"\nn:"<<p.size();
        for (int j=0; j<k-1; j++) {
            long h = p.top();
            h--;
            p.push(h-h/2);
            p.push(h/2);
            p.pop();
           // cout << "\nj:" << j <<" h:"<<h;
        }
        long h = p.top();
        h--;
        //cout << "\nh: " << h;
        cout << "Case #" << i+1 << ": "<< (h-h/2) << " " << h/2 <<"\n";
    }
	return 0;
}
