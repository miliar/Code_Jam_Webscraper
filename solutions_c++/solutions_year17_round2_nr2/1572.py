#include<bits/stdc++.h>

using namespace std;

char foo(int n){
    if(n==0){
        return 'R';
    }
    if(n==1){
        return 'O';
    }
    if(n==2){
        return 'Y';
    }
    if(n==3){
        return 'G';
    }
    if(n==4){
        return 'B';
    }
    if(n==5){
        return 'V';
    }
}

int  main(){
    long long int t,k,n,a[10],b[10];
    char ch[1000];

    FILE *fp1,*fp2;

    fp1 = fopen ("input.txt", "r");
    fp2 = fopen ("output.txt", "w");

    fscanf(fp1,"%lld",&t);

    for(k=1;k<=t;k++){
        fscanf(fp1,"%lld",&n);

        for(int i=0;i<6;i++){
            fscanf(fp1,"%lld",&a[i]);
        }

        for(int i=0;i<6;i++){
            b[i] = a[i];
        }

        sort(a,a+6,greater<long long int>());

        if(a[1]+a[2] < a[0]){
            fprintf(fp2,"Case #%lld: IMPOSSIBLE\n",k);
        }
        else{
            printf("%lld %lld %lld",a[0],a[1],a[2]);
            char c1,c2,c3;
            int i=0;
            int o,p;
            int done=0;

            while(b[i]!=a[0]){
                i++;
            }

            c1 = foo(i);
            o=i;

            i=0;
            while(!done){
                if(b[i]==a[1] && i!=o){
                    done = 1;
                }
                if(done==0)
                    i++;
            }


            c2 = foo(i);
            p = i;
            done = 0;

            i=0;
            while(!done){
                if(b[i]==a[2] && i!=o && i!=p){
                    done = 1;
                }
                if(done==0)
                    i++;
            }


            c3 = foo(i);



            string s;

            printf("%c %c %c\n",c1,c2,c3);

            int l = (a[1]+a[2]) - a[0];

            for(int i=0;i<l;i++){
                s += c1;
                s += c2;
                s += c3;
            }

            int count1,count2,count3;

            count1 = a[0] - l;
            count2 = a[1] - l;
            count3 = a[2] - l;

            for(int i=0;i<count2;i++){
                s+=c1;
                s+=c2;
            }

            for(int i=0;i<count3;i++){
                s+=c1;
                s+=c3;
            }


            strcpy(ch, s.c_str());
            fprintf(fp2,"Case #%lld: %s\n",k,ch);
        }



    }

    fclose(fp1);
	fclose(fp2);

    return 0;
}


