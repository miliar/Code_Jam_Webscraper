#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstring>
#include <vector>
#include <unordered_map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t, k;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;  // read n and then m.
        cout << "Case #"<<i<<": ";
        // bool save[10];
        int len = s.size(), ret = 0;
        /*char pos;
        if(k*2 > len+1){
            int j = len-k+1;
            pos = s[len-k];
            bool cont = false;
            while(j < k){
                if(s[j]!= pos){
                    cont = true;
                    break;
                }
                ++j;
            }
            if(cont){
                cout<< "IMPOSSIBLE"<<endl;
                continue;
            }
        }*/
        
        int ind = 0;
/*        if(s[len-1] == '-'){
            ret++;
            for(int j = len-k; j< len; ++j){
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }*/
        while(ind <= len-k){
            if(s[ind] == '-'){
                ret++;
                for(int j = ind; j< ind+k; ++j){
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
            ++ind;
        }
        
        bool suc = true;
        for(int j = 0; j < len; ++j){
            if(s[j]!= '+'){
                suc = false;
                break;
            }
        }
        if(!suc){
            cout<< "IMPOSSIBLE"<<endl;
        }else{
            cout <<ret<<endl;
        }
        
    }
    return 0;
}