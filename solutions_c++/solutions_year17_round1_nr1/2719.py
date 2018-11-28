#include <bits/stdc++.h>
using namespace std;
char grid[30][30];
char newgrid[30][30];

void dedp(int r1,int r2,int c1,int c2) {
    for (int i=r1;i<=r2;i++) {
        for (int j=c1;j<=c2;j++) {
            grid[i][j]=newgrid[i][j];
        }
    }
    return;
}

int dp(int r1,int r2,int c1,int c2) {
    /*for (int i=r1;i<=r2;i++) {
     for (int j=c1;j<=c2;j++) {
     cout<<grid[i][j];
     }
     cout<<endl;
     }*/
    int flag=0;
    int count=0;
    char rem='~';
    for (int i=r1;i<=r2;i++) {
        for (int j=c1;j<=c2;j++) {
            if ((count==0)&&grid[i][j]!='?') {
                count=1;
                rem=grid[i][j];
            }
            else if (grid[i][j]!='?') {
                if (rem!=grid[i][j]) {
                    flag=1;
                    break;
                }
            }
        }
    }
    if ((flag==0)&&(rem!='~')) {
        for (int i=r1;i<=r2;i++) {
            for (int j=c1;j<=c2;j++) {
                grid[i][j]=rem;
            }
        }
        return 1;
    }
    
    for (int i=r1;i<r2;i++) {
        if (dp(r1,i,c1,c2)+dp(i+1,r2,c1,c2)==2)
            return 1;
        else {
            dedp(r1,i,c1,c2);
            dedp(i+1,r2,c1,c2);
        }
    }
    for (int i=c1;i<c2;i++) {
        if (dp(r1,r2,c1,i)+dp(r1,r2,i+1,c2)==2)
            return 1;
        else {
            dedp(r1,r2,c1,i);
            dedp(r1,r2,i+1,c2);
        }
    }
    return 0;
}

int main () {
    int T,R,C;
    cin>>T;
    for (int t=1;t<=T;t++) {
        cin>>R>>C;
        for (int i=0;i<R;i++) {
            for (int j=0;j<C;j++) {
                cin>>grid[i][j];
                newgrid[i][j]=grid[i][j];
            }
        }
        dp(0,R-1,0,C-1);
        printf("Case #%d:\n",t);
        for (int i=0;i<R;i++) {
            for (int j=0;j<C;j++) {
                cout<<grid[i][j];
            }
            cout<<endl;
        }
    }
}
