#include <bits/stdc++.h>
using namespace std;
int pro(char A[],int k) {
    int cnt=0;
    for(int i=0;i<strlen(A)-k+1;i++) {
        if(A[i]=='-') {
            cnt++;
            for(int j=i;j<i+k;j++) {
                if(A[j]=='-') A[j]='+';
                else A[j]='-';
            }
            //printf("%s\n",A);
        }
    }
    for(int i=0;i<strlen(A);i++) {
        if(A[i]=='-') {
            return -1;
        }
    }
    return cnt;
}
int main() {
    int t;
    //freopen("input.txt","r",stdin);
    scanf("%d",&t);
    //FILE *f=fopen("output.txt","w");
    for(int i=0;i<t;i++) {
        char A[1005];
        scanf("%s ",A);
        int k;
        scanf("%d",&k);
        int r=pro(A,k);
        //fprintf(f,"Case #%d: ",i+1);
        //if(r==-1) fprintf(f,"IMPOSSIBLE\n");
        //else fprintf(f,"%d\n",r);
        printf("Case #%d: ",i+1);
        if(r==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",r);
    }
    return 0;
}
