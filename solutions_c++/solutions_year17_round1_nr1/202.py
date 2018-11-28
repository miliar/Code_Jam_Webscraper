//
//  a.cpp
//
//
//  Created by Lucca Siaudzionis on 2017-04-14.
//
//

#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int cases;
    cin >> cases;
    
    for(int tt = 1;tt <= cases;tt++){
        
        int n, m;
        char mapa[30][30];
        
        memset(mapa, '?', sizeof mapa);
        
        cin >> n >> m;
        for(int i = 1;i <= n;i++)
            for(int j = 1;j <= m;j++)
                cin >> mapa[i][j];
        
        for(int i = 1;i <= n;i++){
            
            bool is = false;
            for(int j = 1;j <= m;j++) if(mapa[i][j] != '?') is = true;
            
            if(!is){
                for(int j = 1;j <= m;j++) mapa[i][j] = mapa[i-1][j];
                continue;
            }
            
            for(int j = 1;j <= m;j++)
                if(mapa[i][j] == '?')
                    mapa[i][j] = mapa[i][j-1];
            
            for(int j = m;j >= 1;j--)
                if(mapa[i][j] == '?')
                    mapa[i][j] = mapa[i][j+1];
            
        }
        
        for(int i = n;i >= 1;i--){
            
            bool is = false;
            for(int j = 1;j <= m;j++) if(mapa[i][j] != '?') is = true;
            
            if(!is){
                for(int j = 1;j <= m;j++) mapa[i][j] = mapa[i+1][j];
                continue;
            }
        }
        
        cout << "Case #" << tt << ":" << endl;
        for(int i = 1;i <= n;i++){
            for(int j = 1;j <= m;j++) cout << mapa[i][j];
            cout << endl;
        }
        
    }
    
    return 0;
}
