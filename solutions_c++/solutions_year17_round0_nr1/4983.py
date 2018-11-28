#include<iostream>
using namespace std;
#define MAXN 10000
bool v[MAXN];
int sup[MAXN];
int main(){
  freopen("input.txt", "r", stdin);
  freopen("outputcj1_2.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    int j=0;
    char c;
    c=getchar();
    while(c!='+' && c!='-')
      c=getchar();
    //cout<<c;
    while(c=='+' || c=='-'){
      if(c=='+')
        v[j++]=1;
      else
        v[j++]=0;
      c=getchar();
      //cout<<c;

    }
    int l;
    scanf("%d", &l);
    //cout<<l<<endl;
    //cout<<j<<" "<<l<<" "<<j-l<<endl;
    int att=0;
    int ans=0;
    for(int k=0;k<j-l+1;k++){
      att+=sup[k];
      sup[k]=0;
      if((v[k]+att)%2==0){
        sup[k+l]--;
        ans++;
        att++;
      }
    }
    bool sw=true;
    for(int k=j-l+1;k<j;k++){
      att+=sup[k];
      sup[k]=0;
      if((v[k]+att)%2==0){
        sw=false;
        att++;
      }
    }
    for(int k=j;k<=1000;k++)
      sup[k]=0;
    if(sw){
      cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }else{
      cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    }

  }
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4
*/
