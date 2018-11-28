#include <iostream>
using namespace std;

bool is_tidy(int a){
    int prev=10;
    for(;a>=1;a/=10){
        if(prev<a%10){
            return false;
        }
        prev=a%10;
    }
    return true;
}

int main(){
    int N;
    cin>>N;

    for(int i=0;i<N;i++){
        int a;
        cin>>a;

        for(int b=a;b>0;b--){
            if(is_tidy(b)){
                cout<<"Case #"<<i+1<<": "<<b<<endl;
                break;
            }
        }

    }
    return 0;
}
