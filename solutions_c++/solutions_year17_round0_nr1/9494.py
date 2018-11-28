#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    long long int i, x, j, l, n, t, k;
    cin>>t;
    for(k=1;k<=t;k++){
        x=0;
        string s;
        cin>>s;
        cin>>n;
        l=s.length();
        for(i=0;i<=l-n;i++){
            if(s[i]=='-'){
                for(j=i;j<i+n;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                x++;
            }
        }
        for(i=0;i<l;i++){
            if(s[i]=='-')
                x=-1;
        }
        cout<<"Case #"<<k<<": ";
        if(x==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<x<<endl;
    }
}

