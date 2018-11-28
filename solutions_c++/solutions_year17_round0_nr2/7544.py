#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++){

        string n;
        cin>>n;

        bool f=true;

        for(int i=1;i<n.length();i++)
            if(n[i]<n[i-1]) f=false;

        if(f)
        {
            cout<<"Case #"<<k<<": ";
            cout<<n<<endl;
            continue;
        }

        n[n.length()-1]--;

        for(int i=1;i<n.length();i++){

            if(n[i]<n[i-1]){

                while(i>=2&&n[i-1]-1<n[i-2])
                    i--;

                n[i-1]--;

                for(int j=i;j<n.length();j++)
                    n[j]='9';

                break;
            }
        }

        cout<<"Case #"<<k<<": ";

        int i=0;

        while(n[i]=='0') i++;

        for(;i<n.length();i++)
            cout<<n[i];

        cout<<endl;
    }
    return 0;
}
