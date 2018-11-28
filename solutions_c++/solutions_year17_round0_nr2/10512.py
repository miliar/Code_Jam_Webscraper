#include <iostream>

using namespace std;

int main(){
string s;
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    cin>>s;
    int lim = s.length();
    for(int j=0;j<lim-1;j++){
        if(s[j]>s[j+1]){
            s[j]--;
            for(int k=j+1;k<lim;k++)
                s[k]='9';
            lim=j+1;
        j=-1;
        }

    }
    if(s[0]=='0'){
        for(int i=0;i<s.length();i++)
            s[i]=s[i+1];
    int sz = s.length()-1;
    s.resize(sz);}
    cout<<"Case #"<<i<<": "<<s<<endl;
}
return 0;
}
