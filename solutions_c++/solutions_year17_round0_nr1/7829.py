#include<bits/stdc++.h>
using namespace std;

int main(){

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    int cases = 1;
        while(t--){

                string s;
                cin>>s;

                int k;
                cin>>k;

                long long ans = 0;
                int ct = 0;

                for(int i = 0 ; i < s.size() ; i++){
                    if(s[i] == '+')
                        ct++;
                }
                if(ct == s.size()){
                    cout<<"Case #"<<cases++<<": "<<ans<<endl;
                    continue;
                }

                int idx;

                for(int i = 0 ; i < s.size() - k + 1 ; i++){
                    bool flag = false;
                    if(s[i] == '-'){
                        ans++;
                        for(int j = i ; j < i + k ; j++){
                            if(s[j] == '-')
                                s[j] = '+';
                            else{
                                s[j] = '-';

                                if(!flag){
                                    idx = j;
                                    flag = true;
                                }
                            }
                        }
                    }
                    if(flag)
                        i = idx - 1;
                }

                bool flag = false;
                for(int i = 0 ; i < s.size() ; i++){
                    if(s[i] == '-'){
                        flag = true;
                        break;
                    }
                }

                if(flag)
                    cout<<"Case #"<<cases++<<": "<<"IMPOSSIBLE"<<endl;
                else
                    cout<<"Case #"<<cases++<<": "<<ans<<endl;
        }
    return 0;
}
