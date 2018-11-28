#include <iostream>
#include <string>
#include <vector>

using namespace std;

void doTest(int tc){
    string pattern; cin>>pattern;
    int k; cin>>k;

    int turns=0;
    for(int i=0;i<=pattern.length()-k;++i){
        // cout<<"I: "<<i<<endl;
        if(pattern[i]=='-'){
            turns++;
            for(int j=0;j<k;++j){
                pattern[i+j]=(pattern[i+j]=='+')?'-':'+';
            }
            // cout<<pattern<<endl;
        }
    }
    cout<<"Case #"<<tc<<": ";
    for(int i=0;i<pattern.length();++i){
        if(pattern[i]!='+'){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
    }
    cout<<turns<<endl;
}

int main(){
    int n; cin>>n;
    for(int i=1;i<=n;++i){
        doTest(i);
    }
}