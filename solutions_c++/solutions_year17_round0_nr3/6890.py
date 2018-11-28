#include<vector>
#include<algorithm>
#include<iostream>
#include<string>
#include<cstdlib>

using namespace std;

int findBestStall(int *stalls, int *separationL, int *separationR, unsigned long long N, int *bestMinSeparation, int *bestMaxSeparation) {
    for(int i=1;i<=N;i++) {
        int count = 0;
        while(stalls[i-count] == 0)
            count++;
        separationL[i] = --count;
        count = 0;
        while(stalls[i+count] == 0)
            count++;
        separationR[i] = --count;
        //cout<<"SepLR at pos"<<i<<" "<<separationL[i]<<" "<<separationR[i]<<endl;
        //cout<<"Stall at pos"<<i<<" "<<stalls[i]<<endl;
    }
    long long bestMin = -1, bestPos = 0, bestMax = -1;
    for(int i=N;i>=1;i--) {
        int tmp = min(separationL[i],separationR[i]);
        int tmpMax = max(separationL[i],separationR[i]);
        if(bestMin < tmp) {
            bestMin = tmp;
            bestMax = tmpMax;
            bestPos = i;
            //cout<<bestPos;
        } else if(bestMin == tmp && bestMax <= tmpMax) {
            bestMin = tmp;
            bestMax = tmpMax;
            bestPos = i;
            //cout<<bestPos;
        }
    }
    *bestMinSeparation = bestMin;
    *bestMaxSeparation = bestMax;
    return bestPos;
}

int main() {
    int tc;
    cin>>tc;
    for(int z=1;z<=tc;z++) {
        unsigned long long N, K;
        cin >> N >> K;
        int stalls[N+2] = {0};
        stalls[0] = 1;
        stalls[N+1] = 1;
        int separationL[N+1] = {-10};
        int separationR[N+1] = {-10};
        int bestMinSeparation = -10;
        int bestMaxSeparation = -10;
        for(int i=0;i<K;i++) {
            stalls[findBestStall(stalls, separationL, separationR, N, &bestMinSeparation, &bestMaxSeparation)] = true;
        }
        //if(log2(N) > K)
        cout<<"Case #"<<z<<": "<<bestMaxSeparation<<" "<<bestMinSeparation<<endl;
    }
    return 0;
}
