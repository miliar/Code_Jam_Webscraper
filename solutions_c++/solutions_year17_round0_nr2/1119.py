#include<bits/stdc++.h>
using namespace std;
char s[100];
char ans[100];
int n;
int check(int pos,int v){
    for(int i=pos;i<=n;i++){
        ans[i]=v+'0';
    }
    for(int i=1;i<=n;i++){
        if(ans[i]<s[i]){
            return 1;
        }
        else if(ans[i]==s[i]) continue;
        else return 0;
    }
}

int main(){
    FILE *fp1=fopen("C:\\Users\\Administrator\\Downloads\\B-large.in","r+");
    FILE *fp2=fopen("C:\\Users\\Administrator\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int ansnum=0;
    while(t--){
        memset(ans,NULL,sizeof(ans));
        fscanf(fp1,"%s",s+1);
        n=strlen(s+1);
        int cur='0';
        for(int i=1;i<=n;i++){
            for(int j=ans[i-1]-'0';j<=9;j++){
                if(check(i,j)) continue;
                else{
                    check(i,j-1);break;
                }
            }
        }

        long long ans1=0;
        long long x=1;
        for(int i=n;i>=1;i--){
            ans1+=x*(ans[i]-'0');
            x*=10;
        }
        fprintf(fp2,"Case #%d: %lld\n",++ansnum,ans1);

    }


}
