#include<iostream>
#include<string.h>
#include<stdio.h>
int v[30];
using namespace std;
int main(){
  freopen("input.txt", "r", stdin);
  freopen("outputBp.txt", "w", stdout);
  int t;
  scanf("%d\n", &t);
  for(int i=0;i<t;i++){
    string s;
    cin>>s;
    int n=0;
    while(s[n]!='\0') n++;
    //cout<<s<<" "<<n<<endl;
    v[0]=s[0]-'0';
    for(int j=1;j<n;j++){
      //cout<<"\t"<<v[j-1]<<" "<<(s[j]-'0')<<endl;
      if(v[j-1]<=(s[j]-'0')){
        v[j]=s[j]-'0';
      }else{
        //cout<<"\t entrato"<<endl;
        v[j]=s[j]-'0';
        int k=j-1;
        while(k>=0 && v[k]>v[k+1]){
          if(v[k]==0)
            v[k]=9;
          else
            v[k]--;

          k--;

        }
        for(int l=k+2;l<=j;l++)
          v[l]=9;
        for(int l=j;l<n;l++)
          s[l]='9';
      }
    }
    int k=0;
    while(v[k]==0)
      k++;
    cout<<"Case #"<<i+1<<": ";
    if(k==n)
      cout<<"0";
    for(;k<n;k++)
      cout<<v[k];

    cout<<endl;
  }
}
