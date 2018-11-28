#include<stdio.h>
#include<string.h>

int pow(int ,int );

int main()
{
    FILE *fin,*fout;
    fin = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\input2.txt","r");
    fout = fopen("C:\\Users\\a123\\Desktop\\code jam QR\\output2.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        char inp[30];
        int num[30];
        fscanf(fin,"%s",inp);
        int lnum = strlen(inp);
        for(int i = 0 ; i < lnum ; i++){
            num[i] = inp[i] - '0';
        }
        if(lnum != 1){
            for(int i = lnum-1 ; i > 0 ; i--){
                if(num[i] < num[i-1]){
                    for(int j = lnum-1 ; j >= i ; j--){
                        num[j] = 9;
                    }
                    num[i-1]--;
                }
            }
        }
        fprintf(fout,"Case #%d: ",q);
        if(num[0] != 0) fprintf(fout,"%d",num[0]);
        for(int i = 1 ; i < lnum ; i++){
            fprintf(fout,"%d",num[i]);
        }
        fprintf(fout,"\n");
    }
}

int pow(int num , int ord)
{
    if(ord == 0) return 1;
    long long int ans = 1;
    for(int i = 1 ; i <= ord ; i++){
        ans = ans*num;
    }
    return ans;
}
