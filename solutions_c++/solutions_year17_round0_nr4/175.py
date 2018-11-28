#include <iostream>
#include <algorithm>
#include <bitset>
using namespace std;
int tc;
int n,m;
int r,c;
char ch;
bitset<100> orth[100],orth_o[100];
bitset<100> diag[100],diag_o[100];
inline void maximize_orth(){
    // greedy algorithm
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            bool used=false;
            if(!used){
                for(int k=0;k<n;++k){
                    if(orth[i][k]){
                        used=true;
                        break;
                    }
                }
            }
            if(!used){
                for(int k=0;k<n;++k){
                    if(orth[k][j]){
                        used=true;
                        break;
                    }
                }
            }
            if(!used){
                orth[i][j]=true;
            }
        }
    }
}
inline void consider_set_diag(int i,int j){
    bool used=false;
    if(!used){
        for(int k=0;k<n;++k){
            if(i-j+k>=0&&i-j+k<n){
                if(diag[i-j+k][k]){
                    used=true;
                    break;
                }
            }
        }
    }
    if(!used){
        for(int k=0;k<n;++k){
            if(i+j-k>=0&&i+j-k<n){
                if(diag[i+j-k][k]){
                    used=true;
                    break;
                }
            }
        }
    }
    if(!used){
        diag[i][j]=true;
    }
}
inline void maximize_diag(){
    // also a greedy algorithm
    for(int depth=0;depth<(n>>1);++depth){
        // top
        for(int l=depth;l<n-depth-1;++l){
            int i=depth;
            int j=n-1-l;
            consider_set_diag(i,j);
        }
        // left
        for(int l=depth;l<n-depth-1;++l){
            int i=l;
            int j=depth;
            consider_set_diag(i,j);
        }
        // bottom
        for(int l=depth;l<n-depth-1;++l){
            int i=n-1-depth;
            int j=l;
            consider_set_diag(i,j);
        }
        // right
        for(int l=depth;l<n-depth-1;++l){
            int i=n-1-l;
            int j=n-1-depth;
            consider_set_diag(i,j);
        }
    }
    // remember the centre if n is odd!
    if(n&1){
        consider_set_diag(n/2,n/2);
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>n>>m;
        for(int i=0;i<n;++i){
            orth[i].reset();
            orth_o[i].reset();
            diag[i].reset();
            diag_o[i].reset();
        }
        for(int i=0;i<m;++i){
            cin>>ch>>r>>c;
            --r;
            --c;
            if(ch=='x'||ch=='o'){
                orth_o[r][c]=orth[r][c]=true;
            }
            if(ch=='+'||ch=='o'){
                diag_o[r][c]=diag[r][c]=true;
            }
        }
        maximize_orth();
        maximize_diag();
        int y=0,z=0;
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                if(orth_o[i][j]!=orth[i][j]||diag_o[i][j]!=diag[i][j])++z;
                if(orth[i][j])++y;
                if(diag[i][j])++y;
            }
        }
        cout<<"Case #"<<ct<<": "<<y<<" "<<z<<endl;
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                if(orth_o[i][j]!=orth[i][j]||diag_o[i][j]!=diag[i][j]){
                    if(orth[i][j]&&diag[i][j]){
                        cout<<'o';
                    }
                    else if(orth[i][j]){
                        cout<<'x';
                    }
                    else if(diag[i][j]){
                        cout<<'+';
                    }
                    else{
                        cout<<"Horrible error";
                    }
                    cout<<' '<<(i+1)<<' '<<(j+1)<<endl;
                }
            }
        }
    }
}


