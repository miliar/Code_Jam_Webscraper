#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>

#define PB push_back
using namespace std;

char color[6]={'R','O','Y','G','B','V'};
int cnt[6];
char ans[1100];

int main()
{
  freopen("B-small-attempt1.in","r",stdin);
  freopen("B-small-attempt1.out","w",stdout);
  //freopen("b.in","r",stdin);
  int test,cas(1);
  scanf("%d",&test);
  while(test--){
    int n;
    scanf("%d",&n);
    for(int i = 0; i < 6; ++i) scanf("%d",&cnt[i]);
    int j(0);
    int last(-1);
    while(cnt[1]>0 && cnt[4]>0){
      ans[j++]='B';
      ans[j++]='O';
      --cnt[4];--cnt[1];
      last=1;
    }
    if(last==1 && (ans[0] != 'B' || j < n)){
      ans[j++]='B';
      --cnt[4];
      last=4;
    }
    while(cnt[3]>0 && cnt[0]>0){
      ans[j++]='R';
      ans[j++]='G';
      --cnt[3]; --cnt[0];
      last=3;
    }
    if(last==3 && (ans[0] != 'R' || j < n)){
      ans[j++]='R';
      --cnt[0];
      last=0;
    }
    while(cnt[5]>0 && cnt[2]>0){
      ans[j++]='Y';
      ans[j++]='V';
      --cnt[5]; --cnt[2];
      last=5;
    }
    if(last==5 && (ans[0]!='Y' || j < n)){
      ans[j++]='Y';
      --cnt[2];
      last=2;
    }
    while(true){
      int b[] = {0,2,4};
      int cur=-1;
      for(int i = 0; i < 3;++i){
        if(cnt[b[i]]>0 && last != b[i]){
          if(cur==-1 || cnt[b[i]]>cnt[cur] 
          || (cnt[b[i]]==cnt[cur] && color[b[i]]==ans[0])){
            cur=b[i];
          }
        }
      }
      if(cur==-1) break;
      --cnt[cur];
      last=cur;
      ans[j++]=color[cur];
    }
    bool flag=true;
    for(int i = 0; i < 6; ++i)  {
      flag &= (cnt[i]==0);
    }
    string ptr(ans,n);
//    for(int i = 0; i < n;++i) ptr.append(ans[i]);
    if(!flag || (ans[0] == ans[n-1])){
      ptr="IMPOSSIBLE";
    }
    printf("Case #%d: %s\n",cas++,ptr.c_str());
  }


  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
