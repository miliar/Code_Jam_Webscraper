#include <bits/stdc++.h>
using namespace std;

string s;
int t;

int main(){
    ifstream cin ("tidy.in");
    ofstream cout ("tidy.out");
    cin>>t;
    for (int w=1; w<=t; w++){
        cin>>s;
        int i=1;
        while (i<s.length() && s[i]>=s[i-1]) i++;
        if (i>=s.length() || s.length()==1) cout<<"Case #"<<w<<": "<<s<<"\n";
        else{
            s[i-1]=char(int(s[i-1])-1);
            int q=i-1;
            while (q>0 && s[q]<s[q-1]){
                s[q]='9';
                s[q-1]=char(int(s[q-1])-1);
                q--;
            }
            for (i; i<s.length(); i++) s[i]='9';
            if (s[0]=='0') s.erase(0,1);
            cout<<"Case #"<<w<<": "<<s<<"\n";
        }
    }
    return 0;
}
