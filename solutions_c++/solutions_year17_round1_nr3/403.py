#include<stdio.h>
int ans=-1;
int b,d,hd,ad,hk,ak;
int check[105][105][105][105];
int tttt=0;
int cao;
void work(int k,int h,int a,int hh,int aa){
  if (a>hh) a=100;
  if(h<0) return;
  if (aa<0) aa=0;
  //if (cao>=96) printf("%d %d %d %d %d\n",k,h,a,hh,aa);
  if (check[h][a][hh][aa]>k){
    check[h][a][hh][aa]=k;
  } else return;
  //printf("%d\n",tttt++);
  if (hh<=0){
    if(k<ans || ans<0) ans=k;
    return;
  }
  if(k>ans) return;
  if (ans>0 && k>ans) return;
  if (!(((hh-a)>0) && ((h-aa)<=0))){
    if ((hh-a)<=0){
      if(k<ans || ans<0) ans=k;
      return;
    }
    work(k+1,h-aa,a,hh-a,aa);
  }
  if ((hd-h)>aa) work(k+1,hd-aa,a,hh,aa);
  if(!((h+d-aa)<=0)) if(aa>0) if(d>0){
    int cao=aa-d;
    if (cao<0 ) cao=0;
    work(k+1,h-cao,a,hh,cao);
  }
  if((h-aa)<=0) return;
  if(a>=hh) return;
  if(b>0 && a<=hh)  work(k+1,h-aa,a+b,hh,aa);
}
    
  
int main(){
 freopen("cc.in","r",stdin);
 freopen("c.out","w",stdout);
  int t;

  scanf("%d",&t);
  for(int tt=0;tt<t;tt++){
    for(int t1=0;t1<101;t1++)
      for(int t2=0;t2<101;t2++)
        for(int t3=0;t3<101;t3++)
          for(int t4=0;t4<101;t4++)
            check[t1][t2][t3][t4]=401;
          cao=tt;
    tttt=0;
    scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
    ans=401;
    work(1,hd,ad,hk,ak);
    if (ans<401) printf("Case #%d: %d\n",tt+1,ans);else printf("Case #%d: IMPOSSIBLE\n",tt+1);
  }
  fclose(stdin);
  fclose(stdout);
}