#include <iostream>
#include <queue>

using namespace std;


void getLsRs(int n, int k){
    priority_queue<int> lengths;
    lengths.push(n);
    int temp;
    for(int i = 0; i<k-1; i++){
        temp = lengths.top();
        if(temp%2==0){
            lengths.push(temp/2);
            lengths.push(temp/2-1);
        }else{
            lengths.push((temp-1)/2);
            lengths.push((temp-1)/2);
        }
        lengths.pop();

    }

    temp = lengths.top();

    if(temp%2==0){
        cout<<temp/2<<" "<<temp/2-1<<endl;
    }else{
        cout<<temp/2<<" "<<temp/2<<endl;
    }
}

int main(){
    int n, k;

    int tc; cin>>tc;

    for(int i = 1; i<=tc; i++){
        cin>>n>>k;
        cout<<"Case #"<<i<<": ";
        if(n==k){
            cout<<0<<" "<<0<<endl;
        }else{
            getLsRs(n,k);
        }
    }

return 0;
}
