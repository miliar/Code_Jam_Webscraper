#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;



int main() {
    
    int t;
    cin >> t;
    string s;
    int k;
    for(int i = 0; i < t; i++){
        cout<<"Case #"<<i+1<<": ";
        cin >> s>>k;
        int count=0;
        int length=s.length();
        vector<int> str(length,0);
        for(int j=0;j<length;j++){
            if(s.substr(j,1)=="-"){
                str[j]=0;
            }else{
                str[j]=1;
            }
        }
        for(int j=0;j+k-1<length;j++){
            if(str[j]==0){
                count++;
                for(int a=0;a<k;a++){
                    if(str[j+a]==0){
                        str[j+a]=1;
                    }else{
                        str[j+a]=0;
                    }
                }
            }
        }
        int j=0;
        while(j<k){
            if(str[length-j-1]==0){
                cout<<"IMPOSSIBLE"<<endl;
                break;
            }
            j++;
        }
        if(j==k){
            cout<<count;
        cout<<endl;
        }
    }
    
    return 0;
}


