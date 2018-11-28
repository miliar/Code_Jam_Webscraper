#include <bits/stdc++.h>
using namespace std;

struct Pancake {
    int r,h;
};

long long height(Pancake a) {
    return (long long)a.h * 2 * (long long)a.r;
}

int T;

int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        int N,K;
        scanf("%d%d",&N,&K);
        Pancake pancakes[N];
        int indexes[N];
        for(int i=0;i<N;i++) scanf("%d%d",&pancakes[i].r,&pancakes[i].h),indexes[i]=i;
        long long maxi=0;
        do {
            long long total=0;
            int bestRadius=0;
            for(int i=0;i<K;i++) {
                bestRadius=max(bestRadius,pancakes[indexes[i]].r);
                total+=height(pancakes[indexes[i]]);
            }
            total+=(((long long)bestRadius)*((long long)bestRadius));
            if(maxi<total) maxi=total;
        } while(next_permutation(indexes,indexes+N));
        cout.precision(9);
        cout<<"Case #"<<t<<": "<<fixed<<((double)maxi)*atan(1.0)*4<<endl;
    }
    
    return 0;
}
