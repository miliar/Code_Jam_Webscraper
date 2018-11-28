#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int T,t;
    cin>>T;
    for (t=0; t<T; t++) {
        int R,C;
        cin>>R>>C;
        string s;
        vector<string> vs;
        for (int i=0; i<R; i++) {
            cin>>s;
            vs.push_back(s);
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (vs[i][j]!='?') {
                    for (int k=j+1; k<C; k++) {
                        if (vs[i][k] =='?') {
                            vs[i][k] = vs[i][j];
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (vs[i][j]!='?') {
                    for (int k=j-1; k>=0; k--) {
                        if (vs[i][k] =='?') {
                            vs[i][k] = vs[i][j];
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (vs[i][j]!='?') {
                    for (int k=i-1; k>=0; k--) {
                        if (vs[k][j] =='?') {
                            vs[k][j] = vs[i][j];
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (vs[i][j]!='?') {
                    for (int k=j-1; k>=0; k--) {
                        if (vs[i][k] =='?') {
                            vs[i][k] = vs[i][j];
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        for (int i=1; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (vs[i][j]=='?') {
                    vs[i][j] = vs[i-1][j];
                }
            }
        }
        
        cout <<"Case #"<<t+1<<": " <<endl;
        for (int i=0; i<R; i++) {
            cout<<vs[i]<<endl;
        }
    }
    return 0;
}