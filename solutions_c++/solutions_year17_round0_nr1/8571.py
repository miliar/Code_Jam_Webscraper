#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool istrue(string s){
    for(int p=0;p<s.length();p++){
        if(s[p]=='-'){
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
        string s;
        int k;
        cin>>s>>k;
        int number = 0;
        for(int p=0;p<=s.length()-k;p++){
            if(s[p]=='-'){
                number++;
                for(int l=p;l<p+k;l++){
                    if(s[l]=='-'){
                        s[l] = '+';
                    }
                    else{
                        s[l]='-';
                    }
                }
            }
        }

        string ans;
        if(istrue(s)){
            stringstream ss;
            ss<<number;
            ss>>ans;
        }
        else{
            ans = "IMPOSSIBLE";
        }

        string x3 = "Case #";

        stringstream ss2;
        ss2<<i;
        string y;
        ss2>>y;

        string x4 = ": ";

        string x;
        x = x3+y+x4+ans+"\n";
        file<<x;

    }
    return 0;
}
