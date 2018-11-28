#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<cstring>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    FILE *inf, *outf;
    inf=fopen("B-small-attempt2.in","r");
    outf=fopen("B-small-attempt2-result.in","w");
    char c[8] = {'V','R','O','Y','G','B','V','R'};
    int T;
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
        int cn[6],tot;
        string ret = "";
        memset(cn,0,sizeof(cn));
        fscanf(inf,"%d %d %d %d %d %d %d",&tot,&cn[0],&cn[1],&cn[2],&cn[3],&cn[4],&cn[5]);
        bool isGood = true;
        for(int j=0;j<6;j++){
            if(cn[j]*1.0/tot > 0.5)isGood = false;
        }
        if(isGood){
            char beforeCh = 'M';
            for(int j=0;j<tot;j++){
                int maxVal=0;
                int maxPos=-1;
                for(int k=0;k<6;k++){
                    char try1Ch = c[k+1];
                    char try2Ch = c[k];
                    char try3Ch = c[k+2];
                    if(beforeCh == try1Ch || beforeCh == try2Ch || beforeCh == try3Ch)continue;
                    if(cn[k]>maxVal){
                        maxPos = k;
                        maxVal = cn[k];
                    }else if(cn[k] == maxVal && c[k+1] == ret[0]){
                        maxPos = k;
                        maxVal = cn[k];
                    }
                }
                ret = ret + c[maxPos + 1];
                cn[maxPos]--;
                beforeCh = c[maxPos + 1];
            }
        }
        if(ret.size() != tot){
            ret = "IMPOSSIBLE";
        }
        fprintf(outf,"Case #%d: %s\n",i+1,ret.c_str());       
    }
}