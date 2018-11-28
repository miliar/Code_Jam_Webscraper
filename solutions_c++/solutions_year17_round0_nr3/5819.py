#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <queue>

using namespace std;
priority_queue<unsigned long> empty_chunks;

unsigned long EnterStall() {
    unsigned long val = empty_chunks.top();
    unsigned long n1 = val/2;
    unsigned long n2 = val/2;
    empty_chunks.pop();
    if (val % 2 == 0) { // Even sized chunk
        n1 = val/2 -1;
    }
    if (n1) {
        empty_chunks.push(n1);
    }
    if (n2) {
        empty_chunks.push(n2);
    }
    return val;
}

int main() {
    int iters;    ifstream fin;
    fin.open("input.txt");
    fin >> iters;
    ofstream fout;
    fout.open("output.txt");
    for (int i = 0; i < iters; ++i) {
        empty_chunks = priority_queue<unsigned long>();
        unsigned long n, k;
        fin >> n >> k;
        empty_chunks.push(n);
        unsigned long last_val;
        while (k > 0) {
            last_val = EnterStall();
            k--;
        }
        unsigned long n1 = last_val/2;
        unsigned long n2 = last_val/2;
        empty_chunks.pop();
        if (last_val % 2 == 0) { // Even sized chunk
            n1 = last_val/2 -1;
        }
        fout << "Case #" << i+1 << ": ";
        fout << n2 << " " << n1 << endl;
        cout << "Case #" << i+1 << ": ";
        cout << n2 << " " << n1 << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
