#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int t1;
    cin>>t1;
    for(int k=1;k<=t1;k++){
       
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
        int f=0;
        for(int i=l-size;i<l;i++){
            if(str[i]=='-'){
                cout<<"Case #"<<k<<": IMPOSSIBLE\n";
                f=1;
                //cout<<str<<count;
                break;
            }
        }
        if(f==0)
            cout<<"Case #"<<k<<": "<<count<<"\n";
    }
    
    return 0;
}
