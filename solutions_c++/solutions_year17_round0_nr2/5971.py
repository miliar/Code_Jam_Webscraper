#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string Ans;
bool getT(string& str, int pos,int minVal){
    if(pos==str.length()) return true;
    int curVal= str[pos]-'0';

    if(curVal>=minVal && getT(str,pos+1,max(curVal,minVal))){
        if(pos!=0 || str[pos]!=0)
            Ans= str[pos] + Ans;
        return true;
    }else{
        if(curVal==0 || curVal-1<minVal) return false;
        Ans="";
        for(int i=pos+1;i<str.length();++i) Ans+='9';
        if(curVal-1!=0 | pos!=0)Ans = (char)(str[pos]-1) + Ans;
        return true;
    }


}
int main(){
    int T; scanf("%d",&T);
    for(int tc=1;tc<=T;++tc){
        Ans="";
        string N;         
        cin >> N;        
        getT(N,0,0);
        printf("Case #%d: ",tc);
        cout << Ans<<endl;
    }
    return 0;
}