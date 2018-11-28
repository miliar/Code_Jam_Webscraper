#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++){

        string s;
        cin>>s;
        int kk;
        cin>>kk;

        int c=0;
        bool f=true;

        for(int i=0;i<s.length();i++){

            if(s[i]=='-'){

                if(i+kk-1>=s.length()){
                    f=false;
                    break;
                }

                for(int j=i;j<i+kk;j++)
                    s[j]=(s[j]=='+'?'-':'+');

                c++;
            }
        }

        cout<<"Case #"<<k<<": ";

        if(f)
            cout<<c<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;

    }
    return 0;
}
