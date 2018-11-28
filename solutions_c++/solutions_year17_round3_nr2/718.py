#include<stdio.h>
#include<cstring>
#include<algorithm>

#define D 1

using namespace std;


int ex[1442*D][1442*D][2]; // ex[time][j][CJ] = the minim exchanges till time given J has worked for j, an 1 for J 0 for C

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,cases,i,j, Acs, Ajs, start, end;
    bool Ac[1442*D],Aj[1442*D]; //busy
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++)
    {
        scanf("%d%d",&Acs, &Ajs);
        memset(Ac,0,sizeof(Ac));
        memset(Aj,0,sizeof(Aj));
        for(i=1;i<=Acs;i++){
            scanf("%d%d",&start,&end);
            for(j=start;j<end;j++){
                Ac[j]=true;
            }
        }
        for(i=1;i<=Ajs;i++){
            //fprintf(stderr," i=%d Ajfs=%d\n",i,Ajs);
            scanf("%d%d",&start,&end);
            for(j=start;j<end;j++){
                Aj[j]=true;
            }
        }
        
        memset(ex,0,sizeof(ex));
        int an = 0;
        if(!Aj[0]){
		ex[1][1][1]=1;
        //fprintf(stderr,"here\n");
        for(i=1;i<1440*D;i++){
		    //fprintf(stderr,"i=%d\n",i);
            for(j=0;j<=720*D;j++){
                
                //
                if(ex[i][j][1]){
                //fprintf(stderr,",ex[%d][%d][0]=%d ,ex[%d][%d][1]=%d\n",i,j,ex[i][j][0],i,j,ex[i][j][1]); scanf("%*c");
                    if(!Aj[i]){
                        if(!ex[i+1][j+1][1] || ex[i+1][j+1][1]>ex[i][j][1])ex[i+1][j+1][1]=ex[i][j][1];
                    }
                    if(!Ac[i]){
                        if(!ex[i+1][j][0] || ex[i+1][j][0]>ex[i][j][1]+1)ex[i+1][j][0]=ex[i][j][1]+1;
                    }
                }
                if(ex[i][j][0]){
                //fprintf(stderr,",ex[%d][%d][0]=%d ,ex[%d][%d][1]=%d\n",i,j,ex[i][j][0],i,j,ex[i][j][1]);scanf("%*c");
                    if(!Aj[i]){
                        if(!ex[i+1][j+1][1] || ex[i+1][j+1][1]>ex[i][j][0]+1)ex[i+1][j+1][1]=ex[i][j][0]+1;
                    }
                    if(!Ac[i]){
                        if(!ex[i+1][j][0] || ex[i+1][j][0]>ex[i][j][0])ex[i+1][j][0]=ex[i][j][0];
                    }
                }
            }
        }
        an = ex[1440*D][720*D][0];
        if(an==0 || (ex[1440*D][720*D][1]>0 && an > ex[1440*D][720*D][1]-1)) an =ex[1440*D][720*D][1]-1;
        //fprintf(stderr," aaa an=%d\n",an);
        }
        memset(ex,0,sizeof(ex));
        if(!Ac[0]){ex[1][0][0]=1;
        //fprintf(stderr,"here\n");
        for(i=1;i<1440*D;i++){
		    //fprintf(stderr,"i=%d\n",i);
            for(j=0;j<=720*D;j++){
                
                //
                if(ex[i][j][1]){
                //fprintf(stderr,",ex[%d][%d][0]=%d ,ex[%d][%d][1]=%d\n",i,j,ex[i][j][0],i,j,ex[i][j][1]); scanf("%*c");
                    if(!Aj[i]){
                        if(!ex[i+1][j+1][1] || ex[i+1][j+1][1]>ex[i][j][1])ex[i+1][j+1][1]=ex[i][j][1];
                    }
                    if(!Ac[i]){
                        if(!ex[i+1][j][0] || ex[i+1][j][0]>ex[i][j][1]+1)ex[i+1][j][0]=ex[i][j][1]+1;
                    }
                }
                if(ex[i][j][0]){
                //fprintf(stderr,",ex[%d][%d][0]=%d ,ex[%d][%d][1]=%d\n",i,j,ex[i][j][0],i,j,ex[i][j][1]);scanf("%*c");
                    if(!Aj[i]){
                        if(!ex[i+1][j+1][1] || ex[i+1][j+1][1]>ex[i][j][0]+1)ex[i+1][j+1][1]=ex[i][j][0]+1;
                    }
                    if(!Ac[i]){
                        if(!ex[i+1][j][0] || ex[i+1][j][0]>ex[i][j][0])ex[i+1][j][0]=ex[i][j][0];
                    }
                }
            }
        }
        if(an<=0 || (ex[1440*D][720*D][0]>0 && an > ex[1440*D][720*D][0]-1))an = ex[1440*D][720*D][0]-1 ;
        if(an<=0 || (ex[1440*D][720*D][1]>0 && an > ex[1440*D][720*D][1])) an =ex[1440*D][720*D][1];
        
        }
        printf("Case #%d: %d\n",cases,an/D);
    }
    return 0;
}
