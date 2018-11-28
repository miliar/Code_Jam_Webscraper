#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void fix(string& in, int j) {
    if(in[j] == '1') {
        in.pop_back();
        for(int i = 0; i < in.length(); i++)
            in[i] = '9';
    }
    else {
        in[j]--;
        if(j > 0 && in[j-1] > in[j]) {
            in[j] = '9';
            fix(in,j-1);
        }
    }
}


int main() {
    int n;
    cin >> n;
    vector<string> result;
    for(int i = 1; i <= n; i++) {
        string in;
        cin>>in;
        for(int j = 0; j < in.length() - 1; j++) {
            if(in[j] > in[j+1]) {
                for(int k = j+1; k < in.length(); k++)
                    in[k] = '9';
                fix(in, j);
                break;
            }
        }
        cout<<"Case #"<<i<<": "<<in<<endl;
    }
    return 0;
}
