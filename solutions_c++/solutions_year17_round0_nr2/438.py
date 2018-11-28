#include <cstdio>
#include <cstring>

int main(){
    freopen("B-large.in","r",stdin);
    freopen("Blargeoutput.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        char N[23];
        scanf("%s", N);
        int L = strlen(N);
        int i = 1;
        while (i<L&&N[i]>=N[i-1]) i++;
        if (i<L){
            int j = i;
            while (N[j-1]>=N[j]&&j>=0) j--;
            if (j==-1||(j==0&&N[j]=='1')){
                for (int k = 0; k < L-1; k++){
                    N[k] = '9';
                }
                N[L-1] = '\0';
            }
            else {
                N[j]--;
                for (int k = j+1; k < L; k++){
                    N[k] = '9';
                }
            }
            /*if (N[i-1]==1&&j==0){
                for (int k = 0; k < L-1; k++){
                    N[k] = '9';
                }
                N[L-1] = '\0';
            }
            else {
                int a = j;
                while (N[a]=='0'){
                    N[a] = '9';
                    a--;
                }
                for (int k = j; k < L; k++){
                    N[k] = '9';
                }
            }*/
        }
        printf("Case #%d: %s\n",t,N);
    }
}
