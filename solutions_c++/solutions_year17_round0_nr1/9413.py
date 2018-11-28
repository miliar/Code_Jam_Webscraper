#include<bits/stdc++.h>
using namespace std;
int q,k,res,c=1,n;
string a;
main (){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ifstream in;    ofstream out;
    in.open("A-small-attempt1.in");
    out.open("A-small-attempt1.out");
    cin>>q;
    int i,j;
    bool ban=false;
    while(q--){
        cin>>a>>k;
        n=a.size();
        res=0;
        ban=false;
        cout<<"Case #"<<c++<<": ";
        for(i=0; i<n ;i++)
            if(a[i]=='-'){
                if(i+k>n){
                    cout<<"IMPOSSIBLE\n";
                    ban=true;
                    break;
                }
                for(j=0;j<k;j++)
                    if(a[j+i]=='-')
                        a[j+i]='+';
                    else
                        a[j+i]='-';
                res++;
            }
        if(!ban)
            cout<<res<<"\n";

    }
    in.close();
    out.close();
}
