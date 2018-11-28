/**
Author:  ShivamRathore (Shivam010)
**/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
char ch[7]={'R','O','Y','G','B','V'};

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string out = "Case #";
        int n;
        pair<int,int> a[6];
        cin>>n;
        for(int i=0;i<6;i++){
            cin>>a[i].first;
            a[i].second=i;
        }
        char ans[n];
        bool flag=1;

        int p=-1,j=0;
        for(int i=0;i<n;i++){
            j=5;
            sort(a,a+6);
            while(a[j].first!=0 && j>=0){
                int in=a[j].second;
                if(p!=in){
                    if(p&1){
                        if(in!=p-1 && in!=(p+1)%6)
                            break;
                    }
                    else{
                        if(p!=in-1 && p!=(in+1)%6)
                            break;
                    }
                }
                j--;
            }
            if(j==-1){
                flag=0;
                break;
            }
            if(a[j].first==0){
                flag=0;
                break;
            }
            p=a[j].second;
            ans[i]=ch[p];
            a[j].first--;
        }
        if(ans[0]==ans[n-1])
            flag=0;
        cout<<out<<t<<": ";
        if(flag){
            for(int i=0;i<n;i++)
                cout<<ans[i];
            cout<<endl;
        }
        else
            cout<<"IMPOSSIBLE\n";
        /** answer **/
    }
    return 0;
}
