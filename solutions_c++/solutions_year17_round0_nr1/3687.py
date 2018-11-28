#include<bits/stdc++.h>

using namespace std;

void flip(vector<int>& cake, int k, int left){
    for(int cnt=0;cnt<k;cnt++)
        cake[left+cnt] = !cake[left+cnt];
}

int main(){
    int T;
    cin>>T;
    getchar();
    for(int t=1;t<=T;t++){
        vector<int> cake;
        int k;
        while(1){
            int temp=getchar();
            if(temp == ' ')break;
            if(temp=='+') cake.push_back(1);
            else cake.push_back(0);
        }
        cin>>k;
        getchar();
        bool possible = true;
        int flipCnt = 0;
        for(int cnt=0;cnt<cake.size();cnt++){
            if(cnt<=cake.size()-k && !cake[cnt]){
                flip(cake,k,cnt);
                flipCnt++;
            }
            possible = possible&&cake[cnt];
        }
        printf("Case #%d: ",t);
        if(possible) printf("%d\n",flipCnt);
        else printf("IMPOSSIBLE\n");
    }
}

