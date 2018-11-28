#include <vector>
#include <iostream>

using namespace std;
int main(){
    int t;cin>>t;
    int caseno=1;
    while(t--){
        long int no;cin>>no;
        string s=to_string(no);
        int pos=1;
        //cout<<no<<" ";
        while(pos<s.length()){
         //   cout<<"here"<<endl;
            if(s[pos]<s[pos-1]){
                break;
            }
            pos++;
        }
        if(pos==s.length()){
            cout<<"Case #"<<caseno<<": "<<no<<endl;
        }
        else{
            if(s[pos]=='0' && s[pos-1]=='1'){
                string ans1="";
                int j=1;
                int slen=s.length();//cout<<slen<<" "<<j<<endl;
                while(j<slen){
                    //cout<<"here1"<<endl;
                    ans1.push_back('9');j++;
                   // cout<<ans1<<endl;
                }
                cout<<"Case #"<<caseno<<": "<<ans1<<endl;
            }
            else{
                string ans1=s.substr(0,pos);
                char prob=s[pos-1];
                
                int k=pos-2;
                while(k>=0 && ans1[k]==ans1[k+1]){
                    ans1[k+1]='9';k--;
                }
                if(k>=0)ans1[k+1]=ans1[k+1]-1;
                
                else ans1[0]=ans1[0]-1;
                
                int j=pos;
                while(j<s.length()){
 //                   cout<<"here2"<<endl;
                    ans1.push_back('9');j++;
                }
                cout<<"Case #"<<caseno<<": "<<ans1<<endl;
            }
        }
        caseno++;
    }
}
