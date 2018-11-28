#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int res=0,flag=0;

void flip(string &s, int i, int k){
    for(int j=0;j<k;j++,i++){
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
    }
    res++;
}

void check(string &s, int k, int len){
    flag=1;
    for(int i=0;i<len;i++){
        if(s[i]=='-'){
            flag=0;
            if(k<=len-i){
                flip(s,i,k);
            }
            else{
                res=-1;
                break;
            }
        }
        else
            flag=1;
    }
}

int main() {
    fstream infile, outfile;
    infile.open("infile.txt", ios::in);
    outfile.open("outfile.txt", ios::out);
    int t,i=0;
    infile>>t;
    while(i<t){
        res=0;
        i++;
        string s;
        int k;
        infile>>s>>k;
        int len=strlen(s.c_str());
        check(s,k,len);
        outfile<<"Case #"<<i<<": ";
        if(res==-1)
            outfile<<"IMPOSSIBLE\n";
        else
            outfile<<res<<"\n";
    }
    infile.close();
    outfile.close();
    return 0;
}