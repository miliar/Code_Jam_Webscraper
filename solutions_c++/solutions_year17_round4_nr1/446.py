#include <bits/stdc++.h>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    int n,p;
    scanf("%d%d",&n,&p);
    int a[100],c[4]={0},S=0;
    for(int i=0;i<n;i++){
      scanf("%d",a+i);
      c[a[i]%p]++;
      S+=a[i];
    }
    int M=(S%p==0?0:1);
    if(p==2){
      M+=c[0]+c[1]/2;
    }
    else if(p==3){
      M+=c[0];
      int s=min(c[1],c[2]);
      M+=s,c[1]-=s,c[2]-=s;
      M+=c[1]/3+c[2]/3;
    }
    else if(p==4){
      M+=c[0];
      int s=min(c[1],c[3]);
      M+=s,c[1]-=s,c[3]-=s;
      int s1=min(c[1]/2,c[2]);
      M+=s1,c[1]-=s1*2,c[2]-=s1;
      int s3=min(c[3]/2,c[2]);
      M+=s3,c[3]-=s3*2,c[2]-=s3;
      M+=c[1]/4+c[3]/4+c[2]/2;
    }
    printf("Case #%d: %d\n",cs,M);
  }
  return 0;
}
