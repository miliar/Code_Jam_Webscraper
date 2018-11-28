#include<bits/stdc++.h>

using namespace std;

string printS(string s){

    int i ;
    for(i = 0; i < s.length(); i++){
        if(s[i] > '0')
            break;
    }
    return s.substr(i);
}

int main(){

    int t, l;
    string s;
    cin>>t;
    for(l = 0; l < t; l++){
        cin>>s;
        int i = s.length() - 2, j = 0;
        while(i >= 0){
           // cout<<s[i]<<endl;
            if(s[i] > s[i + 1]){
                if(s[i] == '0')
                    j = i;
                else{
                    s[i] = s[i] - 1;
                    j = i + 1;
                }
            }
            i--;
          //  cout<<i<<endl;
        }
       // cout<< j << endl;
        while(j > 0 && j < s.length()){
            s[j] = '9';
            j++;
        }
        cout<<"Case #"<<l+1<<": "<<printS(s)<<endl;
    }
return 0;
}
