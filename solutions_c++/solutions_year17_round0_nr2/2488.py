#include <iostream>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int q = 1; q <= t; q++){
        string a;
        cin>>a;
        cout<<"Case #"<<q<<": ";

        if((int)a.size() == 1){
            cout<<a<<endl;
        }else{
            int i = 0;
            int l = (int)a.size();
            int inc = -1;
            int dec = -1;
            while(i < l-1){
                if(a[i+1] > a[i]){
                    inc = i;
                }else if(a[i+1] < a[i]){
                    dec = i;
                    break;
                }
                i++;
            }
            if(dec == -1){
                cout<<a<<endl;
            }else{
                if(inc == -1){
                    if(a[0] == '1'){
                        for(int j = 0; j < l-1; j++){
                            cout<<'9';
                        }
                        cout<<endl;
                    }else{
                        cout<<(a[0] - '0' - 1);
                        for(int j = 0; j < l-1; j++){
                            cout<<'9';
                        }
                        cout<<endl;
                    }
                }else{
                    for(int j = 0; j <= inc; j++){
                        cout<<a[j];
                    }
                    cout<<(a[inc+1] - '0' - 1);
                    for(int j = inc + 2; j < l; j++){
                        cout<<'9';
                    }
                    cout<<endl;
                }
            }
        }
    }
}
