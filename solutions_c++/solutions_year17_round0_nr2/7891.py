#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;

ll stringToLl(string s){
    stringstream ss(s);
    ll N;
    ss >> N;
    return N;
}

string llToString(ll N){
    stringstream ss2;
    ss2 << N;
    return ss2.str();
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string s;
        cin >> s;
        int i;
        while(true) {
            for(i=0;i<s.size()-1;i++){
                if(s[i] > s[i+1]){
                    break;
                }
            }

            for(int j=i+1;j<s.size();j++){
                s[j] = '9';
            }

            if(i != s.size()-1){
                ll N = stringToLl(s);
                N -= (ll)pow(10, s.size() - 1 - i);
                s = llToString(N);
            } else {
                break;
            }
        } 

        cout << "Case #" << t << ": " << stringToLl(s) << endl;
    }
}
