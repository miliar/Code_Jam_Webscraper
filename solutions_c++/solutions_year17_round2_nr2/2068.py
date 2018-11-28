#include<cstdio>
#include<cstring>
int main(){
    freopen("input.in","r+",stdin);
    freopen("output.out","w+",stdout);
    int T,n,arr[7],circle[1004]={0,},b,m1,m2,m3;
    char c[7];
    c[1]='R',c[3]='Y',c[5]='B';
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&n);
        b=0;
        memset(circle,0,sizeof(circle));
        for(int i=1;i<=6;i++)
            scanf("%d",&arr[i]);
      
        for(int i=1;i<=6;i++){
            if(arr[i]>n/2)
                b=1;
        }
        if(b){
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
        else{
            printf("Case #%d: ",t);
            for(int i=0;i<n;i++){
                if(arr[1]>=arr[3] && arr[1]>=arr[5]){
                    m1=1;
                    if(arr[3]>=arr[5])
                        m2=3,m3=5;
                    else
                        m2=5,m3=3;
                }
                else if(arr[3]>=arr[5] && arr[3]>=arr[1]){
                    m1=3;
                    if(arr[1]>=arr[5])
                        m2=1,m3=5;
                    else
                        m2=5,m3=1;
                }
                else{
                    m1=5;
                    if(arr[1]>=arr[3])
                        m2=1,m3=3;
                    else
                        m2=3,m3=1;
                }
                if(circle[(i-1+n)%n]!=m1){
                    if(i==n-2){
                        if(circle[0]!=m2){
                            circle[i]=m1;
                            arr[m1]--;
                            printf("%c",c[m1]);
                        }
                        else{
                            circle[i]=m2;
                            arr[m2]--;
                            printf("%c",c[m2]);
                        }
                    }
                    else{
                        circle[i]=m1;
                        arr[m1]--;
                        printf("%c",c[m1]);
                    }
                }
                else{
                    circle[i]=m2;
                    arr[m2]--;
                    printf("%c",c[m2]);
                }
            }
            printf("\n");
        }

    }
}
