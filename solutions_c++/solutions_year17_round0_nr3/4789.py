#include <bits/stdc++.h>

using namespace std;

int main (){
    int T;
    scanf("%d" ,&T);
    for (int t=1;t<=T;t++){
        long long n,k,odp1, odp2;
        scanf("%lld %lld", &n, &k);
        long long a = 0;
        long long b = n-k;
        while((1<<a)<=k)a++;
        a = 1<<a;
        /*if(b%a==0){
            long long x = b/a;
            odp1 = x/2;
            odp2 = x/2;
            if(x%2==1)odp1++;
            printf("fff");
        }else{*/
            long long d = n - a/2 + 1;
            //printf("%lld\n\n", t);
            long long xs = d/(a/2);
            long long xb = xs+1;
            long long nb = d%(a/2);
            long long ns = (a/2)-nb;
            //printf("small ones %lld of %lld and big ones %lld of %lld\n", ns,xs,nb,xb);
            /*long long pairs = min(nb,ns);
            long long biggers = (nb-pairs)/2;
            long long smallers = (ns-pairs)/2;
            printf("pairs: %lld, biggers: %lld, smallers: %lld\n",pairs, biggers, smallers );*/
            long long left = k-a/2+1;
            //printf("left to go: %lld\n", left);
            if(left<=nb){
                xb--;
                odp1=xb/2;
                odp2=odp1;
                if(xb%2==1){
                    odp1++;
                }
                //printf("b");
            }else{
                xs--;
                odp1=xs/2;
                odp2=odp1;
                if(xs%2==1){
                    odp1++;
                }
                //printf("s");
            }
        //}
        printf("Case #%d: %d %d\n", t, odp1, odp2);
    }

    return 0;
}