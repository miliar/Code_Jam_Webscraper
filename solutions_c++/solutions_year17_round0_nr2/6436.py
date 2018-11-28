#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {
    int t, i, j, l, k;
    string a;
    ifstream ifile("/home/harish/algos/input.txt");
    ofstream ofile("/home/harish/algos/output.txt");
    string line;

    getline(ifile, line);
    t = stoi(line);
    for(int k=1;k<=t;k++) {
        getline(ifile, a);
        l = a.length();
        for(i=l-1;i>=1;i--) {
            if(a[i] < a[i-1]) {
                a[i-1] = a[i-1]-1;
                for(j=i;j<l;j++)
                    a[j] = '9';
            }
        }
        if(a[0] == '0')
            a = a.substr(1, l-1);
        ofile << "Case #" << k << ": " << a << endl;
    }
    ifile.close();
    ofile.close();
    return 0;
}