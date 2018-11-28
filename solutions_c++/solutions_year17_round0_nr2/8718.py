#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        string str;
        cin >> str;
        int flag=0,n=str.size();
        while(flag==0){
            flag=1;
            for(int j=0;j<n-1;j++){
                if(str[j]>str[j+1]){
                    str[j]=str[j]-1;
                    for(int k=j+1;k<n;k++)
                        str[k]='9';
                    flag=0;
                    break;
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(str[0]=='0'){
            for(int j=1;j<n;j++)
                cout << str[j];
        }
        else
            cout << str;
        cout << endl;
    }
    return 0;
}
