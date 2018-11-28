#include<iostream>
#include<fstream>
using namespace std;

string decrease(int idx, string str){
    int len = str.length();
    if(idx==0 && str[idx]=='1'){
        string temp="";
        for(int i=0;i<len-1;i++) temp+="9";
        return temp;
    }

    if(str[idx]>'0'){
        str[idx] = str[idx]-1;

        if(idx&&str[idx]<str[idx-1]){
            return decrease(idx-1,str);
        }

        for(int i=idx+1;i<len;i++) str[i]='9';
        return str;
    } else {
        return decrease(idx-1,str);
    }
}
string fun(int idx, string str){
    if(idx == str.length()) return str;
    if(idx==0) return fun(idx+1,str);

    if(str[idx]<str[idx-1]) {
        return decrease(idx-1,str);
    }

    return fun(idx+1,str);
}

int main(){
    fstream fin("/Users/anupsing/Documents/CP/GCJ/QF/2/input.in");
    fstream fout("/Users/anupsing/Documents/CP/GCJ/QF/2/output.txt");

 int T;
    fin>>T;
    int cases=1;
    while(T--){
        string ans="";
        long long num;
        fin>>num;
        while(num){
            ans = (char)('0'+((int)num%10))+ans;
            num/=10;
        }
        ans = fun(0,ans);
        fout<<"Case #"<<cases<<": "<<ans<<endl;
        cases++;


    }
    return 0;

}
