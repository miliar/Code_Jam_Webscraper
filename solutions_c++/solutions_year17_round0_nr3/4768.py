#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

long long calculate(long long n, long long k) {
    
    multiset<long long, greater<long long>> mySet;
    if (n < 1) {
        return 0;
    }
    
    mySet.insert(n);
    multiset<long long, greater<long long>>::iterator it;
    while (--k) {
        it = mySet.begin();
        long long temp = *it;
        if (temp == 1) {
            return 0;
        }
        if (temp % 2 == 1) {
            mySet.insert(temp / 2);
            mySet.insert(temp / 2);
        } else {
            mySet.insert(temp / 2 - 1);
            mySet.insert(temp / 2);
        }
        mySet.erase(it);
    }
    
    return *(mySet.begin());
}

int main(int argc, const char * argv[]) {
    ifstream ifile;
    ifile.open("/Users/Zhen/Desktop/FB/FB/03_input.txt");
    int t;
    ifile >> t;

    ofstream ofile;
    ofile.open("/Users/Zhen/Desktop/FB/FB/03_output.txt");

    for (int i = 0; i < t; i++) {
        int N, K;
        ifile >> N >> K;


        long long result = calculate(N, K);
        if (result == 0) {
            ofile << "Case #" << (i + 1) << ": "<< 0 << "\t" << 0 << endl;
        } else if (result % 2) {
            ofile << "Case #" << (i + 1) << ": "<< result / 2 << "\t" << result / 2 << endl;
        } else {
            ofile << "Case #" << (i + 1) << ": "<< result / 2 << "\t" << result / 2 - 1 << endl;
        }
        
        
    }
    
    ifile.close();
    ofile.close();

    return 0;
}
