#include <iostream>
using namespace std;
 string str;
 int k , n;
 int ans = 0;
 int dp(string str12 , int count , int i , int ans) {
     if(i == n) {
        //  cout<<str12<<" "<<count<<endl;  
         if(count == 0) {
             return ans;
         }
         return 0;
     }
     int nk = count;
     string str1 = str12;
     if(n-i >= k) {
        for(int j = i ; j < i+k ; j++) {
            if(str12[j] == '-') {
                count --;
                str12[j] = '+';
            }
            else {
                count ++;
                str12[j] = '-';
            }
        }
        return max( dp(str12 , count , i+1 , ans+1) ,dp(str1 , nk , i+1 , ans));
     }
        return dp(str1 , nk , i+1 , ans);
 }
int main() {
    int test;
    cin>>test;
    int all = test;
    while(test--) {
        cin>>str;
        cin>>k;
        int count = 0;
        n = str.length();
        for(int i  = 0 ; i < n ;i ++) {
            if(str[i] == '-') {
                count ++;
            }
        }
        if(count ) {
            int l = dp(str ,  count , 0 , 0);
            if(l) {
                cout<<"Case #"<<all-test<<": "<<l<<endl;
            }
            else {
                 cout<<"Case #"<<all-test<<": IMPOSSIBLE"<<endl;
            }
        }
        
        else
        cout<<"Case #"<<all-test<<": 0"<<endl;
        
        
    }
    return 0;
}
