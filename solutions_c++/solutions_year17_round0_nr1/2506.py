#include<bits/stdc++.h>
using namespace std;
string s,s1;
int l,k;
int make(){
    int cnt = 0;
    for(int i=0;i<l;i++){
        if(s[i] == '-'){
            if(i+k <= l){
                cnt++;
                for(int j=i;j<i+k;j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
    }
    return cnt;
}
bool check(){
    for(int i=0;i<l;i++){
        if(s[i] == '-')
            return 0;
    }
    return 1;
}
int main(){
    int test;
    cin >> test;
    for(int t=0;t<test;t++){
        int ans = INT_MAX;
        cin >> s;
        s1 = s;
        l = s.size();
        cin >> k;
        int temp1 = make();
      //  cout << temp1 << endl;
        if(check())
            ans = min(ans,temp1);
        else{
            reverse(s.begin(),s.end());
            int temp2 = make();
            if(check())
                ans = min(ans,temp1+temp2);
        }
        s = s1;
        reverse(s.begin(),s.end());
        temp1 = make();
        if(check()) 
            ans = min(ans,temp1);
        else{ 
            reverse(s.begin(),s.end());
            int temp2 = make();
            if(check()) 
                ans = min(ans,temp1+temp2);
        }
        if(ans == INT_MAX)
            printf("Case #%d: IMPOSSIBLE\n",t+1);
        else
            printf("Case #%d: %d\n",t+1,ans);
    }
    return 0;
}
