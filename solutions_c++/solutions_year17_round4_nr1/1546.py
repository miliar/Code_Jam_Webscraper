#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<stdlib.h>
#include<iomanip>
using namespace std;
int dp[4][101][101][101];
int trace[4][101][101][101];
int rec(int r,int x,int y,int z,int p){
    if(dp[r][x][y][z]>=0){
        return dp[r][x][y][z];
    }
    else{
        int mx=0;
        if(x>0){
            int tmp = rec((r+1)%p,x-1,y,z,p);
            if( tmp>mx){
                mx=tmp;
                trace[r][x][y][z] = 1;
            }
        }
        if(y>0){
            int tmp = rec((r+2)%p,x,y-1,z,p);
            if( tmp>mx){
                mx=tmp;
                trace[r][x][y][z] = 2;
            }
        }
        if(z>0){
            int tmp = rec((r+3)%p,x,y,z-1,p);
            if( tmp>mx){
                mx=tmp;
                trace[r][x][y][z] = 3;
            }
        }
        if(r==0){
            ++mx;
        }
        dp[r][x][y][z]=mx;
        return mx;
    }
}

int main(){
    int TT;
    cin>>TT;
    int n;
    int p;
    for(int T=1;T<=TT;++T){
        for(int i=0;i<101;++i){
            for(int j=0;j<101;++j){
                for(int k=0;k<101;++k){
                    for(int l=0;l<4;++l){
                        dp[l][i][j][k]=-1;
                    }
                }
            }
        }
        dp[0][0][0][0]=0;
        dp[1][0][0][0]=0;
        dp[2][0][0][0]=0;
        dp[3][0][0][0]=0;
        cin>>n>>p;
        int b[4]={0};

        int a;
        for(int i=0;i<n;++i){
            cin>>a;
            ++b[a%p];
            //v[a%p].push_back(a);
        }
        int count = rec(0,b[1],b[2],b[3],p);
        cout<<"Case #"<<T<<": "<<count+b[0]<<endl;
    }
    return 0;
}




//map<int,int> mp;
//for(int i=0;i<10;++i){
//    mp.insert(make_pair(i,0));
//}
//for(auto it=mp.begin();it!=mp.end();++it){
//    cout<<it->first;
//}
