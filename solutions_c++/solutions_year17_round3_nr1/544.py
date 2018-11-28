#include<stdio.h>
#include<algorithm>
using namespace std;

struct cart{
    double r;
    double h;
    double up;
    double sd;
    double num;
};
int main()
{
    FILE *fin,*fout;
    fin=fopen("C:\\Users\\a123\\Desktop\\1C\\input2.txt","r");
    fout=fopen("C:\\Users\\a123\\Desktop\\1C\\output2.txt","w+t");
    int w;
    double pi = 3.1415926535;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int n,k;
        fscanf(fin,"%d%d",&n,&k);
        cart pan[1010];
        for(int i = 1 ; i <= n ; i++){
            fscanf(fin,"%lf%lf",&pan[i].r,&pan[i].h);
            pan[i].num = i;
            pan[i].up = pi*pan[i].r*pan[i].r;
            pan[i].sd = 2*pi*pan[i].r*pan[i].h;
        }
        for(int i = 1 ; i <= n-1 ; i++){
            for(int j = i+1 ; j <= n ; j++){
                if(pan[j].sd > pan[i].sd){
                    cart temp = pan[i];
                    pan[i] = pan[j];
                    pan[j] = temp;
                }
            }
        }
        double maxr = 0;
        double tot = 0;
        for(int i = 1 ; i <= k-1 ; i++){
            tot = tot+pan[i].sd;
            if(pan[i].r > maxr){
                maxr = pan[i].r;
            }
        }
        double maxp = 0;
        for(int i = k ; i <= n ; i++){
            if(pan[i].r < maxr){
                double temp = pi*maxr*maxr+pan[i].sd;
                if(temp > maxp) maxp = temp;

            }
            else{
                double temp = pi*pan[i].r*pan[i].r+pan[i].sd;
                if(temp > maxp) maxp = temp;
            }
        }
        tot+=maxp;
        fprintf(fout,"Case #%d: %.9lf\n",q,tot);
    }
}

