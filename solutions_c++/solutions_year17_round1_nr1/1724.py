#include <bits/stdc++.h>
using namespace std;

char grid[100][100];

int main(){
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc,i,j,k,R,C;
    string str;
    cin>>tc;
    for(int tc1=1;tc1<=tc;tc1++){
        cin>>R>>C;
        for(i=0;i<R;i++){
            cin>>str;
            for(j=0;j<C;j++)
                grid[i][j] = str[j];
        }
        for(i=0;i<R;i++){
            for(j=0;j<C;j++)
                if(grid[i][j]!='?')
                    break;
            if(j==C) continue;
            for(k=0;k<j;k++) grid[i][k]=grid[i][j];
            char last = grid[i][j];
            j++;
            while(j<C){
                if(grid[i][j]=='?')
                    grid[i][j] = last;
                else last = grid[i][j];
                j++;
            }
        }
        for(j=0;j<C;j++){
            for(i=0;i<R;i++)
                if(grid[i][j]!='?')
                    break;
            if(i==R) continue;
            for(k=0;k<i;k++) grid[k][j] = grid[i][j];
            char last = grid[i][j];
            i++;
            while(i<R){
                if(grid[i][j]=='?')
                    grid[i][j] = last;
                else last = grid[i][j];
                i++;
            }
        }
        cout<<"Case #"<<tc1<<":\n";
        for(i=0;i<R;i++){
            for(j=0;j<C;j++)
                cout<<grid[i][j];
            cout<<"\n";
        }
    }
    return 0;
}
