#include <iostream>
using namespace std;

int tidy(int n){
    int m, mm;
    bool found;
    if(n < 10)return n;
    while(n){
        found=true;
        m = n;
        mm = m%10;
        while (m){
            if(m%10 > mm%10){
                found=false;
                break;
            }
            mm = m%10;
            m/=10;
        }
        if(found)return n;
        n--;
    }
    return n;
}

int main(){
    int t,n;
    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> n;
        cout << "Case #" <<  i << ": " << tidy(n) << endl;
    }
    return 0;
}
