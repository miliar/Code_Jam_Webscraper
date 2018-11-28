#include<bits/stdc++.h>
using namespace std;
void printoutput(int testcase,string ans){
    cout<<"Case #"<<testcase<<": "<<ans<<"\n";
    return;
}
void func(string s,int start,int last,int testcase){
    int tmp = 1,index;
    for(int i = start + 1; i < last; i++){
        if(s[i] < s[i-1]){
            tmp = 0;
            index = i;
            break;
        }
    }
    if(tmp == 1){
        string ans = "";
        for(int i = 0; i < s.length(); i++){
            if(s[i] != '0'){
                ans = ans + s[i];
            }
        }
        printoutput(testcase,ans);
        return;
    }
    s[index-1] = s[index-1] - 1;
    for(int i = index; i < last; i++){
        s[i] = '9';
    }
    func(s,0,index,testcase);
}
int main(){
    freopen("C:\\Users\\Dell\\Desktop\\inp.in", "r", stdin);
	freopen("C:\\Users\\Dell\\Desktop\\output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int testcase = 1; testcase <= t; testcase++){
        string s;
        cin>>s;
        int n = s.length();
        func(s,0,n,testcase);
    }
    return 0;
}
