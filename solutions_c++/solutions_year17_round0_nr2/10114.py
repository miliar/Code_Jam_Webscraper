#include <iostream>
using namespace std;
int main(){
  int t;
  cin>>t;
  string s[t];
  for(int m=0;m<t;m++){
  cin>>s[m];
  int flage=1;
  for(int i=0;s[m][i+1];i++){if(s[m][i+1]<s[m][i]) {flage=0; break;} }
  if(flage==0){
  for(int j=0;s[m][j+1];j++){
    if(s[m][j+1]<=s[m][j]){
      char max=s[m][j];
      //cout<<j;
      int max_index=j;
        for(int i=j;s[m][i];i++){
          if(s[m][i]>max){
            max=s[m][i];
            max_index=i;
            //cout<<max<<endl;
        }
      }
      if(max_index==s[m].length()-1) {
        s[m][j]=s[m][j]-1;
        for(int i=j+1;s[m][i];i++) s[m][i]=9+48;
      }
      else{
      //cout<<max_index<<" "<<max<<endl;
      s[m][max_index]=s[m][max_index]-1;
      for(int k=max_index+1;s[m][k];k++){
        s[m][k]=9+48;
      }
    }
      break;
    }
  }
}
}
  for(int i=0;i<t;i++) {
    cout<<"Case #"<<i+1<<": "; 

    int flag=0;
    for(int j=0;s[i][j];j++){
    if(s[i][j]==48 && flag==0){}
    else {
      cout<<s[i][j];
      flag=1;
      }
    }
    cout<<endl;
  }


}
