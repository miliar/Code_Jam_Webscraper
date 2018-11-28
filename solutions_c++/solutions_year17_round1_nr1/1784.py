#include <cmath>
#include <queue>
#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
#include <stack>
#include <climits>
#include <assert.h>
#include <set>
#include <queue>
#include <algorithm>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;


typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;
const int N = 100001;
const int MOD = 1e9 + 7;

int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int aaaaaa = 0; aaaaaa < t; aaaaaa++){
        int r,c;
        cin>>r>>c;
        string grid[r];
        for(int i = 0; i < r; i++){
            cin>>grid[i];
        }
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j] != '?'){
                    for(int z = 0; z < c && (grid[i][z] == '?' || grid[i][z] == grid[i][j] || z < j); z++){
                        if(z < j && grid[i][z] == '?'){
                            grid[i][z] = grid[i][j];
                        }
                        else if(z > j && grid[i][z] == '?'){
                            grid[i][z] = grid[i][j];
                        }
                    }
                }
            }
        }
        
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(grid[i][j] != '?'){
                    for(int z = 0; z < r && (grid[z][j] == '?' || grid[z][j] == grid[i][j] || z < i); z++){
                        if(z < i && grid[z][j] == '?'){
                            grid[z][j] = grid[i][j];
                        }
                        else if(z > i && grid[z][j] == '?'){
                            grid[z][j] = grid[i][j];
                        }
                    }
                }
            }
        }
        
        cout<<"Case #"<<aaaaaa+1<<": "<<endl;
        for(int i = 0; i < r;i++){
            cout<<grid[i]<<endl;
        }
        
        
    }
    return 0;
}
