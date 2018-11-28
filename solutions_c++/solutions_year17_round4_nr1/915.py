#include<stdio.h>

int main()
{
    FILE *fin,*fout;
    fin=fopen("C:\\Users\\owner\\Desktop\\2\\input1.txt","r");
    fout=fopen("C:\\Users\\owner\\Desktop\\2\\output1.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int tg;
        int pi;
        fscanf(fin,"%d%d",&tg,&pi);
        int num[4];
        for(int i = 0 ; i <= 3 ; i++){
            num[i] = 0;
        }
        int tnum;
        for(int i = 1 ; i <= tg ; i++){
            fscanf(fin,"%d",&tnum);
            int temp = tnum%pi;
            num[temp]++;
        }
        int gr = 0;
        gr+=num[0];
        if(pi==2){
            int temp = num[1]/2;
            gr += temp;
            if(num[1]%2 != 0){
                gr++;
            }
        }
        if(pi==3){
            if(num[1] == num[2]) gr+=num[2];
            if(num[1] > num[2]){
                gr+=num[2];
                num[1]-=num[2];
                int temp = num[1]/3;
                gr += temp;
                if(num[1]%3 != 0){
                    gr++;
                }
            }
            else if(num[2] > num[1]){
                gr+=num[1];
                num[2]-=num[1];
                int temp = num[2]/3;
                gr += temp;
                if(num[2]%3 != 0){
                    gr++;
                }
            }
        }
        if(pi==4){
            gr+=num[2]/2;
            num[2] = num[2]%2;
            if(num[1] >= num[3]){
                gr+=num[3];
                num[1]-=num[3];
                num[3] = 0;
                if(num[2]==1 && num[1]>=2){
                    gr++;
                    num[2]--;
                    num[1]-=2;
                }
                int temp = num[1]/4;
                num[1] = num[1]%4;
                gr += temp;
            }
            else if(num[3] > num[1]){
                gr+=num[1];
                num[3]-=num[1];
                num[1] = 0;
                if(num[2]==1 && num[3]>=2){
                    gr++;
                    num[2]--;
                    num[3]-=2;
                }
                int temp = num[3]/4;
                num[3] = num[3]%4;
                gr += temp;
            }
            for(int i = 1 ; i <= 3 ; i++){
                if(num[i] != 0){
                    gr++;
                    break;
                }
            }
        }

        fprintf(fout,"Case #%d: %d\n",q,gr);
    }
}
