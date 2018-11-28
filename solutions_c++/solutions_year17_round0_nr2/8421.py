#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;


long long tidyNum(string& s) {
    
    //s is tidyNum
    if(s.length()==1) return stoll(s);
    int i=0;
    long long res=0;
    while(i+1<s.length() && s[i]<=s[i+1]) {
        res=res*10+(s[i]-'0');
        ++i;
    }
    if(i+1==s.length()) return res*10+(s[i]-'0');
    if(i>=1 && s[i]==s[i-1]) {
        int j=0;
        long long nres=(s[0]=='1') ? 0:s[0]-'1';
        while(j<s.length()-1) {
            nres=nres*10+9;
            ++j;
        }
        return nres;
    }
    res=res*10+(s[i]-'1');
    while(i+1<s.length()) {
        res=res*10+9;
        ++i;
    }
    return res;
}

int main() {
    
    ifstream infile;
    ofstream outfile;
    infile.open("Bs.txt");
    outfile.open("out.txt");
    if(infile.is_open()) {
        int T; //# of cases
        string s;
        long long n;
        infile>>T;
        for(int i=0;i<T;++i) {
            infile>>s;
            n=tidyNum(s);
            outfile<<"Case #"<<i+1<<": "<<n<<endl;
        }
    }
    infile.close();
    outfile.close();
    
    /*
    int T; //# of cases
    string s;
    long long n;
    cin>>T;
    for(int i=0;i<T;++i) {
        cin>>s;
        n=tidyNum(s);
        cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
    */
    return 0;
}
