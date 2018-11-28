#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

void comp(int tc){
    string s;
    cin >> s;
    int n = (int)s.length();
    for(int i=0; i<n-1; ++i){
        if(s[i] > s[i+1]){
            --s[i];
            fill(s.begin()+i+1, s.end(), '9');
            while(i>0 && s[i-1] > s[i]){
                --s[i-1];
                s[i] = '9';
                --i;
            }
            break;
        }
    }
    
    auto pos = s.find_first_not_of('0');
    if(pos != string::npos){
        s.erase(s.begin(), s.begin()+pos);
    }
    
    cout << "Case #" << tc << ": " << s << endl;
}

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc<=T; ++tc){
        comp(tc);
    }
}
