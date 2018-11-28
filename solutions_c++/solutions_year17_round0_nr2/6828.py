#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
    ifstream cin("in.in");
    ofstream cout("out.in");

    int T;
    cin>>T;
    for (int t = 1; t<=T; t++) {
        long long ans = 0, n;
        cin>>n;
        vector<int> d;
        while (n) {
            d.push_back(n % 10);
            n /= 10;
        }

        reverse(d.begin(), d.end());

        for (int i=1; i<d.size(); i++) {
            if (d[i] < d[i-1]) {
                int j = i - 1;
                for (; j>=0; j--) {
                    if (j == 0 || d[j] - 1 >= d[j-1]) {
                        d[j]--;
                        break;
                    }
                }
//                if (d[0] == 0) {
//                    d.pop_back();
//                    i = 0;
//                }
                for (j=j+1; j<d.size(); j++) {
                    d[j] = 9;
                }
                break;
            }
        }

        for (int i=0; i<d.size(); i++) {
            ans = 10 * ans + d[i];
        }

        cout<<"Case #"<<t<<": ";
        cout<<ans<<endl;

    }
}