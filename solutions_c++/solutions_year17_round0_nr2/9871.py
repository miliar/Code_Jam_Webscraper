#include<bits/stdc++.h>
using namespace std;

int ara[10];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("Bsmallattempt1.out","w",stdout);
    int T,cs=0;
    scanf("%d", &T);
    while(T--)
    {
        int num;
        scanf("%d", &num);
        int p = num;
        int idx = 0;
        int ager = num%10;
        int f=0;
        memset(ara, 0, sizeof(ara));
        /*while(p)
        {
            int remd = p%10;
            ara[idx++] = remd;
            p = p/10;
            if(ager != remd) f=1;
            ager = remd;
        }
        if(idx==1 || f==0){
            printf("Case #%d: %d 1\n", ++cs, num);

            continue;
        }
        int flag=0;
        for(int i=0; i<idx-1; i++){
            if(ara[i] > ara[i+1]){
                flag=1;
                break;
            }
        }
        if(flag==0){
            printf("Case #%d: %d 2\n", ++cs, num);
            continue;
        }*/
        for(int i=num; i>=0; i--){
            memset(ara, 0, sizeof(ara));
            int idx=0;
            int p = i;
            while(p)
            {
                int remd = p%10;
                ara[idx++] = remd;
                p = p/10;
            }

            int flag1=0;
            for(int j=idx-1; j>0; j--){
                if(ara[j] > ara[j-1]){
                    flag1=1;
                    break;
                }
            }
            if(flag1==0){
                printf("Case #%d: %d\n", ++cs, i);
                break;
            }
        }

    }


    return 0;
}
