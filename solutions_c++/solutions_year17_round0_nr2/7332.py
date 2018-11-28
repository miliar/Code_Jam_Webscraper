#include<bits/stdc++.h>
using namespace std;

// problem B

int main()
{
    FILE *fp_in, *fp_out;

    char *input_file = "AA.in";
    char *output_file = "AA.o";

    fp_in = fopen(input_file,"r");
    fp_out = fopen(output_file,"w");

    char S[100];
    int T,i,j,k;
    bool found;

    fscanf(fp_in,"%d",&T);

    for(j=1;j<=T;j++){
        fscanf(fp_in,"%s",S);

        for(i=1;i<strlen(S);i++){
            if(S[i-1]>S[i]){
                S[i-1]--;
                for(k=i;k<strlen(S);k++)
                    S[k]=9+'0';
                i=0;
            }
        }

        fprintf(fp_out,"Case #%d: ",j);
        if(S[0]=='0'){
            for(i=1;i<strlen(S);i++)
                fprintf(fp_out,"%c",S[i]);
        }
        else {
            for(i=0;i<strlen(S);i++)
                fprintf(fp_out,"%c",S[i]);
        }
        fprintf(fp_out,"\n");
    }
    fclose(fp_in);
    fclose(fp_out);

    return 0;
}


