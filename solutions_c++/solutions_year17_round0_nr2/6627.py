#include "bits/stdc++.h"
using namespace std;
 
#define ll long long

string s;
int n;

void solve(vector <int> &v){
  vector <int> tmp;
  int specialCase = 0,idx=1;
  int pivot;
  tmp.push_back(v[0]);

  // get pivot point if any......
  for(;idx<n;idx++){
     if(v[idx]>=tmp[idx-1]){
        tmp.push_back(v[idx]);
     }
     else{
        pivot = v[idx];
        break;
     }
  }
  
  // check if pivot point
  if(tmp.size()!=n){  
     idx--;
     while(1){
         
         // Special Case ----------------------------------------
         if(idx==0){
            if(pivot!=0 ) { tmp[0]--; break; }
            else if(pivot ==0 and v[0]>1){ tmp[0]--; break;}
            else{
               specialCase=1;
               break;
            }
         }
         // -----------------------------------------------------

         if(tmp[idx] - tmp[idx-1] >=1){
            tmp[idx]--;
            break;
         }
         else{
           tmp.pop_back();
           idx--;
         }
     }

  // filling special case ..........   
  if(specialCase){
    tmp.clear();
    for(int i=0;i<n-1;i++)
      tmp.push_back(9);
  }

  else{
        idx++;
       for(;idx<n;idx++){
         tmp.push_back(9);
       }
     }
  }


  // print the string
  for(int i=0;i<tmp.size();i++){
    printf("%d",tmp[i]);
  }
  printf("\n");
}

int main(int argc, char const *argv[])
{
  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);
  int t; cin >> t;
  int tt = 0;
  while(t--){
    tt++;
    string s; cin >> s;
    n = s.length();
    vector<int>v;
    for(int i=0;i<n;i++){
       v.push_back(s[i]-'0');
    }
    printf("Case #%d: ",tt);
    solve(v);

  }
  return 0;
}