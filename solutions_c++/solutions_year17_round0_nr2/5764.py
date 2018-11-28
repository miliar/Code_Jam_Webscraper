#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int t, digs[20];
long long n;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int o=1; o<=t; o++) {
        scanf("%lld",&n);
        int nds = 0;
        while(n > 0) {
            digs[nds++] = n%10;
            n/=10;
        }
        for(int i=nds-2; i>=0; i--) {
            if(digs[i]<digs[i+1]) {
                digs[i+1]--;
                int k=i+1;
                while(k<=nds-2&&digs[k]<digs[k+1]) {
                    digs[k+1]--;
                    k++;
                }
                for(int j=k-1; j>=0; j--)
                    digs[j] = 9;
                break;
            }
        }
        if(digs[nds-1] == 0) nds--;
        printf("Case #%d: ", o);
        for(int i=nds-1; i>=0; i--) {
            printf("%d",digs[i]);
        }
        printf("\n");
    }
    return 0;
}
