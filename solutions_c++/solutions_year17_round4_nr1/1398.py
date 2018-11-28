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
#include <iomanip>
using namespace std;



ifstream cin("/Users/naginahas/Downloads/A-Large.in");
ofstream cout("/Users/naginahas/Downloads/Aqqqqq.txt");

int dp[101][101][101][4];

int f(int a, int b,int c,int rem,int md){
    
    if(a==0 && b==0 && c==0) return 0;
    
    if(dp[a][b][c][rem]!=-1) return dp[a][b][c][rem];
    int cand1=0,cand2=0,cand3 =0;
    int ret =0;
    if(rem==0) ret = 1;
    
    if(a!=0)
        cand1 = f(a-1,b,c,((rem-1)+3*md)%md,md);
    
    if(b!=0)
        cand2 = f(a,b-1,c,((rem-2)+3*md)%md,md);
    
    if(c!=0)
        cand3 = f(a,b,c-1,((rem-3)+3*md)%md,md);
    int cand4 = max(max(cand1,cand2),cand3);
    return dp[a][b][c][rem] = ret + cand4;
    
}

int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int N,P;
        cin >> N >> P;
        vector <int> g;
        int rems[4]={0};
        for(int i=0;i<N;i++){
            int z;
            cin >> z;
            g.push_back(z);
            rems[z%P]++;
        }
        for(int i=0;i<101;i++){
            for(int j=0;j<101;j++){
                for(int k=0;k<101;k++){
                    for(int m=0;m<4;m++){
                        dp[i][j][k][m] = -1;
                    }
                }
            }
        }
        int ans = f(rems[1],rems[2],rems[3],0,P);
        ans += rems[0];
        cout << "Case #" << t+1 << ": "<< ans << endl;
    }
    return 0;
}
