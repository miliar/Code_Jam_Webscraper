#include <iostream>
using namespace std;
#include <stdio.h>
#include <string.h>

int main() {
	// your code goes here
	
	int t;
	int flip;
	int i,j;
	int c,temp;
	char s[50000];
    cin>>t;
    int err = 0;
    int tcase = 1;
    while(t--){
        c=0;
        err = 0;
        cin>>s;
        cin>>flip;
        for(i=0;i<strlen(s);i++){
            if(s[i]=='+'){
            continue;
            }else{
                c++;
                if(i>strlen(s)-flip){
                    cout<<"Case #"<<tcase<<": "<<"IMPOSSIBLE"<<endl;
                    err = 1;
                    break;
                }else{
                    for(j=i;j<i+flip;j++){
                        if(s[j]=='-'){
                            s[j]='+';
                        }else{
                            s[j]='-';
                        }
                    }    
                }
            }
        }
        
        if(!err){
            cout<<"Case #"<<tcase<<": "<<c<<endl;
           
        }
        tcase++;
        
    }
	return 0;
}
