#include <iostream>
using namespace std;

int main() {
    int t,n,tok=1;
    cin>>t;
    while(t--){
        int count=0, flag=0;
        string s;
        cin>>s>>n;
        for(int i=0;i<s.length();i++){
            if(s[i]=='-'){
                if(n<=(s.length()-i)){
                    count++;
                    for(int j=i,p=0;p<n;j++,p++){
                        if(s[j]=='-'){
                            s[j]='+';
                        }
                        else
                            s[j]='-';
                    }
                }
            }
        }
        for(int i=0;i<s.length();i++){
            if(s[i]=='-'){
                cout<<"Case #"<<tok++<<": "<<"IMPOSSIBLE"<<endl; flag=1; break;
            }
        }
        if(flag==0)
            cout<<"Case #"<<tok++<<": "<<count<<endl;
        
    }
	return 0;
}

