#include <bits/stdc++.h>

using namespace std;

pair<int,int> draw(vector<vector<int> >& grid,
                   pair<int,int> base,
                   pair<int,int> pivot,
                   pair<int,int> nxt){
    int token = grid[pivot.first][pivot.second];
    if(pivot.first<nxt.first){
        for(int row=base.first;row<nxt.first;row++)
        for(int col=base.second;col<grid[row].size();col++)
            grid[row][col] = token;
        return pair<int,int>(pivot.first+1,0);
    } else{
        for(int row=base.first;row<=pivot.first;row++)
        for(int col=base.second;col<nxt.second;col++)
            grid[row][col] = token;
        if(pivot.second>=grid[pivot.first].size()-1)
            return pair<int,int>(pivot.first+1,0);
        return pair<int,int>(base.first,pivot.second+1);

    }

}

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        printf("Case #%d: \n",t);
        int n,m;
        cin>>n>>m;
        getchar();
        vector<vector<int> > grid(n, vector<int>(m));
        vector<pair<int,int> > pos;
        for(int row=0;row<n;row++)
        for(int col=0;col<m;col++){
            int temp=getchar();
            if(temp == '\n'){
                col--;
                continue;
            } if(temp=='?'){
                grid[row][col]=0;
                continue;
            }
            grid[row][col] = temp;
            pos.push_back(pair<int,int>(row,col));
        }
        pos.push_back(pair<int,int>(n,-1));
        pair<int,int> base(0,0);
        for(int cnt=0;cnt<pos.size()-1;cnt++){
            base = draw(grid,base,pos[cnt],pos[cnt+1]);
        }
        for(int row=1;row<n;row++)
        for(int col=0;col<m;col++){
            if(grid[row][col]==0)
                grid[row][col]=grid[row-1][col];
        }
        for(int row=0;row<n;row++){
            for(int col=0;col<m;col++)
                cout<<(char)grid[row][col];
            cout<<"\n";
        }
    }


    return 0;
}
