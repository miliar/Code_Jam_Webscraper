#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string a;
        cin>>a;

        for(int j=a.size()-1;j>0;--j){
            if(a[j-1]>a[j]){
                for(int k=a.size();k>=j;--k){
                    a[k]='9';
                }
                --a[j-1];
            }
        }

        if(a.front()=='0')a=a.substr(1);

        cout << "Case #" << i + 1 << ": "<<a<<'\n';
    }
    return 0;
}