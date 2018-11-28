#include <bits/stdc++.h>
using namespace std;
int T;
int cas;

const int N=30;

char s[N][N];


bool used[N][N];

int main(){
    for(cin>>T; T--; ){
        printf("Case #%d:\n", ++cas);
        ///////////////////////////////////////
        memset(used, 0, sizeof(used));
        int r, c;
        cin >> r >> c;
        for(int i=0; i<r; i++)
            cin >> s[i];

        for(int i=0; i<r; i++)
            for(int j=0; j<c; j++)
                if(isalpha(s[i][j]) && !used[i][j]){

                    used[i][j]=true;
                    char cur=s[i][j];

                    // cout << i<< ' '<< j<< endl;
                    int t=i, b=i, l=j, r=j;

                    for(int x=i-1; x>=0; x--){
                        if(s[x][j]=='?')
                            t=x;
                        else break;
                    }

                    for(int y=j-1; y>=0; y--)
                        if(s[i][y]=='?')
                            l=y;
                        else break;

                    for(int y=j+1; y<c; y++){

                        if(s[i][y]=='?'){
                            r=y;
                        }
                        else break;

                    }

                    // cout << t <<' '<<b << ' '<<l << ' '<< r<< endl;
                    for(int i=t; i<=b; i++)
                        for(int j=l; j<=r; j++)
                            s[i][j]=cur, used[i][j]=true;


                }

        for(int i=1; i<r; i++)
            if(s[i][0]=='?')
                for(int j=0; j<c; j++)
                    s[i][j]=s[i-1][j];

        for(int i=0; i<r; i++)
            puts(s[i]);

////////////////////////////////////////////////////////
    }
    return 0;

}