#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
void find(vector<int> );
int great(vector<int>& v1, vector<int>& v2);
int main(){
  freopen("B-large.in","r",stdin);
  freopen("output-tidy-numbers-large.out","w",stdout);
  int T;
  cin>>T;
  int x=T;
  for(int x=1;x<=T;x++){
    string input;
    cin>>input;
    int len=input.length();
    vector<int> num(len);
    for(int i=0;i<len;i++){
      num[i]=input[i]-'0';
    }
    cout<<"Case #"<<x<<": ";
    find(num);
  }
}
void find(vector<int> num){
  vector<int> copy=num;
  int len=num.size();
  for(int i=0;i<len;i++){
    for(int j=0;j<len-1;j++){
      if(copy[j]>copy[j+1]){
        copy[j]=copy[j]-1;
        copy[j+1]=9;
      }
    }
  }
  for(int i=len-1;i>=0;i--){
    if(copy[i]!=9){
      copy[i]++;
      if(!great(num,copy)) {copy[i]--; break;}
    }
  }
  int i=0;
  while(copy[i]==0) i++;
  for(i;i<len;i++) cout<<copy[i];
  cout<<endl;

}
int great(vector<int> &v1, vector<int> &v2){
  int len=v1.size();
  int isGreat=0;
  int k=0;
  while((k<len)){
    if(v1[k]==v2[k]) k++;
    else if(v1[k]<v2[k]) {isGreat=0; break;}
    else {isGreat=1; break;}
  }
  return isGreat;
}
