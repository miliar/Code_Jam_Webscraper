#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

void flipPancakes(string & s, int i, int k){
    for(int j=i; j < i+k; ++j){
        s[j] = s[j] == '+' ? '-' : '+';
    }
}

int checkPancakes(string &  s, int k){
    int flipCount = 0;
    for(int i=0; i < s.size(); ++i){
        if(s[i]=='-' && i +k <= s.size()){
            flipPancakes(s,i,k);
            //cout << s << endl;
            flipCount ++;
        }

        if(s[i]=='-'){
            return -1;
        }
    }

    return flipCount;
}

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    string s;
    int k;

    for(int i=1; i <=t; i++){

        cin >> s >> k;

        int results = checkPancakes(s,k);

        cout << "Case #"<< i << ": ";
        if(results < 0){
            cout << "IMPOSSIBLE\n";
        }else{
            cout << results << "\n";
        }

    }

    return 0;
}