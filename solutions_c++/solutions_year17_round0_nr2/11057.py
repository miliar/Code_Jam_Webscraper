#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");
    int t, n, no = 1;
    fin>>t;
    while(t--){
        fin>>n;
        int temp_var = n;
        while(temp_var) {
            vector<int> ss, temp;
            n = temp_var;
            while (n) {
                ss.push_back(n % 10);
                n /= 10;
            }
            reverse(ss.begin(), ss.end());
            temp = ss;
            sort(ss.begin(), ss.end());
            if (ss == temp) {
                fout << "Case #" << no << ": " << temp_var << "\n";
                no++;
                break;
            }
            temp_var--;
        }
    }
    return 0;
}
