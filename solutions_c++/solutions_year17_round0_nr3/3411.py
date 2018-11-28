#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstring>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t,n,k;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        vector<int> s;
        s.push_back(n);
        for(int j = 1; j < k; ++j){
            int cur = s.front();
            pop_heap(s.begin(), s.end());
            s.pop_back();
            if(cur%2){
                s.push_back(cur/2);
                push_heap(s.begin(),s.end());
                s.push_back(cur/2);
                push_heap(s.begin(),s.end());
            }else{
                s.push_back(cur/2);
                push_heap(s.begin(),s.end());
                s.push_back(cur/2-1);
                push_heap(s.begin(),s.end());
            }
        }
        
        int cur = s.front();
        int mind = 0, maxd = 0;
        if(cur%2){
            maxd = cur/2;
            mind = cur/2;
        }else{
            maxd = cur/2;
            mind = cur/2-1;
        }
        cout<<maxd<<" "<<mind<<endl;
        
    }
    return 0;
}