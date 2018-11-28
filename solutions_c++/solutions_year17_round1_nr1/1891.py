#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);

int main()
{
    ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;

    for(int tc=1;tc<=testCases;tc++) {
        int r,c;
        string board[200];
        cin>>r>>c;
        for(int i=0;i<r;i++) {
            cin>>board[i];
        }


        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(board[i][j] != '?') {
                    //Filling Coulumn Down
                    for(int k=i+1;k<r;k++) {
                        if(board[k][j] == '?') {
                            board[k][j]=board[i][j];
                        } else {
                            break;
                        }
                    }

                    //Filling Coulumn Up
                    for(int k=i-1;k>=0;k--) {
                        if(board[k][j] == '?') {
                            board[k][j]=board[i][j];
                        } else {
                            break;
                        }
                    }


                }
            }
        }
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(board[i][j] != '?') {
                    //Filling Row Right
                    for(int k=j+1;k<c;k++) {
                        if(board[i][k] == '?') {
                            board[i][k]=board[i][j];
                        } else {
                            break;
                        }
                    }

                    //Filling Row Left
                    for(int k=j-1;k>=0;k--) {
                        if(board[i][k] == '?') {
                            board[i][k]=board[i][j];
                        } else {
                            break;
                        }
                    }


                }
            }
        }
        cout<<"Case #"<<tc<<":\n";

        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                cout<<board[i][j];
            }
            cout<<endl;
        }



            

        /*
        if(ok) {
            cout<<"Case #"<<tc<<": "<<res<<"\n";
        } else {
            cout<<"Case #"<<tc<<": "<<"IMPOSSIBLE"<<"\n";
        }*/

    }
    return 0;

}
