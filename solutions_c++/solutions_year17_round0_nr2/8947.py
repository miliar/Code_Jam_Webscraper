#include<vector>
#include<algorithm>
#include<iostream>
#include<string>
#include<cstdlib>

using namespace std;

bool isTidy(string x) {
    char y = x[x.length()-1];
    int i = 2;
    while(1) {
        if(y >= x[x.length()-i]) {
            y = x[x.length()-i];
        }
        else 
            return false;
    }
    return true;
}

int main() {
    int tc;
    cin>>tc;
    for(int z=1;z<=tc;z++) {
        string N;
        cin >> N;
        string x = N;
        for(int i=x.length()-1; i > 0; i--) {
            char *a  = new char;
            *a = x[i];
            char *b  = new char;
            *b = x[i-1];
            if(atoi(a) < atoi(b)) {
                for(int j = i; j < x.length(); j++) {
                    x[j] = '9';
                }
                //if(x[i-1] == '0') {
                //    x[i-1] = '9';
                //} else {
                x[i-1]--;
                //}
            }
        }
        if(x[0] == '0')
            x.erase(x.begin());
        cout<<"Case #"<<z<<": "<<x<<endl;
    }
    return 0;
}
