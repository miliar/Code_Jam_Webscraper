#include<stdio.h>

long long int pow(int ,int );
struct cart{
    long long int num;
    long long int amo;
};
int main()
{
    FILE *fin,*fout;
    fin = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\input3.txt","r");
    fout = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\output3.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        long long int stot,ptot;
        fscanf(fin,"%lld%lld",&stot,&ptot);
        cart cur[3],temp[3];
        if(stot%2 == 0){
            cur[1].num = stot/2;
            cur[2].num = stot/2-1;
            cur[1].amo = 1;
            cur[2].amo = 1;
        }
        else{
            cur[1].num = (stot-1)/2;
            cur[2].num = (stot-1)/2;
            cur[1].amo = 2;
            cur[2].amo = 0;
        }
        if(ptot == 1){
            if(stot%2 == 0){
                fprintf(fout,"Case #%d: %lld %lld\n",q,stot/2,stot/2-1);
            }
            else{
                fprintf(fout,"Case #%d: %lld %lld\n",q,(stot-1)/2,(stot-1)/2);
            }
            continue;
        }
        if(ptot == 2){
            if(cur[1].num%2 == 0){
                fprintf(fout,"Case #%d: %lld %lld\n",q,cur[1].num/2,cur[1].num/2-1);
            }
            else{
                fprintf(fout,"Case #%d: %lld %lld\n",q,(cur[1].num-1)/2,(cur[1].num-1)/2);
            }
            continue;
        }
        if(ptot == 3){
            if(cur[2].num%2 == 0){
                fprintf(fout,"Case #%d: %lld %lld\n",q,cur[2].num/2,cur[2].num/2-1);
            }
            else{
                fprintf(fout,"Case #%d: %lld %lld\n",q,(cur[2].num-1)/2,(cur[2].num-1)/2);
            }
            continue;
        }
        long long int totamo = 3;
        while(1){
            temp[1].num = 0;
            temp[1].amo = 0;
            temp[2].num = 0;
            temp[2].amo = 0;
            if(cur[1].num%2 == 0 && cur[1].num != 0){
                temp[1].num = cur[1].num/2;
                temp[1].amo += cur[1].amo;
                temp[2].num = cur[1].num/2-1;
                temp[2].amo += cur[1].amo;
                if(cur[2].amo!=0 && cur[2].num != 0){
                    temp[2].amo += cur[2].amo*2;
                }
            }
            else{
                temp[1].num = (cur[1].num-1)/2;
                temp[1].amo += cur[1].amo*2;
                if(cur[2].amo!=0 && cur[2].num != 0){
                    temp[1].amo += cur[2].amo;
                    temp[2].num = cur[2].num/2-1;
                    temp[2].amo += cur[2].amo;
                }
            }
            cur[1] = temp[1];
            cur[2] = temp[2];
            //printf("%lld %lld %lld %lld\n",cur[1].num,cur[1].amo,cur[2].num,cur[2].amo);
            totamo += cur[1].amo;
            if(totamo >= ptot){
                if((cur[1].num)%2 == 0){
                    fprintf(fout,"Case #%d: %lld %lld\n",q,cur[1].num/2,cur[1].num/2-1);
                }
                else{
                    fprintf(fout,"Case #%d: %lld %lld\n",q,(cur[1].num-1)/2,(cur[1].num-1)/2);
                }
                break;
            }
            totamo += cur[2].amo;
            if(totamo >= ptot){
                if((cur[2].num)%2 == 0){
                    fprintf(fout,"Case #%d: %lld %lld\n",q,cur[2].num/2,cur[2].num/2-1);
                }
                else{
                    fprintf(fout,"Case #%d: %lld %lld\n",q,(cur[2].num-1)/2,(cur[2].num-1)/2);
                }
                break;
            }
        }
    }
}

long long int pow(int num , int ord)
{
    if(ord == 0) return 1;
    long long int ans = 1;
    for(int i = 1 ; i <= ord ; i++){
        ans = ans*num;
    }
    return ans;
}
