#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++){
        cout<<"Case #"<<i<<": ";
        string a;
        cin>>a;
        int n;
        cin>>n;
        int r=0;
        bool posible = 1;
        for(int j = 0; j < a.size(); j++){
            if(a[j] == '-'){
                r++;
                for(int k = j; k < j+n; k++){
                    if(k >= a.size()){
                        posible = 0;
                        break;
                    }
                    else{
                        if(a[k] == '-'){
                            a[k] = '+';
                        }
                        else{
                            a[k]='-';
                        }
                    }
                }
            }
        }
        if(posible){
            cout<<r<<endl;
        }
        else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
	return 0;
}
