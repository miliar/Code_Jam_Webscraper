#include <bits/stdc++.h>
#define ll long long int
#define sc scanf
#define pf printf
using namespace std;

int main(){
    freopen("C:\\Users\\14301131\\Desktop\\jam\\B-large.in","r",stdin);
    freopen("C:\\Users\\14301131\\Desktop\\jam\\outputFileName2.txt","w",stdout);
    int t;
    sc("%d",&t);
    string s;
    getline(cin,s);
    for(int i=1;i<=t;i++){
        getline(cin,s);
        //cout<<s<<endl;
        int sz=s.size();
        for(int j=0;j<sz-1;j++){
            if(s[j]>s[j+1]){
                s[j]=s[j]-1;
                j++;
                while(j<sz){
                    s[j]='9';
                    j++;
                }
            }
        }

        for(int j=sz-2;j>=0;j--){
            if(s[j]>s[j+1]){
                s[j+1]='9';
                s[j]--;

            }
        }
        stringstream ss;
        ss<<s;
        ll ld;
        ss>>ld;
        pf("Case #%d: %lld\n",i,ld);
    }
}
