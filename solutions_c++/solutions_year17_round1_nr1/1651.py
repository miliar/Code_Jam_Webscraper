#include <bits/stdc++.h>
using namespace std;
#define pb push_back

string grid[26];

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {
        int R,C;
        cin>>R>>C;
        for(int i=0;i<R;i++) cin>>grid[i];
        
        vector<char> init;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                if(grid[i][j]!='?')
                    init.pb(grid[i][j]);
        
        for(int let=0;let<(int)init.size();let++) {
            char letter=init[let];
            int posX,posY;
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++)
                    if(grid[i][j]==letter)
                        posX=i,posY=j;
            int curX,curY=posY-1;
            int width=0;
            while(curY>=0 && grid[posX][curY]=='?') {
                grid[posX][curY]=letter;
                width++;
                curY--;
            }
            curY=posY+1;
            while(curY<C && grid[posX][curY]=='?') {
                grid[posX][curY]=letter;
                width++;
                curY++;
            }
            bool f=0;
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++)
                    if(!f && grid[i][j]==letter)
                        f=1,posX=i,posY=j;
            
            curX=posX+1,curY=posY;
            while(curX<R) {
                bool possible=1;
                for(int i=curY;i<=curY+width;i++)
                    if(grid[curX][i]!='?')
                        possible=0;
                if(possible) {
                    for(int i=curY;i<=curY+width;i++)
                        grid[curX][i]=letter;
                    curX++;
                }
                else
                    break;
            }
            curX=posX-1,curY=posY;
            while(curX>=0) {
                bool possible=1;
                for(int i=curY;i<=curY+width;i++)
                    if(grid[curX][i]!='?')
                        possible=0;
                if(possible) {
                    for(int i=curY;i<=curY+width;i++)
                        grid[curX][i]=letter;
                    curX--;
                }
                else
                    break;
            }
        }
        cout<<"Case #"<<t<<":\n";
        for(int i=0;i<R;i++) cout<<grid[i]<<'\n';
    }
    
    return 0;
}







































