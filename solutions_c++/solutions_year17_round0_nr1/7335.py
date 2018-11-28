#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fp_in, *fp_out;

    char *input_file = "BB.in";
    char *output_file = "BB.o";

    fp_in = fopen(input_file,"r");
    fp_out = fopen(output_file,"w");

    int T,i,j,k,R,N;
    char A[2000];
    bool found;
    fscanf(fp_in,"%d",&T);
    for(i=1;i<=T;i++){
        found=false;
        R=0;
        fscanf(fp_in,"%s %d",A,&N);
        for(j=0;j<strlen(A);j++){
            if(A[j]=='-'){
                if(j+N<=strlen(A)){
                    R++;
                    for(k=j;k<j+N;k++){
                        if(A[k]=='+')
                            A[k]='-';
                        else
                            A[k]='+';
                    }
                }
                else {
                    found=true;
                    break;
                }
            }
        }
        if(!found)
            fprintf(fp_out,"Case #%d: %d\n",i,R);
        else
            fprintf(fp_out,"Case #%d: IMPOSSIBLE\n",i);
    }
    fclose(fp_in);
    fclose(fp_out);
    return 0;
}
