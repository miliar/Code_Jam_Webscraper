#include <iostream>
using namespace std;

bool isTidy(int a){
    int b = a % 10;
    a /= 10;
    while(a!=0) {
        if(a % 10 > b)
            return false;
        b = a % 10;
        a /= 10;
    }
    return true;
}

int main(){
    int t,num;
    cin>>t;
    for (int i = 1; i <= t; ++i){
        cin>>num;
        for(int o=num; o >= 1; o--)
            if(isTidy(o)) {
                cout << "Case #" << i << ": " << o << endl;
                break;
            }
    }
    return 0;
}
