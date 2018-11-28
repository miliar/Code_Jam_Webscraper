#include<bits/stdc++.h>

using namespace std;

int  main(){
    long long int t,x,d,n,k,s,a1,a2;
    double maxi,j;

    FILE *fp1,*fp2;

    fp1 = fopen ("input.txt", "r");
    fp2 = fopen ("output.txt", "w");

    fscanf(fp1,"%lld",&t);

    for(x=1;x<=t;x++){
        fscanf(fp1,"%lld %lld",&d,&n);

        maxi = 0;
        for(int i=0;i<n;i++){
            fscanf(fp1,"%lld %lld",&k,&s);

            printf("%lld %lld\n",k,s);

            j = (double)(d-k)/s;

            printf("%f\n",j);

            if(maxi < j){
                maxi = j;
                a1 = k;
                a2 = s;
            }
        }

        float ans = (double)(d*a2)/(d-a1);

        fprintf(fp2,"Case #%lld: %.6f\n",x,ans);
    }

    fclose(fp1);
	fclose(fp2);

    return 0;
}
