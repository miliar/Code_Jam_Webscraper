#include <iostream>
#include <string>
using namespace std;

int main() {
    int test;
    cin>>test;
    for(int k = 1;k <= test; k++){
       
        string st;
        cin>>st;
        int len = st.length();
        int m;
        int count = 0;
        cin>>m;
        for(int i = 0; i < len-m+1; i++){
            if(st[i] == '-'){
                count++;
                
                for(int j = i;j < i+m; j++){
                    if(st[j] == '-')
                        st[j] = '+';
                    else
                        st[j] = '-';
                }
                
            }
        }
        int temp = 0;
        for(int i=len-m; i<len;i++){
            if(st[i]=='-'){
                cout<<"Case #"<<k<<": IMPOSSIBLE\n";
                temp = 1;
                break;
            }
        }
        if(temp == 0)
            cout<<"Case #"<<k<<": "<<count<<"\n";
    }
    
    return 0;
}
