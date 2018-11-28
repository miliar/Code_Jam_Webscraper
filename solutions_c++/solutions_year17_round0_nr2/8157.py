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
        string ss;
        cin >> ss;
        if (ss.size() > 1) {
            int ind = 0, f=0;
            for (int j=1; j<ss.size(); j++) {
                if ((int)ss[j] < (int)ss[j-1]) {f=1; break;}
                if ((int)ss[j] > (int)ss[j-1]) ind = j;
            }
            if (f) {
                ss[ind] = ss[ind] - 1;
                for (int j=ind+1; j<ss.size(); j++){  
                    ss[j] = 57;
                }
                int k=0;
                for (; k<ss.size(); k++){
                    if (ss[k]!='0') break;
                }
                ss = ss.substr(k);
            }
        }
        cout << "Case #" << i+1 << ": "<< ss <<"\n";
    }
	return 0;
}
