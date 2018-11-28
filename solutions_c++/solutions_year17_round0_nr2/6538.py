#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin>>t;
    int k=t;
    while(t--){
        string n;
        cin>>n;
        if(n[n.length()]=='0')n[n.length()]='9';
        for(int i=n.length()-2;i>=0;i--){
            if(n[i]>n[i+1]){
                for(int j=i+1;j<n.length();j++)n[j]='9';
                int c=n[i]-'0';
                c--;
                char d='0'+c;
                n[i]=d;
            }
        }
        if(n.length()==1)cout<<"Case #"<<k-t<<": "<<n<<endl;
        else{cout<<"Case #"<<k-t<<": ";
            for(int i=0;i<n.length();i++){
                if(n[i]!='0')cout<<n[i];
            }
            cout<<endl;
        }
    }
    return 0;
}
