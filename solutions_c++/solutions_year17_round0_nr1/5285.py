#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void flipK(string &s,int i,int k){
    for(int j=i;j<i+k;j++){
        if(s[j]=='-')
            s[j]='+';
        else
            s[j]='-';
    }
}

int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int flips =0;
        //Move inwards from both side flipping . Proved that this is correct.
        int flag=0;
        for(int l=0;l<n/2;l++){
            
            if(k>(n-2*l) && (s[l]=='-' || s[n-l-1]=='-')){
                cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
                flag=1;
                break;
            }
            if( (k==(n-2*l) && s[l]!=s[n-l-1])){
                cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
                flag=1;
                break;
            }
            if(s[l]=='-' && s[n-l-1]=='-' && k==(n-2*l) ){
                flipK(s,l,k);
                flips++;
            }
            else{
                if(s[l]=='-'){
                    flipK(s,l,k);
                    flips++;
                }
                if(s[n-l-1]=='-'){
                    flipK(s,n-l-k,k);
                    flips++;
                }
            }   
        }
        if(flag==0){
            //n odd and middle - with all other +
            if(n%2!=0 && s[n/2]=='-'){
                cout << "Case #" << i+1 << ": IMPOSSIBLE"<<endl;
            }
            else
                cout << "Case #" << i+1 << ": "<< flips<<endl;
        } 
    }
  return 0;
}
