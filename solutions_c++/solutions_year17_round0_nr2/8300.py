#include<iostream>
#include<string>
using namespace std;

int main() {
    int t;
    string s;
    cin>>t;
    char num[20];
    for(int c=1; c<=t; c++) {
        cin>>s;
        for(int i=0; i<s.size(); i++)
            num[i] = s[i];
        num[s.size()] = '\0';
        for(int i=0; i<s.size()-1; i++) {
            if(num[i]>num[i+1]) {
                int j=i;
                while(j>0 && num[j]==num[j-1]) {
                    j--;
                }
                num[j] = (char)(num[j]-1);
                for(int k=j+1; k<s.size(); k++) num[k] = '9';
            }
        }
        if(num[0]=='0' && s.size()>1)
            cout<<"Case #"<<c<<": "<<string(num+1)<<endl;
        else
            cout<<"Case #"<<c<<": "<<string(num)<<endl;
    }
    return 0;
}