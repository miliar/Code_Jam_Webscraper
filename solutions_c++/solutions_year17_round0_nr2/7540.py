#include <bits/stdc++.h>
using namespace std;


int main()
{
    int test;
    string str;
    int i, j, len, k;
    char temp;

    cin>>test;
    for(i=1; i<=test; ++i){
        cin>>str;
        len = str.length();
        bool decrease = false;
        for(j=0; j<len-1; ++j){
            if(str[j] > str[j+1]){
                if(str[j] == '1'){
                    decrease = true;
                }
                else{
                    k = j;
                    while(k-1 >=0 && str[k-1]==str[j])
                        k--;
                    str[k]--;
                    for(k=k+1; k<len; ++k){
                        str[k] = '9';
                    }
                }
                break;  //common, if we find one point break;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(decrease){
            for(int z = 0; z<len-1; ++z)
                cout<<"9";
        }
        else
            for(int z = 0; z<len; ++z)
                cout<<str[z];
        cout<<"\n";
    }
}
