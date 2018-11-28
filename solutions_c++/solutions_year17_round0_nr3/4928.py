#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<iostream>
#include<string>
#include<queue>
#define ll long long
#define fi first
#define se second
using namespace std;
        int kolik[1000001];
int main(void){
    freopen("C-small-2-attempt4.in","r",stdin);
    freopen("C-small-2.out", "w", stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        int N; int K;
        scanf("%i %i", &N, &K);

        kolik[N]=1;
        int i;
        for(i=0;i<N;i++) kolik[i]=0;
        int x;
        int j=N;
        for(i=0;i<K;i++){
            while(kolik[j]==0) j--;
            kolik[j]--;
            kolik[j/2]++;
            kolik[(j-1)/2]++;
        }
        printf("Case #%i: %i %i\n", l+1, j/2, (j-1)/2);
    }
    return 0;
}


