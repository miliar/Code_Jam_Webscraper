#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("C:\\Users\\Dell\\Desktop\\inp.in", "r", stdin);
	freopen("C:\\Users\\Dell\\Desktop\\output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int testcase = 1; testcase <= t; testcase++){
        string s;
        int k;
        cin>>s>>k;
        int n = s.length(),ans = 0;
        for(int i = 0; i < n; i++){
            if(s[i] == '-'){
                if(i + k - 1 >= n){
                    break;
                }
                ans++;
                for(int j = 0; j < k; j++){
                    if(s[i+j] == '+'){
                        s[i+j] = '-';
                    }
                    else{
                        s[i+j] = '+';
                    }
                }
            }
        }
        int tmp = 1;
        for(int i = 0; i < n; i++){
            if(s[i] == '-'){
                tmp = 0;
                break;
            }
        }
        if(tmp == 0){
            cout<<"Case #"<<testcase<<": "<<"IMPOSSIBLE"<<"\n";
        }
        else{
            cout<<"Case #"<<testcase<<": "<<ans<<"\n";
        }
    }
    return 0;
}
