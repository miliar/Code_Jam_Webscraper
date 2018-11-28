#include <iostream>
using namespace std;

int main() {
    int t,i,j,k,f=0;
    string s;
    cin>>t;
    while(t--){
        f++;
        cin>>s;
        for(i=s.length()-1;i>0;i--){
            if(s[i]<s[i-1]){
                s[i-1]--;
                for(j=i;j<s.length();j++)
                    s[j]='9';
            }
        }
        cout<<"Case #"<<f<<": ";
        for(i=0;i<s.length();i++){
            if(s[i]=='0')
                continue;
            else{
                for(;i<s.length();i++)
                    cout<<s[i];
                    
            }
            cout<<endl;
                
        }
        
    }
 
	return 0;
}
