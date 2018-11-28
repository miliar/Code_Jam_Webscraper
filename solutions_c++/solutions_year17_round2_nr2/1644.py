#include<stdio.h>

int main()
{
    FILE *fin,*fout;
    fin = fopen("C:\\Users\\a123\\Desktop\\codejam R2\\input2.txt","r");
    fout = fopen("C:\\Users\\a123\\Desktop\\codejam R2\\output2.txt","w+t");
    int w;
    fscanf(fin,"%d",&w);
    for(int q = 1 ; q <= w ; q++){
        int n;
        fscanf(fin,"%d",&n);
        int col[7];
        for(int i = 1 ; i <= 6 ; i++){
            fscanf(fin,"%d",&col[i]);
        }
        int ans[1010];
        for(int i = 1 ; i <= 1009 ; i++){
            ans[i] = 0;
        }
        if(col[1]<=n/2 && col[3]<=n/2 && col[5]<=n/2){
            int maxi = 0;
            int maxc = 0;
            if(col[1] > maxi){
                maxc = 1;
                maxi = col[1];
            }
            if(col[3] > maxi){
                maxc = 3;
                maxi = col[3];
            }
            if(col[5] > maxi){
                maxc = 5;
                maxi = col[5];
            }
            int cur = 0;
            //printf("%d\n",maxc);
            for(int i = 1 ; ; i+=2){
                ans[i] = maxc;
                //printf("%d %d\n",i,ans[i]);
                col[maxc]--;
                if(col[maxc] == 0){
                    cur = i+2;
                    break;
                }
            }
            if(cur > n){
                cur-=n;
            }
            //printf("%d\n",cur);
            int maxi2 = 0;
            int maxc2 = 0;
            if(col[1] > maxi2 && maxc != 1){
                maxc2 = 1;
                maxi2 = col[1];
            }
            if(col[3] > maxi2 && maxc != 3){
                maxc2 = 3;
                maxi2 = col[3];
            }
            if(col[5] > maxi2 && maxc != 5){
                maxc2 = 5;
                maxi2 = col[5];
            }
            if(maxc2 != 0){
                //printf("%d\n",maxc2);
                for(int i = cur ; ; i+=2){
                    if(i > n){
                        i-=n;
                    }
                    if(ans[i] != 0){
                        i--;
                        continue;
                    }
                    ans[i] = maxc2;
                    //printf("%d %d\n",i,ans[i]);
                    col[maxc2]--;
                    if(col[maxc2] == 0){
                        break;
                    }
                }
            }
            for(int i = 1 ; i <= 5 ; i+=2){
                if(col[i] != 0){
                    for(int j = 1 ; j <= n ; j++){
                        if(ans[j] == 0){
                            ans[j] = i;
                        }
                    }
                    break;
                }
            }
            fprintf(fout,"Case #%d: ",q);
            for(int i = 1 ; i <= n ; i++){
                //printf("%d %d\n",i,ans[i]);
                if(ans[i] == 1){
                    fprintf(fout,"R");
                }
                else if(ans[i] == 3){
                    fprintf(fout,"Y");
                }
                else if(ans[i] == 5){
                    fprintf(fout,"B");
                }
            }
            fprintf(fout,"\n");
        }
        else{
            fprintf(fout,"Case #%d: IMPOSSIBLE\n",q);
        }
    }
}
