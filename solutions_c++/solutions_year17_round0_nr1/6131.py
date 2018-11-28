#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <iomanip>
#include <deque>
#include <stdio.h>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define FILL(Itr,n) fill((Itr).begin(),(Itr).end(),n)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define UNIQUE(Itr) sort((Itr).begin(),(Itr).end()); (Itr).erase(unique((Itr).begin(),(Itr).end()),(Itr).end())
#define LBOUND(Itr,val) lower_bound((Itr).begin(),(Itr).end(),(val))
#define UBOUND(Itr,val) upper_bound((Itr).begin(),(Itr).end(),(val))
#define MOD 1000000007
typedef long long ll;
typedef pair<int,int> P;

bool judge(string s){
    REP(i,s.size()) if(s[i]!='+') return false;
    return true;
}

int main(){
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/Alargein.txt");
    int T; ifs >> T;
    
    REP(kai,T){
        string S;
        int K;
        ifs >> S >> K;
        
        int cnt = 0;
        int N = (int)S.size();
        for(int i = 0; i <= N-K ; i++){
            if(S[i] == '-'){
                cnt++;
                for(int j = i; j < i+K; j++){
                    if(S[j] == '-') S[j] = '+';
                    else S[j] = '-';
                }
            }
        }
        cout << "Case #" << kai+1 << ": ";
        if(judge(S)){
            cout << cnt << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}
