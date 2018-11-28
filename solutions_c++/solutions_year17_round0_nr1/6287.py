#include<bits/stdc++.h>

using namespace std;

string S;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T,N,i;

    cin>>T;
    for(int z=1;z<=T;z++){

        cin>>S;
        cin>>N;
        cout<<"Case #"<<z<<": ";
        int len = S.length(), ans=0;
        i=0;
        while(i<len){
            while(S[i]=='+' && i<len){
                i+=1;
            }
            if(i+N-1>=len)
                break;
            if(i<len && S[i]=='-'){
                ans += 1;
                for(int j=i;j<=i+N-1;j++){
                    if(S[j]=='-'){
                        S[j]='+';
                    }
                    else{
                        S[j]='-';
                    }
                }
                //cout<<"i= "<<i<<"\t"<<S<<"\n";
                i+=1;
            }
        }
        bool flag=1;
        for(i=0;i<len;i++){
            if(S[i]=='-'){
                flag = 0; break;
            }
        }
        if(flag){
            cout<<ans<<"\n";
        }
        else{
            cout<<"IMPOSSIBLE\n";
        }

    }

    return 0;
}
