#include <iostream>
#include <fstream>
#include <ostream>

using namespace std;

string LastTidyNumber(string s){
    for(int i=0;i<s.size()-1;i++){
        if(s[i]-'0'>s[i+1]-'0'){
            for(int j=i+1;j<s.size();j++){
                s[j]='9';
            }
            s[i]-=1;
            if(i>0 && s[i]<s[i-1]){
                int j=i;
                while(j>0 && s[j]<s[j-1]){
                    s[j]='9';
                    s[j-1]-=1;
                    j--;
                }
            }
            break;
        }
    }
    string res= s[0]=='0'?s.substr(1):s;
    return res;
}


#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

int main(){
    ifstream f("small.txt");
    ofstream myfile("output.txt");
    int N;
    f>>N;
    rep2(nn,1,N+1) {
        string str;
        string k;
        f>>k;
        string res=LastTidyNumber(k);
        myfile << "Case #"<<nn<<": "<<res<<endl;
    }
    myfile.close();
    return 0;
}




