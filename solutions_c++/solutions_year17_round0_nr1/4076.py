#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream infile("A-large.in");
    ofstream outfile("A-large.out");
    int T;
    infile>>T;
    for(int t=1;t<=T;++t){
        string s;
        infile>>s;
        int k;
        infile>>k;

        int start = 0;
        int counter = 0;
        bool flag = true;
        while(start<s.size() && flag){
            while(start<s.size() && s[start]=='+') ++start;
            if(start==s.size()) break;
            for(int i=0;i<k;++i){
                if(i+start>=s.size()){
                    flag = false;
                    outfile<<"Case #"<<t<<": IMPOSSIBLE"<<endl;;
                    break;
                }
                if(s[i+start]=='-') s[i+start] = '+';
                else s[i+start] = '-';
            }
            ++counter;
        }
        if(flag) outfile<<"Case #"<<t<<": "<<counter<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}