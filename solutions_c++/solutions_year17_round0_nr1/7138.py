#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int k=1;k<=t;k++){
       
        string str;
        cin>>str;
        int l=str.length();
        int size;
        int count=0;
        cin>>size;
        for(int i=0;i<l-size+1;i++){
            if(str[i]=='-'){
                count++;
                //cout<<count<<"\t"<<str<<"\n";
                for(int j=i;j<i+size;j++){
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
                //cout<<str<<"\n";
            }
        }
        int flag=0;
        for(int i=l-size;i<l;i++){
            if(str[i]=='-'){
                cout<<"Case #"<<k<<": IMPOSSIBLE\n";
                flag=1;
                //cout<<str<<count;
                break;
            }
        }
        if(flag==0)
            cout<<"Case #"<<k<<": "<<count<<"\n";
    }
    
    return 0;
}