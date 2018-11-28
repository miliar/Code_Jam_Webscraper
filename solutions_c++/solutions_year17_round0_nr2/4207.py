#include <iostream>
#include<sstream>
using namespace std;

int main(){
    int t;
    cin>>t;
    int n;
    n=t;
    string s;

    while (t--){
    cin>>s;
            int l=s.length();

        for (int i=l-2; i>=0; i--){
        if (s[i]-'0'>s[i+1]-'0'){
            for (int j=i+1; j<l; j++){
                s[j]='9';
            }
            s[i]=--s[i];
        }
    }
    cout<<"Case #"<<n-t<<": ";
    for (int c=0; c<l; c++){
        if(s[c]!='0'){cout<<s[c];}
    }
        
        
    cout<<endl;
    }
}
