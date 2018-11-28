#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("C:\\Users\\lenovo\\Downloads\\A-large (1).in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, R, C, cas=0;
    cin>>T;
    while(T--){
        cin>>R>>C;
        vector<vector<char>> cake(R+1, vector<char>(C+1));
        int last_row=-1;
        for(int i=0; i<R; ++i){
            char last='?';
            for(int j=0; j<C; ++j){
                cin>>cake[i][j];
                if(cake[i][j]!='?'){
                    last=cake[i][j];
                    last_row=i;
                }
            }
            cake[i].back()=last;
        }
        cake.back()=cake[last_row];
        for(int i=0; i<=R; ++i){
            for(int j=0; j<=C; ++j){
                if(cake[i][j]!='?'){
                    char name=cake[i][j];
                    for(int ii=i; ii>=0; --ii){
                        for(int jj=j; jj>=0; --jj){
                            if(cake[ii][jj]=='?'){
                                cake[ii][jj]=name;
                            }
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<++cas<<":"<<endl;
        for(int i=0; i<R; ++i){
            for(int j=0; j<C; ++j){
                cout<<cake[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
