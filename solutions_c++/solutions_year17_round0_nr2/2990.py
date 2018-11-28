#include<bits/stdc++.h>
using namespace std;

string dig;

int main(){
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++){
        cin>>dig;
        int gl_ref=0;
        while(!gl_ref){
            int lengths=dig.size();
            int val1s=0;
            for(int i=0;i<lengths-1;i++)
                if(dig[i]>dig[i+1]){
                    dig[i]=dig[i]-1;
                    for(int j=i+1;j<lengths;j++)
                        dig[j]='9';
                }
            
            for(int i=0;i<lengths-1;i++)
                if(dig[i]>dig[i+1]){
                    val1s=1;
                    break;
                }
            if(val1s==0)
                gl_ref=1;
        }
        cout<<"Case #"<<t <<": ";
        int lengths=dig.size(),j;
        for(int i=0;i<lengths;i++)
            if(dig[i]!='0'){
                j=i;break;
            }
        for(int i=j;i<lengths;i++)
            cout<<dig[i];
        cout<<endl;
    }
    return 0;
}
