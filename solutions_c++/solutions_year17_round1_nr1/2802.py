#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int main() {
    int i,t,j,k,m,n,l=0;
    string s[30],st;
    cin>>t;
    while(t--){
        l++;
        cout<<"Case #"<<l<<":"<<endl;
        cin>>m>>n;
        for(i=0;i<m;i++){
              cin>>s[i];
            }
        for(i=0;i<m;i++){
            for(j=0;j<n;j++){
                if(s[i][j]!='?'){
                    for(k=j-1;s[i][k]=='?' && k>=0;k--){
                        s[i][k]=s[i][j];
                    }
                    for(k=j+1;s[i][k]=='?' && k<n;k++){
                        s[i][k]=s[i][j];
                    }
                }
            }
        }
          
        for(i=0;i<m;i++){
            if(s[i][j]!='?'){
                for(k=i-1;s[k][0]=='?' && k>=0;k--){
                    s[k]=s[i];
                }
             
                for(k=i+1;s[k][0]=='?' && k<m;k++){
                    s[k]=s[i];
                }
                }
            
        }
        
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            cout<<s[i][j];
        }
        cout<<endl;
    }   
       
    }      
    
 
	return 0;
}
