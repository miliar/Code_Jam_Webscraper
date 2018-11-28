#include<bits/stdc++.h>
using namespace std;

int main(){
    int i,j,k,t,T;
    long long int x,y,z,n;
    string str,str2;

    cin>>T;
    t=1;
    while(t<=T){
        cin>>x;
        str=to_string(x);
        n=str.size();
        i=n-1;
        while(i>0){
            if(str[i-1]>str[i]){
                str[i-1]--;
                
                j=i;
                while(j<n && str[j]!='9'){
                    str[j]='9';
                    j++;
                }
            }

            i--;
        }

        y=stoll(str);
        
        cout<<"Case #"<<t<<": ";
        //output here
        cout<<y;
        cout<<endl;

        t++;
    }

    return 0;
}
