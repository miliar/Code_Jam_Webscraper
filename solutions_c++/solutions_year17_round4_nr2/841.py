#include<stdio.h>

int main()
{
    FILE *fin,*fout;
    fin=fopen("C:\\Users\\owner\\Desktop\\2\\input2.txt","r");
    fout=fopen("C:\\Users\\owner\\Desktop\\2\\output2.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int st,mcus,tica;
        fscanf(fin,"%d%d%d",&st,&mcus,&tica);
        //int tp[mcus+1][1001];
        int cur[1001];
        int tot[1001];
        for(int i = 1 ; i <= 1001 ; i++){
            cur[i] = 0;
            tot[i] = 0;
        }
        for(int i = 1 ; i <= tica ; i++){
            int temp1,temp2;
            fscanf(fin,"%d%d",&temp1,&temp2);
            cur[temp2]++;
            tot[temp1]++;
            //tp[temp2][cur[temp2]] = temp1;
        }
        if(mcus == 2){
            int mlen = 0;
            if(cur[1] >= cur[2]){
                mlen = cur[1];
            }
            else mlen = cur[2];
            int jud = 0;
            if(tot[1] >= mlen){
                fprintf(fout,"Case #%d: %d 0\n",q,tot[1]);
            }
            else{
                int prom = 0;
                for(int i = 1 ; i <= st ; i++){
                    if(tot[i] > mlen){
                        prom += tot[i]-mlen;

                        break;
                    }
                }
                printf("%d %d %d\n",q,mlen,prom);
                fprintf(fout,"Case #%d: %d %d\n",q,mlen,prom);
            }
        }
    }
}
