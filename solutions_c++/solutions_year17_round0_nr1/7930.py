#include <bits/stdc++.h>

using namespace std;

int main(){
    int tests,i,k,n,offset;
    long long int flips;
    bool valid;
    vector<int>res;
    cin>>tests;
    for(int t=0;t<tests;++t){
        string st;
        cin>>st>>k;
        n=st.size();
        res.assign(n+1,0);
        flips=0;
        for(i=0;i<n;i++){
            offset=st[i]=='-'?0:1;
            if(i<n-k+1 && (res[i]+offset)%2==0){
                res[i]++;
                res[i+k]--;
                flips++;
            }
            res[i+1]+=res[i];
        }
        valid=true;
        for(i=0;i<n;i++){
            offset=st[i]=='-'?0:1;
            if((res[i]+offset)%2==0){
                valid=false;
                break;
            }
        }
        cout<<"Case #"<<t+1<<": ";
        if(valid)
            cout<<flips<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    }
}
