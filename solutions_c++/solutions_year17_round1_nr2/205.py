//
//  b.cpp
//
//
//  Created by Lucca Siaudzionis on 2017-04-14.
//
//

#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long lli;
typedef pair<int, int> pii;

//------------------------
#define MAXN 55
#define ff  first
#define ss second

int n, p;
lli r[MAXN];
lli q[MAXN][MAXN];

int ind[MAXN];
vector<int> event;
vector<pii> inter[MAXN];
//------------------------



int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int cases;
    cin >> cases;
    
    for(int tt = 1;tt <= cases;tt++){
        
        cin >> n >> p;
        for(int i = 1;i <= n;i++)
            cin >> r[i];
        
        event.clear();
        for(int i = 1;i <= n;i++){
            ind[i] = 0;
            inter[i].clear();
        }
        
        for(int i = 1;i <= n;i++){
            for(int j = 1;j <= p;j++){
                cin >> q[i][j];
                
                lli cur = lli(ceil(double(q[i][j])/(r[i]*1.1)));
                
                //cout << cur << endl;
                
                while( (cur-1)*r[i]*11 >= q[i][j]*10 ) cur--;
                while( cur*r[i]*11 < q[i][j]*10 ) cur++;
                
                //cout << cur << endl;
                
                int ini = int(cur);
                
                cur = lli(ceil(double(q[i][j])/(r[i]*0.9)));
                while( (cur+1)*r[i]*9 <= q[i][j]*10 ) cur++;
                while( cur*r[i]*9 > q[i][j]*10 ) cur--;
                
                int fim = int(cur);
                
                //cout << ini << " " << fim << endl;
                
                if(ini <= fim){
                    event.push_back(ini);
                    inter[i].push_back(pii(ini, fim));
                }
            }
        }
        
        for(int i = 1;i <= n;i++) sort(inter[i].begin(), inter[i].end());
        
        /*for(int i = 1;i <= n;i++){
            for(auto pp : inter[i]) cout << "(" << pp.ff << ", " << pp.ss << ") ";
            cout << endl;
        }*/
        
        sort(event.begin(), event.end());
        
        int answer = 0;
        for(auto e : event){
            
            bool shit = false;
            bool megashit = false;
            
            for(int i = 1;i <= n;i++){
                
                while(ind[i] < (int)inter[i].size() && inter[i][ind[i]].ss < e)
                    ind[i]++;
                
                if(ind[i] == (int)inter[i].size()){
                    shit = true;
                    megashit = true;
                    break;
                }
                
                if(inter[i][ind[i]].ff > e){
                    shit = true;
                    break;
                }
            }
            
            //cout << e << " " << shit << endl;
            
            if(megashit) break;
            if(shit) continue;
            
            answer++;
            for(int i = 1;i <= n;i++) ind[i]++;
        }
        
        cout << "Case #" << tt << ": " << answer << endl;
    }
    
    return 0;
}
