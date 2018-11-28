#include <iostream>
using namespace std;

string find(string s) {
    int len = s.size();
    if(len <= 1) return s;
    string res = "";
    int i = 0;
    for (i=0;i<len-1;i++) {
        if(s[i] > s[i+1]) {
            res += s[i] - 1;
            int pointer = i - 1;
            while(pointer >= 0) {
                if(res[pointer] > res[pointer+1]) {
                    res[pointer] = res[pointer] - 1;
                    res[pointer+1] = '9';
                    pointer--;
                }
                else{
                    break;
                }
            }
            for(int j=i+1;j<len;j++)
                res+='9';
            break;
        }
        else {
            res+=s[i];
        }
    }
    if(i == len-1) {
        if(s[i] >= s[i - 1])
            res += s[i];
    }

    int nz = 0;
    while(res[nz] == '0') nz++;
    return res.substr(nz, len - nz);
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        string s;
        cin>>s;
        cout<<"Case #"<<i<<": "<<find(s)<<endl;
    }

    return 0;
}
