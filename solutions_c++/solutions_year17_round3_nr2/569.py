//#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<assert.h>

using namespace std;



ifstream cin("/Users/naginahas/Downloads/B-Large.in");
ofstream cout("/Users/naginahas/Downloads/Bnnnnn.txt");


char dday[720+720]={0};

int dp[720+720+5][720+1500][2][2];


int f(int first, int t, int delta,int prev){
    
    int best = 5000;
    int cand;
    
    if(t == 720+720){
        if(delta!=0) return 5000;
        if(first == prev) return 0;
        else return 1;
    }
    if(dp[t][delta+1500][first][prev]!=-1) return dp[t][delta+1500][first][prev];
    if(dday[t]!='J'){
        int nf = first;
        if(t==0) nf = 1;
        cand = f(nf,t+1,delta+1,1);
        if(prev ==0 && t!=0) cand++;
        best = min(cand,best);
    }
    if(dday[t]!='C'){
        int nf = first;
        if(t==0) nf = 0;
        cand = f(nf,t+1,delta-1,0);
        if(prev==1 && t!=0) cand++;
        best = min(cand,best);
    }
    return dp[t][delta+1500][first][prev]= best;
  
}

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int Ac, Aj;
        cin >> Ac >> Aj;
        for(int i=0;i<720+720+5;i++)
            for(int j=0;j<720+1500;j++)
                for(int k=0;k<2;k++)
                    for(int m=0;m<2;m++)
                        dp[i][j][k][m] = -1;
        for(int k =0;k<720+720;k++) dday[k] = 'N';
        vector <pair <int,int> > vc;
        vector < pair <int,int > > vj;
        for(int j=0;j<Ac;j++){
            pair <int,int> pi;
            cin >> pi.first >> pi.second;
            vc.push_back(pi);
            for(int k=pi.first;k<pi.second;k++)
                dday[k] = 'J';
        }
        for(int j=0;j<Aj;j++){
            pair <int,int> pi;
            cin >> pi.first >> pi.second;
            vj.push_back(pi);
            for(int k=pi.first;k<pi.second;k++)
                dday[k] = 'C';
        }
        int ans = f(0,0,0,0);
        cout << "Case #" << t+1 << ": " << ans << endl;
    }
    return 0;
}

