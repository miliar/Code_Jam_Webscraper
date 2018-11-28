#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
    fstream infile, outfile;
    infile.open("infile.txt", ios::in);
    outfile.open("outfile.txt", ios::out);
    int t,i=0;
    infile>>t;
    while(i<t){
        int flag=0;
        string s;
        infile>>s;
        int len=strlen(s.c_str());
        int l=len;
        while(l--){
            if(flag==0){
                for(int i=1;i<len;i++){
                    if(s[i-1]>s[i]){
                        flag=0;
                        s[i-1]-=1;
                        for(int j=i;j<len;j++){
                            s[j]='9';
                        }
                        break;
                    }
                    else
                        flag=1;
                }
            }
            else
                break;
        }
        if(s[0]=='0' && len>0)
            s=s.substr(1);
        i++;
        outfile<<"Case #"<<i<<": "<<s<<"\n";
    }
    infile.close();
    outfile.close();
    return 0;
}