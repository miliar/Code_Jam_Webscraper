#include<bits/stdc++.h>
using namespace std;

int main(){

    ifstream myReadFile;
    myReadFile.open("input.in");
    ofstream myfile;
    myfile.open ("output.out");
    int t;
    myReadFile>>t;
    int c=1;
    while(t--){
        string s;
        int k;
        myReadFile>>s>>k;
        int ret=0;
        bool no=false;
        for(auto i=0;i<=s.size()-k;i++){
            if(s[i]=='-'){
                    ret++;
                for(auto j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }

        for(int i=0;i<k;i++){
            if(s[s.size()-i-1]=='-'){
                no=true;
                break;
            }
        }

        if(no)myfile<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
        else myfile<<"Case #"<<c<<": "<<ret<<endl;
        c++;
    }
    return 0;
}
