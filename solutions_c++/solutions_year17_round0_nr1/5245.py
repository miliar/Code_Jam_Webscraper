#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
//��2ȡģ��01������
const int MAXN=2000;
//��equ�����̣�var����Ԫ�������������Ϊequ,����Ϊvar+1,�ֱ�Ϊ0��var
int equ,var;
int a[MAXN][MAXN]; //�������
int x[MAXN]; //�⼯
int free_x[MAXN];//�����洢���ɱ�Ԫ�����ö�����ɱ�Ԫ����ʹ�ã�
int free_num;//���ɱ�Ԫ�ĸ���
//����ֵΪ-1��ʾ�޽⣬Ϊ0��Ψһ�⣬���򷵻����ɱ�Ԫ����
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
            free_x[free_num++]=col;//��������ɱ�Ԫ 
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
    for(int i=k;i<equ;i++)if(a[i][col]!=0)return -1;//�޽�
    if(k<var)return var-k;//���ɱ�Ԫ����
    //Ψһ�⣬�ش�
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
