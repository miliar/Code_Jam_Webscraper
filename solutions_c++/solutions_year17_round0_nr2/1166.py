#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <set>
#include <numeric>
#include <cmath>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <queue>
#include <numeric>
#include <iomanip>
#define ll long long
using namespace std;
int testCase;
string ans;
string s;
bool fnd;
void go(int idx,int flag,char num,string &s){  //flag는 대소관계결정됫나
    if(idx==s.length()){
        fnd=true;
        return;
    }
    if(flag){
        ans.push_back('9');
        go(idx+1,flag,10,s);
    }
    else{
        char st='0'; char e=s[idx];
        if(idx=='0')st='1';
        for(char c=e;c>=num;c--){
            if(!fnd)ans.push_back(c);
            if(c<s[idx])go(idx+1,1,c,s);
            else go(idx+1,0,c,s);
            if(!fnd)ans.pop_back();
            if(fnd)return;
        }
    }
}
int main(){
    freopen("/Users/papaya0033/Desktop/B-small-attempt0.in","r",stdin);
    freopen("/Users/papaya0033/Desktop/B-small-attempt0.out","w",stdout);
    cin>>testCase;
    for(int t=1;t<=testCase;t++){
        fnd=false;
        s.clear(),ans.clear();
        string s; cin>>s;
        go(0,0,'1',s);
        if(ans.size()==0){
            for(int j=0;j<s.length()-1;j++)ans+='9';
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
    
    
    return 0;
}
