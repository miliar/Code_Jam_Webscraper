#include<bits/stdc++.h>
using namespace std;


int main(){
    long long int test;
    cin>>test;
    long long int c=1;
    while(test--){

        string p;
        long long int k, count=0;
        cin>>p;
        cin>>k; //inputs taken


        for(long long int i=0; i<=p.length()-k; i++){  //parsing through the array
            if(p[i]=='-'){  //if getting a -ve entry switching the next k elements
                count=count+1;
                for(long long int j=i; j<k+i; j++){
                    if(p[j]=='-')
                        p[j]='+';
                    else
                        p[j]='-';
                }
            }
        }


        long long int flag=1;
        for(long long int i=p.length()-k; i<p.length(); i++){    //checking the last k elements
            if(p[i]=='-'){
                flag=0;
                break;
            }
        }

        cout<<"Case #"<<c<<": ";
        c++;
        if(flag==0)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<count<<endl;

        //cout<<p;
    }
}
