#include <iostream>
#include <fstream>
#include <ostream>

using namespace std;


bool isOk(string s){
    for(auto c:s){
        if(c=='-') return false;
    }
    return true;
}



string numberOfFlip(string& s, int k){
    int counter=0;
    for(int i=0;i<=s.size()-k;i++){
        if(s[i]=='-'){
            for(int j=i;j<i+k;j++){
                if(s[j]=='-') s[j]='+';
                else if(s[j]=='+') s[j]='-';
            }
            counter++;
        }
    }
    if(isOk(s)) return to_string(counter);
    return "IMPOSSIBLE";
}


#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

int main(){
    ifstream f("small.txt");
    ofstream myfile("output.txt");
    int N;
    f>>N;
    rep2(nn,1,N+1) {
        string str;
        int k;
        f>>str>>k;
        string res=numberOfFlip(str, k);
        myfile << "Case #"<<nn<<": "<<res<<endl;
    }
    myfile.close();
    return 0;
}




