#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
//对2取模的01方程组
const int MAXN=2000;
//有equ个方程，var个变元。增广矩阵行数为equ,列数为var+1,分别为0到var
int equ,var;
int a[MAXN][MAXN]; //增广矩阵
int x[MAXN]; //解集
int free_x[MAXN];//用来存储自由变元（多解枚举自由变元可以使用）
int free_num;//自由变元的个数
//返回值为-1表示无解，为0是唯一解，否则返回自由变元个数
int Gauss(){
    int max_r,col,k;
    free_num=0;
    for(k=0,col=0;k<equ&&col<var;k++,col++){
        max_r=k;
        for(int i=k+1;i<equ;i++){
            if(abs(a[i][col])>abs(a[max_r][col]))max_r=i;
        }
        if(a[max_r][col]==0){
            k--;
            free_x[free_num++]=col;//这个是自由变元 
            continue;
        }
        if(max_r!=k){
            for(int j=col;j<var+1;j++)swap(a[k][j],a[max_r][j]);
        }
        for(int i=k+1;i<equ;i++){
            if(a[i][col]!=0){
                for(int j=col;j<var+1;j++)a[i][j]^=a[k][j];
            }
        }
    }
    for(int i=k;i<equ;i++)if(a[i][col]!=0)return -1;//无解
    if(k<var)return var-k;//自由变元个数
    //唯一解，回代
    for(int i=var-1;i>=0;i--){
        x[i]=a[i][var];
        for(int j=i+1;j<var;j++)x[i]^=(a[i][j]&&x[j]);
    }return 0;
}
int k,n,T;
char s[2010];
int main(){
	//freopen("A-small-attempt0.in","r",stdin);
	 //freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
    	printf("Case #%d: ",cas);
        memset(a,0,sizeof(a));
        scanf("%s%d",s,&k);
        n=strlen(s);
        for(int i=0;i<=n-k;i++){
            for(int j=0;j<k;j++)a[i+j][i]=1;
        }
        for(int i=0;i<n;i++){
		    if(s[i]=='-')a[i][n]=1;
            else a[i][n]=0;
		}equ=n,var=n;
        int u=Gauss();
        if(u==-1)puts("IMPOSSIBLE");
        else if(u==0){
		    int ans=0;
		    for(int i=0;i<n;i++)if(x[i])ans++;
            printf("%d\n",ans);
        }else{
            int ans=0x3f3f3f3f;
            int tot=1<<u;
            for(int i=0;i<tot;i++){
        	      int cnt=0;
        	      for(int j=0;j<u;j++){
        	          if(i&(1<<j)){
        	              x[free_x[j]]=1;
        	              cnt++;
        	          }else x[free_x[j]]=0;
        	      }for(int j=var-u-1;j>=0;j--){
        	          int idx;
        	          for(idx=j;idx<var;idx++)if(a[j][idx])break;
        	          x[idx]=a[j][var];
        	          for(int l=idx+1;l<var;l++){
        	              if(a[j][l])x[idx]^=x[l];
        	          }cnt+=x[idx];
        	      }ans=min(ans,cnt);
        	  }printf("%d\n",ans);
        }
    }return 0;
}
