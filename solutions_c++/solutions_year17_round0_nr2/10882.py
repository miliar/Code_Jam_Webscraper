#include<bits/stdc++.h>
using namespace std;
void mf(int nl,int narr[]){
    int printedTill=-1;
    if(nl==1){
        cout<<narr[0];
    }
    for(int i=0;i<nl-1;i++){
        if(narr[i]>narr[i+1]){
            if(narr[i]-1!=0)
                cout<<narr[i]-1;
            for(int j=printedTill;j<nl-2;j++){
                cout<<'9';
            }
            break;
        }
        else if(narr[i]==narr[i+1]){
            if(i==nl-2){
                for(int j=printedTill;j<nl-1;j++){
                    cout<<narr[i];
                }
            }
        }
        else{
            for(int j=printedTill;j<i;j++){
                cout<<narr[i];
                printedTill++;
            }
            if(i==nl-2){
                cout<<narr[nl-1];
            }
        }
    }
}
void fn(){
    long long int n,k;
    cin>>n;
    k=n;
    int nl=0;
    while(k){
        nl++;
        k/=10;
    }
    k=n;
    int narr[nl];
    for(int i=0;i<nl;i++){
        narr[nl-i-1]=k%10;
        k=k/10;
        //cout<<narr[nl-i-1]<<' ';
    }
    mf(nl,narr);
}

int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": ";
        fn();
        cout<<'\n';
    }
}
