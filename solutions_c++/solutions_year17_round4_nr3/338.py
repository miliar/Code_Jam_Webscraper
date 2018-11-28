#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cassert>
#define RIGHT 0
#define DOWN 1
#define LEFT 2
#define UP 3
using namespace std;
int tc;
int n,p,r,c;
char house[50][50];
int dj[]={1,0,-1,0},di[]={0,1,0,-1};
int proper(int i,int j){
    return i*c+j;
}
int reflect(int dir,char t){
    if(t=='/'){
        switch(dir){
        case RIGHT:
            return UP;
        case DOWN:
            return LEFT;
        case LEFT:
            return DOWN;
        case UP:
            return RIGHT;
        }
    }
    else{ // '\'
        switch(dir){
        case RIGHT:
            return DOWN;
        case DOWN:
            return RIGHT;
        case LEFT:
            return UP;
        case UP:
            return LEFT;
        }
    }
    assert(false);
}
bool get_cells(int i,int j,int direction,set<int>& out){
    if(i<0||j<0||i>=r||j>=c)return false;
    if(house[i][j]=='.'){
        out.insert(proper(i,j));
        return get_cells(i+di[direction],j+dj[direction],direction,out);
    }
    else if(house[i][j]=='-'||house[i][j]=='|')return true;
    else if(house[i][j]=='#')return false;
    else if(house[i][j]=='/'){
        int newdir=reflect(direction,'/');
        return get_cells(i+di[newdir],j+dj[newdir],newdir,out);
    }
    else{
        int newdir=reflect(direction,'\\');
        return get_cells(i+di[newdir],j+dj[newdir],newdir,out);
    }
}
int main(){
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>r>>c;
        vector<vector<set<int>>>shooters;
        vector<pair<int,int>>sloc;
        map<int,set<int>>cells;
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                cin>>house[i][j];
                if(house[i][j]=='.'){
                    cells.emplace(proper(i,j),set<int>{});
                }
            }
        }
        bool impossible=false;
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                if(house[i][j]=='-'||house[i][j]=='|'){
                    vector<set<int>> ret;
                    set<int> acc1;
                    bool c1,c2;
                    c1=get_cells(i,j-1,LEFT,acc1);
                    c2=get_cells(i,j+1,RIGHT,acc1);
                    if(!(c1||c2)){
                        for(const int& x:acc1){
                            cells[x].emplace(shooters.size());
                        }
                        ret.emplace_back(move(acc1));
                        house[i][j]='-';
                    }
                    set<int> acc2;
                    c1=get_cells(i-1,j,UP,acc2);
                    c2=get_cells(i+1,j,DOWN,acc2);

                    if(!(c1||c2)){
                        for(const int& x:acc2){
                            cells[x].emplace(shooters.size());
                        }
                        ret.emplace_back(move(acc2));
                        house[i][j]='|';
                    }
                    if(ret.empty())impossible=true;
                    shooters.emplace_back(move(ret));
                    sloc.emplace_back(i,j);
                }
            }
        }
        if(impossible){
            cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
            continue;
        }
        for(const pair<int,set<int>>& cell:cells){
            if(cell.second.empty())impossible=true;
        }
        if(impossible){
            cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
            continue;
        }
        while(true){
            while(true){
                bool havestuff=false;
                for(map<int,set<int>>::iterator it=cells.begin();it!=cells.end();){
                    pair<const int,set<int>>& cell=*it;
                    if(cell.second.size()==1){
                        havestuff=true;
                        int shooterid=*(cell.second.begin());
                        vector<set<int>>& shooter=shooters[shooterid];
                        if(shooter.size()==2){
                            bool has1=(shooter[0].find(cell.first)!=shooter[0].end());
                            bool has2=(shooter[1].find(cell.first)!=shooter[1].end());
                            if(has1&&!has2){
                                for(const int& x:shooter[1]){
                                    cells[x].erase(shooterid);
                                }
                                house[sloc[shooterid].first][sloc[shooterid].second]='-';
                                shooter.erase(shooter.begin()+1);
                            }
                            else if(has2&&!has1){
                                for(const int& x:shooter[0]){
                                    cells[x].erase(shooterid);
                                }
                                shooter.erase(shooter.begin());
                            }
                        }
                        cells.erase(it++);
                    }
                    else{
                        ++it;
                    }
                }
                if(!havestuff)break;
            }
            for(const pair<int,set<int>>& cell:cells){
                if(cell.second.empty())impossible=true;
            }
            if(impossible)break;
            int ii;
            for(ii=0;ii<shooters.size();++ii){
                vector<set<int>>& shooter=shooters[ii];
                if(shooter.size()==2){
                    for(const int& x:shooter[1]){
                        cells[x].erase(ii);
                    }
                    house[sloc[ii].first][sloc[ii].second]='-';
                    shooter.pop_back();
                    break;
                }
            }
            for(const pair<int,set<int>>& cell:cells){
                if(cell.second.empty())impossible=true;
            }
            if(impossible)break;
            if(ii>=shooters.size())break;
        }
        if(impossible){
            cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<"Case #"<<ct<<": POSSIBLE"<<endl;
        for(int i=0;i<r;++i){
            for(int j=0;j<c;++j){
                cout<<house[i][j];
            }
            cout<<endl;
        }

    }
}

