#include<iostream>
#include<fstream>
#include<string>

using namespace std;

void flip(string& s, int start, int end) {
    for(int i=start;i<end;++i) {
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}

int pancake(string& s, int k) {
    int res=0;
    
    for(int i=0;i<s.length();++i) {
        if(s[i]=='-' && i+k<=s.length()) {
            flip(s,i,i+k);
            res++;
        }
    }
    if(s==string (s.length(),'+')) return res;
    else return -1;
}

int main() {
    ifstream infile;
    ofstream outfile;
    infile.open("Al.txt");
    outfile.open("out.txt");
    if(infile.is_open()) {
        int T; //# of cases
        string s;
        int k,n; //k is length of flipper, n is # of flips needed
        infile>>T;
        for(int i=0;i<T;++i) {
            infile>>s>>k;
            n=pancake(s,k);
            
            if(n!=-1) outfile<<"Case #"<<i+1<<": "<<n<<endl;
            else outfile<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }

    }
    infile.close();
    outfile.close();
    return 0;
}
