#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream infile("B-large.in");
    ofstream outfile("B-large.out");

    int T;
    infile>>T;

    for(int t=1;t<=T;++t){
        string s;
        infile>>s;

        int start = 0;
        bool flag = true;

        for(int i=1;i<s.size();++i){
            if(s[i]>s[i-1]) start = i;
            if(s[i]<s[i-1]){
                flag = false;
                break;
            }
        }

        if(!flag){
            s[start] = (char)(s[start] - 1);
            for(++start;start<s.size();++start) s[start] = '9';
        }


        for(int i=0;i<s.size();++i){
            if(s[i]!='0'){
                s = s.substr(i);
                break;
            }
        }
        outfile<<"Case #"<<t<<": "<<s<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}