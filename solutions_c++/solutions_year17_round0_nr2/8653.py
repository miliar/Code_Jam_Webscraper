#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool istidy(int p){
    stringstream ss;
    string s;
    ss<<p;
    ss>>s;
    for(int j=0;j<s.length()-1;j++){
        if(s[j] > s[j+1]){
            return false;
        }
    }
    return true;
}

int main()
{
    ofstream file;
    file.open("output.txt");
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        int n;
        cin>>n;
        int ans;
        for(int p=n;p>=1;p--){
            if(istidy(p)){
                ans=p;
                break;
            }
        }
        string x3 = "Case #";

        stringstream ss2;
        ss2<<i;
        string y;
        ss2>>y;

        string x4 = ": ";

        stringstream ss3;
        ss3<<ans;
        string y2 ;
        ss3>>y2;

        string x;
        x = x3+y+x4+y2+"\n";
        file<<x;




    }

    return 0;
}
