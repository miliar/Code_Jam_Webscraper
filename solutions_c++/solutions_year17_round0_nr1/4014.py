#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
int check1(string s,int k)
{
    int t=0;
    for(int i=0;i+k<=s.size();i++){
        if(s[i]=='-'){
            t++;
            for(int j=i;j<i+k;j++){
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
        }
    }
    for(int i=0;i<s.size();i++){
        if(s[i]=='-') return -1;
    }
    return t;
}
int check2(string s,int k)
{
    reverse(s.begin(),s.end());
    int t=0;
    for(int i=0;i+k<=s.size();i++){
        if(s[i]=='-'){
            t++;
            for(int j=i;j<i+k;j++){
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
        }
    }
    for(int i=0;i<s.size();i++){
        if(s[i]=='-') return -1;
    }
    return t;
}
int main()
{
    freopen("data.out","w",stdout);
    int T;
    cin>>T;
    for(int kase=1;kase<=T;kase++){
        string S;
        int k,res;
        cin>>S>>k;
        if(check1(S,k)==-1&&check2(S,k)==-1)
            res=-1;
        else
            res=min(check1(S,k),check2(S,k));
        if(res==-1)
            cout<<"Case #"<<kase<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<kase<<": "<<res<<endl;

    }
    return 0;
}
