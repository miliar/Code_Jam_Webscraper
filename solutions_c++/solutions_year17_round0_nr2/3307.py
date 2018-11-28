#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstring>
#include <vector>
#include <unordered_map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #"<<i<<": ";
        string ret = "";
        int len = s.size();
        bool good = true;
        for(int j = len-1; j >0; --j){
            if(s[j]<s[j-1]){
                good = false;
                break;
            }
        }
        if(good){
            cout<<s<<endl;
            continue;
        }
        int j = len -1;
        int flag = 0;
        while(j>0){
            if(s[j]<s[j-1]){
                s[j-1]--;
                flag = j;
            }
            --j;
        }
        for(; flag<len; ++flag){
            s[flag] = '9';
        }
        s.erase(0, s.find_first_not_of('0'));
        cout<< s<<endl;
    }
    return 0;
}