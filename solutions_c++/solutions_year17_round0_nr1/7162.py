#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;

void flip(string &s, int i, int k){
    int j = i+k;
    while (i < j){
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
        i++;
    }
}

string ans(string s, int k){
    int len = s.length();
    int count = 0;
    for (int i = 0; i < len; i++){
        if (s[i] == '-'){
            count++;
            if (i+k > len) return "IMPOSSIBLE";

            flip(s, i, k);
        }
    }

    if (s[len-1] == '-') return "IMPOSSIBLE";

    return SSTR(count);
}

int main(){
    ifstream cin("A-large.in");
    ofstream cout("output-pancakes-large.txt");

    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << (i+1) << ": " << ans(s, k) << endl;
    }
    return 0;
}
