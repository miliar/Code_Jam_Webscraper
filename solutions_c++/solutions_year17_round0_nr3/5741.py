#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>

typedef struct {
    long long int index;
    long long int minLSRS; 
    long long int maxLSRS; 
} results;

using namespace std;

int main() {

    int T;

    long long int N, K;
    long long int ls,rs,st,stindex;
    long long int final_minlsrs,final_maxlsrs,final_index;

    char Stall[1000005];
    results Stall_stats[1000005];
    int results_count;
    //long long int minLSRS[1000005];
    //long long int maxLSRS[1000005];

    scanf("%d", &T);
    //printf("%d\n",T);

    for (int i=1;i<=T;i++) {
        scanf("%lld %lld", &N, &K);

        memset(Stall, '0', N+2);

        //char Stall[] = new char[N+2];
        Stall[0] = '1';
        Stall[N+1] = '1';

        //long long int minLSRS[]

        //printf("%lld %lld\n", N, K);
        for (int j=0; j<K; j++) {
            //For each empty stall
            Stall_stats[0].minLSRS=-1;
            Stall_stats[0].maxLSRS=-1;
            results_count=0;

            for (st=1;st<=N;st++) {
                if (Stall[st]=='0') {
                   //Compute LS
                   for (stindex=st-1;Stall[stindex]=='0' && stindex>=0;stindex--) {

                   }
                   ls=st-stindex;
                   for (stindex=st+1;Stall[stindex]=='0' && stindex<=N+1;stindex++) {

                   }
                   rs=stindex-st;
                   long long locallsrsmin=std::min(ls,rs);
                   if (locallsrsmin > Stall_stats[0].minLSRS) {
                       Stall_stats[0].minLSRS=locallsrsmin;
                       Stall_stats[0].maxLSRS=std::max(ls,rs);
                       Stall_stats[0].index = st;
                       results_count = 1;
                   } else {
                       if (locallsrsmin == Stall_stats[0].minLSRS) {
                           Stall_stats[results_count].minLSRS=locallsrsmin;
                           Stall_stats[results_count].maxLSRS=std::max(ls,rs);
                           Stall_stats[results_count].index = st;
                           results_count++; 
                       }
                   }
                }
            }
            //All empty stalls checked 
            final_minlsrs = Stall_stats[results_count-1].minLSRS;
            final_maxlsrs = Stall_stats[results_count-1].maxLSRS;
            final_index = Stall_stats[results_count-1].index;
            for (int loop_results=results_count-2;loop_results>=0; loop_results--) {
                if (Stall_stats[loop_results].maxLSRS >= final_maxlsrs) {
                    final_minlsrs = Stall_stats[loop_results].minLSRS;
                    final_maxlsrs = Stall_stats[loop_results].maxLSRS;
                    final_index = Stall_stats[loop_results].index;
                }
            }
            Stall[final_index]='1';
        }
        printf("Case #%d: %lld %lld\n", i, final_maxlsrs-1, final_minlsrs-1);
    }

}
