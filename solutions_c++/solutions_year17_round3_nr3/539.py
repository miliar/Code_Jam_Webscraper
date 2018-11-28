#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    FILE *fin,*fout;
    fin=fopen("C:\\Users\\a123\\Desktop\\1C\\input3.txt","r");
    fout=fopen("C:\\Users\\a123\\Desktop\\1C\\output3.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int ctot,creq;
        fscanf(fin,"%d%d",&ctot,&creq);
        double utot;
        fscanf(fin,"%lf",&utot);
        double prob[105];
        for(int i = 1 ; i <= ctot ; i++){
            fscanf(fin,"%lf",&prob[i]);
        }
        for(int i = 1 ; i <= ctot-1 ; i++){
            for(int j = i+1 ; j <= ctot ; j++){
                if(prob[i] > prob[j]){
                    double temp = prob[i];
                    prob[i] = prob[j];
                    prob[j] = temp;
                }
            }
        }
        /*for(int i = 1 ; i <= ctot ; i++){
            printf("%lf ",prob[i]);
        }
        printf("\n");*/
        for(int i = 1 ; i <= ctot ; i++){
            double temp = 0;
            for(int j = 1 ; j <= i ; j++){
                temp+=prob[j];
            }
            temp+=utot;
            temp = temp/i;
            if(i == ctot){
                for(int j = 1 ; j <= i ; j++){
                    prob[j] = temp;
                }
                break;
            }
            else if(temp < prob[i+1]){
                for(int j = 1 ; j <= i ; j++){
                    prob[j] = temp;
                }
                break;
            }
        }
        double ans = 1;
        if(ctot == creq){
            for(int i = 1 ; i <= ctot ; i++){
                ans*=prob[i];
            }
            fprintf(fout,"Case #%d: %lf\n",q,ans);
        }
    }
}

