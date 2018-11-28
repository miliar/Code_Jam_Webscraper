#include<bits/stdc++.h>
using namespace std;
int main(){
    int test;
    cin >> test;
    for(int t=0;t<test;t++){
        string s;
        cin >> s;
        long long int l = s.size();
        long long int i;
        for(i=1;i<l;i++){
            if(s[i]-'0' >= s[i-1]-'0')
                continue;
            else{
                while(i >= 0 && s[i]-'0' < s[i-1]-'0'){
                    s[i-1]--;
                    i--;
                }
                break;
            }
        }
        for(int j=i+1;j<l;j++){
            s[j] = '9';
        }
        long long ans = 0;
            long long temp = 1;
        for(int i=l-1;i>=0;i--){
            ans += temp*(s[i]-'0');
            temp*=10;
        }
        printf("Case #%d: %lld\n",t+1,ans);
    }
    return 0;
}
