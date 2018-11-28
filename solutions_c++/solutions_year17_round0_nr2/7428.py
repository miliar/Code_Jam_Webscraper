#include<bits/stdc++.h>
using namespace std;


int main(){
    long long int test;
    cin>>test;
    long long int c=1, i, flag=0;
    while(test--){
        flag=0;
        string n;
        cin>>n;
        cout<<"Case #"<<c<<": ";
        c++;
        //cout<<n.length()<t max=(<endl;
        long long int cnt=0;
        if(n.length()==1)
            cout<<n<<endl;
        else{
            for(i=0; i<n.length()-1; i++){
                    if(n[i]>n[i+1]){
                        flag=1;
                        break;
                    }
                    if(n[i]==n[i+1]){
                        cnt++;
                    }
                    else
                    {cnt=0;}
                    //if(n[i]==n[i+1]){

                    //}
            }
            if(flag==0){
            }
            else{
            n[i-cnt]=(char)(n[i-cnt]-1);
            for(long long int j=i-cnt+1; j<n.length(); j++){
                n[j]='9';
            }
        }


        long long int k;
        for(k=0; k<n.length();k++){
        if(n[k]!='0')
            break;
        }
        for(long long int j=k; j<n.length();j++)
            cout<<n[j];
        cout<<endl;
    }
}
}
