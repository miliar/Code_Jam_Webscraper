#include<stdio.h>
#include<algorithm>
using namespace std;
struct cart{
    int n;
    int s;
    int e;
};
int abso(int );
int main()
{
    FILE *fin,*fout;
    fin=fopen("C:\\Users\\a123\\Desktop\\1C\\input1.txt","r");
    fout=fopen("C:\\Users\\a123\\Desktop\\1C\\output1.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int atot,btot;
        cart a[210];
        fscanf(fin,"%d%d",&atot,&btot);
        int tot = atot+btot;
        int t1 = 720;
        int t2 = 720;
        if(atot > 0){
            for(int i = 1 ; i <= atot ; i++){
                fscanf(fin,"%d%d",&a[i].s,&a[i].e);
                t1 = t1-a[i].e+a[i].s;
                a[i].n = 1;
            }
        }
        if(btot > 0){
            for(int i = atot+1 ; i <= tot ; i++){
                fscanf(fin,"%d%d",&a[i].s,&a[i].e);
                t2 = t2-a[i].e+a[i].s;
                a[i].n = -1;
            }
        }
        for(int i = 1 ; i <= tot-1 ; i++){
            for(int j = i+1 ; j <= tot ; j++){
                if(a[i].e  > a[j].e){
                    cart temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
        int sp1[210];
        int sp2[210];
        int cur1 = 1;
        for(int i = 1 ; i <= tot-1 ; i++){
            if(a[i].n > 0 && a[i+1].n > 0){
                sp1[cur1] = a[i+1].s-a[i].e;
                cur1++;
            }
        }
        if(a[1].n>0 && a[tot].n>0){
            sp1[cur1] = a[1].s+1440-a[tot].e;
            cur1++;
        }
        cur1--;
        //printf("2:%d\n",cur1);
        //printf("1\n");
        sort(sp1+1,sp1+cur1+1);
        int cur2 = 1;
        for(int i = 1 ; i <= tot-1 ; i++){
            if(a[i].n < 0 && a[i+1].n < 0){
                sp2[cur2] = a[i+1].s-a[i].e;
                cur2++;
            }
        }
        if(a[1].n<0 && a[tot].n<0){
            sp2[cur2] = a[1].s+1440-a[tot].e;
            cur2++;
        }
        cur2--;
        sort(sp2+1,sp2+cur2+1);
        int totsp = 0;
        //printf("3:%d\n",t1);
        //printf("4:%d\n",sp1[1]);
        for(int i = 1 ; i <= cur1 ; i++){
            t1-=sp1[i];
            if(t1 < 0){
                totsp += (cur1-i+1)*2;
                break;
            }
        }
        for(int i = 1 ; i <= cur2 ; i++){
            t2-=sp2[i];
            if(t2 < 0){
                totsp += (cur2-i+1)*2;
                break;
            }
        }
        printf("%d\n",totsp);
        for(int i = 1 ; i <= tot-1 ; i++){
            //printf("1\n");
            if((a[i].n)*(a[i+1].n) < 0){
                totsp++;
            }
        }
        if((a[1].n)*(a[tot].n) < 0){
            totsp++;
        }
        fprintf(fout,"Case #%d: %d\n",q,totsp);
    }
}

int abso(int number)
{
    if(number > 0) return number;
    return -number;
}
