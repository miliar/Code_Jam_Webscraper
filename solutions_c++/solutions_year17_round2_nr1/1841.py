#include<stdio.h>

int main()
{
    FILE *fin,*fout;
    fin = fopen("C:\\Users\\a123\\Desktop\\codejam R2\\input1.txt","r");
    fout = fopen("C:\\Users\\a123\\Desktop\\codejam R2\\output1.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        double dis;
        int n;
        double init[1050],maxs[1050];
        fscanf(fin,"%lf",&dis);
        fscanf(fin,"%d",&n);
        double maxi = 0;
        for(int i = 1 ; i <= n ; i++){
            fscanf(fin,"%lf%lf",&init[i],&maxs[i]);
            double temp = (dis - init[i])/maxs[i];
            if(temp > maxi){
                maxi = temp;
            }
        }
        double ans = dis/maxi;
        fprintf(fout,"Case #%d: %lf\n",q,ans);
    }
}
