#include<bits/stdc++.h>
using namespace std;
bool f(string &L){
  for (int i = 1; i < L.size(); ++i)
  {
     if(L[i-1] <= L[i])continue;
     else return 0;
  }
  return 1;
}
int main(){
    int t, h;
    cin>>t;
    string last, num;
    for (int i = 1; i <= t; ++i){
      cin>>num;
      h = num.size();
      while(!f(num)){
        int pos = 0;
        for (int j = 1; j < h; ++j){
            if( num[j-1] > num[j]){
              if(num[j-1] == '1' && j == 1){
                num = "";
                for(int k = 1; k < h; k++){
                  num += "9";
                }
              }
              else{
                num[j-1] = (char)(num[j-1] - 1);
                for(int k = j; k < h; k++){
                  num[k] = '9';
                }
              }
              break;
            }
        }
        h = num.size();
      }
      cout<<"Case #"<<i<<": "<<num<<endl;
    }
}