#include<iostream>
#include<string>

using namespace std;

int main() {
    int cases;
    cin>>cases;
    for(int cas=1;cas<=cases;++cas) {
        cout << "Case #"<<cas<<": ";
        string s;
        cin>>s;
        for(int times = 0; times < 20; times ++){
            for(int i = 0; i< s.size();++i) {
                bool good = true;
                for(int j=0; j< i;++j) if(s[j]>s[i]) good = false;
                if(!good) {
                    for(int j = i;j<s.size();++j) s[j]='9';
                    bool continua = true;
                    for(int j = i-1;continua;--j){
                        s[j]--;
                        if(s[j]<'0') s[j]='9';
                        else continua = false;
                    }
                    break;
                }
            }
        }
        if(s[0]=='0') cout << s.substr(1,s.size()-1) << endl;
        else cout << s << endl;
    }
}
