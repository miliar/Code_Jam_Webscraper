#include <iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    string s;int k;
    for(int i=0; i<t; i++){
        cin>>s>>k;
        int count=0;int t=0;
        int len=s.length();
        for(int j=0; j<=len; j++){
            if (s[j]=='-' ){
                if (j>=len-k+1){
                    cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
                t=1;
                break;
                }
            for(int a=j;a<k+j; a++){
                if(s[a]=='-')
                    s[a]='+';
                else
                    s[a]='-';
            }
            count++;
            }
            
        }
        if (t==0)
        cout<<"Case #"<<i+1 <<": "<<count<<endl;
    }
}
