#include <bits/stdc++.h>

using namespace std;

void failure(){
    cout<<"IMPOSSIBLE"<<endl;
}
void success(int res){
    cout<<res<<endl;
}

int minSteps(string s,int k){
    int it =0;
    int slen = s.length();
    int ans =0;
    while(it<slen-k+1){
        if(s[it]=='-'){
            for(int j=it;j<it+k;j++){
                s[j]=='-'?s[j]='+':s[j]='-';
            }
            ans++;
        }
        it++;
    }
    //cout<<s<<endl;
    for(int i=slen-1;i>=0;i--){
        if(s[i]=='-'){
                return -1;
        }
    }
    return ans;
}

int main()
{
    freopen("A2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int iter=1;iter<=T;iter++){
        string s;
        cin>>s;
        int k;
        cin>>k;

        cout<<"Case #"<<iter<<": ";

        int slen = s.length();
        int f =0;
        for(int i=0;i<slen;i++){
            if(s[i]=='-'){
                f =1;
                break;
            }
        }
        if(f==0){
            success(0);
            continue;
        }
        if(slen<k){
            failure();
            continue;
        }

        int ans = minSteps(s,k);
        if(ans==-1){
            failure();
            continue;
        }
        else{
            success(ans);
            continue;
        }


    }
}
