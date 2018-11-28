#include <iostream>
using namespace std;

void flip(int a, int k, int arr[]){
    for(int i=0;i<k;i++){
        arr[a+i]=-arr[a+i];
    }
}

int main(){
    int S;
    cin>>S;
    
    for(int i=0;i<S;i++){
        string l;
        int K;
        int a[1000]={};
        
        cin>>l>>K;
        for(int j=0;j<l.size();j++){
            if(l[j]=='+'){
                a[j]=1;
            }else if(l[j]=='-'){
                a[j]=-1;
            }
        }
        
        int count=0;
        for(int j=0;j<l.size()-K+1;j++){
            if(a[j]==-1){
                flip(j, K, a);
                count++;
            }
        }
        
        bool succ = true;
        for(int j=0;j<l.size();j++){
            if(a[j]==-1){
                succ = false;
            }
        }
        cout<<"Case #"<<i+1<<": ";  
        if(succ){
            cout<<count<<endl;
        }else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
    
    return 0;
}