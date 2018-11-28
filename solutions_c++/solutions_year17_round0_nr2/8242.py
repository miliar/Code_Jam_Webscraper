#include<bits/stdc++.h>
using namespace std;

bool isTidy(string num){
    int numsize = num.length();
    for(int i=1; i<numsize; i++){
        if(num[i] < num[i-1]) return false;
    }
    return true;
}

int main() {

    ifstream cin("B-small-attempt0.in");
    ofstream cout("B-output.txt");
    long long int T,N;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N;
        for(long long int i=N; i>=0; i--){
            stringstream ss;
            ss << i;
            string str = ss.str();
            if(isTidy(str)){
                cout << "Case #" << t << ": " << i<< endl;
                break;
            }
        }
    }
}
