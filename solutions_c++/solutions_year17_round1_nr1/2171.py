#include<bits/stdc++.h>
using namespace std;
void process(string &str){
int t;
    for(t=0;t<str.size();t++)
        if(str[t]!='?')break;
    for(int i=0;i<t;i++)
    str[i]=str[t];
    char tmp=str[t];
    for(int i=t+1;i<str.size();i++){
        if(str[i]=='?')
        str[i]=tmp;
        else
        tmp=str[i];
    }
}
int main(){
    int T;
    cin>>T;
    for(int t_i=0;t_i<T;t_i++){
        int R,C;
        cin>>R>>C;
        vector <string> s(R);
        for(int i=0;i<R;i++)
        cin>>s[i];
       // vector <char> ch(R,'');
        string tmp(C,'?');
        int t;
        // return 0;
        for(t=0;t<R;t++)
            if(s[t]!=tmp)break;
        process(s[t]);
        //cout<<s[t];
        for(int i=0;i<t;i++){
            s[i].assign(s[t]);
        }
        int p=t;
        for(int i=t+1;i<R;i++){
         //   cout<<i<<" ";
            if(s[i].compare(tmp)==0){
                s[i].assign(s[p]);
            }
            else{
               // cout<<"here";
                process(s[i]);
                p=i;
            }
        }
        printf("Case #%d:\n",t_i+1);
        for(int i=0;i<R;i++)
        cout<<s[i]<<"\n";
    }
    return 0;
}