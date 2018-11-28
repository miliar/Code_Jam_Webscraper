#include <bits/stdc++.h>
using namespace std;
int main(){
    int i,t,k,j,z;
    int len,count,imp;
    string l;
    cin>>t;
    for(i=0;i<t;i++){
        count=0;
        cin>>l;
        cin>>k;
        len=l.size();
        for(j=0;j<len+1-k;j++){
            if(l[j]=='-'){
                count++;
                for(z=0;z<k;z++){
                    if(l[j+z]=='-'){
                        l[j+z]='+';
                    }else{
                        l[j+z]='-';
                    }
                }
            }
        }
        imp=0;
        for(j=0;j<len;j++){
            if(l[j]=='-'){
                imp=1;
                break;
            }
        }
        if(imp==1){
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": "<<count<<endl;
        }
    }
    return 0;
}
