#include<bits/stdc++.h>
using namespace std;

void solve(int n,int k){
    if(n==k){
        cout<<"0 0"<<endl;
        return;
    }
    vector<int> aux;
    aux.push_back(n);
    make_heap(aux.begin(),aux.end());
    for(int i=0;i<k-1;i++){
        int top=aux.front();
        pop_heap(aux.begin(), aux.end());
        aux.pop_back();
        // for(int j=0;j<aux.size();j++){
        //     cout<<aux[j]<<" ";
        // }
        // cout<<endl;
        // if(top%2==0){
            aux.push_back(top/2);
            push_heap(aux.begin(), aux.end());
            aux.push_back((top-1)/2);
            push_heap(aux.begin(), aux.end());
        // }
        // else{

        // }
    }
    // int maxE=INT_MIN,minE=INT_MAX;
    // for(int i=0;i<aux.size();i++){
    //     maxE=max(maxE,(aux[i])/2);
    //     minE=min(minE,(aux[i]-1)/2);
    // }
    int maxi= *max_element(aux.begin(),aux.end());
    int maxE=maxi/2;
    int minE=(maxi-1)/2;
    cout<<maxE<<" "<<minE<<endl;
}
int main(){

    int tCase;
    cin>>tCase;
    for(int t=1;t<=tCase;t++){
        int n,k;
        cin>>n>>k;
        cout<<"Case #"<<t<<": ";
        solve(n,k);
    }
    return 0;
}