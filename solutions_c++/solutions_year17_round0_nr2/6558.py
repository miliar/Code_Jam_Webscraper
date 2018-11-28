#include<bits/stdc++.h>
#define MX 100005
using namespace std;
typedef long long ll;

string func(string str){
     int i, j, k;
     int l=str.length();
     string ans="";
     for(i=1; i<l; ++i){
          if(str[i]<str[i-1]){
               for(j=i-1; j>=0; --j){
                    if(str[j]==str[i-1]) k=j;
                    else break;
               }
               str[k]--;
               for(j=k+1; j<l; ++j) str[j]='9';
               break;
          }
     }
     k=0;
     for(i=0; i<l; ++i){
          if(str[i]!='0') k=1;
          if(k) ans+=str[i];
     }
     return ans;
}

int main(){
     freopen("largeB.in", "r", stdin);
     freopen("largeB.txt", "w", stdout);
     string num;
     int i, j, k;
     int t, T;
     cin >> T;
     for(t=1; t<=T; ++t){
          cin >> num;
          cout << "Case #" << t << ": " << func(num) << endl;
     }
     return 0;
}

