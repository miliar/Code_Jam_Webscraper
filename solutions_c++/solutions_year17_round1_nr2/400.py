#include<stdio.h>

int b[100];
int c[100];
int a[100][100];
int main(){
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  int t;
  int n,p;
  scanf("%d",&t);
  for(int tt=0;tt<t;tt++){
    scanf("%d %d",&n,&p);
    for(int i=0;i<n;i++)
      scanf("%d",&b[i]);
    
    for(int i=0;i<n;i++)
      for(int j=0;j<p;j++)
        scanf("%d",&a[i][j]);
    for(int i=0;i<n;i++)
      for(int j=0;j<p-1;j++)
        for(int k=0;k<p-j-1;k++)
          if(a[i][k]>a[i][k+1]){
            int tmp=a[i][k];
            a[i][k]=a[i][k+1];
            a[i][k+1]=tmp;
          }
    int ans=0;
    int tmp=1;
    for(int i=0;i<n;i++){
      c[i]=0;
    }
    bool tui=true;
    while(tui){
      bool flag=true;
      bool tmpp=true;
      for(int i=0;i<n;i++){
        double xiao=tmp*b[i]*0.9;
        double da=tmp*b[i]*1.1;
        if ((a[i][c[i]]+0.00001)<xiao){
          c[i]++;
          if (c[i]>=p) tui=false;
          flag=false;
          tmpp=false;
        }
        if ((a[i][c[i]]-0.00001)>da){
          flag=false;
        }
      }
      //printf("%d %d\n",ans,tmp);
      if (flag) {
        ans++; 
        for(int i=0;i<n;i++){
          c[i]++;
          if (c[i]>=p) tui=false;
        }
      }
      else if (tmpp) tmp++;
    }
    printf("Case #%d: %d\n",tt+1,ans);
  }
  fclose(stdin);
  fclose(stdout);
}