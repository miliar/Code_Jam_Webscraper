#include <cstdio>
#include<vector>
#include<algorithm>
#include <cmath>
using namespace std;

int pack[50][50];
int mini[50][50];
int maxi[50][50];
int rata[50];
int cursor[50];

int main(){
int t;
scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n,p;
        int res=0;
        scanf("%d%d",&n,&p);
        for(int i=0;i<n;i++){
            scanf("%d",&rata[i]);
            cursor[i]=0;
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                scanf("%d",&pack[i][j]);
            }
            sort(&pack[i][0],&pack[i][p]);
            for(int j=0;j<p;j++){
                mini[i][j]=std::ceil((double) pack[i][j] / ((double) rata[i]*1.1));

                int x=mini[i][j];
                while((x-1)*rata[i]*1.1 >= pack[i][j]){x--;}
                mini[i][j]=x;

                if(mini[i][j]==0){mini[i][j]=1;}
                maxi[i][j]=std::floor((double) pack[i][j] / ((double) rata[i]*0.9));
                
                x=maxi[i][j];
                while((x+1)*rata[i]*0.9 <= pack[i][j]){x++;}
                maxi[i][j]=x;
                
                //printf("%d %d\n",mini[i][j],maxi[i][j]);
                if(mini[i][j]>maxi[i][j]){maxi[i][j]=-1;}
            }
        }
        int maxcursor=0;
        while(maxcursor<p){
            int lmin=mini[0][cursor[0]];
            int lmax=maxi[0][cursor[0]];

            for(int i=1;i<n;i++){
                lmin=max(lmin,mini[i][cursor[i]]);
                lmax=min(lmax,maxi[i][cursor[i]]);
            }
            if(lmin<=lmax){
                //printf("v %d %d %d\n",cursor[0],lmin,lmax);
                for(int i=0;i<n;i++)cursor[i]++;res++;maxcursor++;
            }
            else{//invalid cursor
                //printf("inv %d %d %d\n",cursor[0],lmin,lmax);
                int minmaxi=maxi[0][cursor[0]];int ii=0;
                for(int i=1;i<n;i++){
                    if(minmaxi>maxi[i][cursor[i]]){ii=i;minmaxi=maxi[i][cursor[i]]; } 
                }
                cursor[ii]++;maxcursor=max(maxcursor,cursor[ii]); 
            }

            //can we do  a pack with the elements under the cursor ?
            // if no, find min maxi, increase cursor
        }
        printf("Case #%d: %d\n",cas,res);







    }
return 0;
}
