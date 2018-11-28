#include<iostream>
#include <limits>
#include <algorithm>
#include<vector>
#include<iomanip>
#include<string>
#include<unordered_map>
#include<stack>
#include <queue>
#include <deque>
#include <chrono>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <random>
#define forn(i,n) for(int i=0;i<n;++i)
#define mp std::make_pair
#define pii std::pair<int, int>
#define pll std::pair<long long, long long>
using std::cin;
using std::cout;


void draw(std::vector<std::vector<char> >& cake, pii point){
        int x=point.first;
        int y=point.second;
        for(int j=0;j<cake[0].size();j++){
            if(cake[x][j]=='?'){
                cake[x][j]=cake[x][y];
            }else{
                if(j>y)
                    break;
            }
        }
}
void copy_line(std::vector<std::vector<char> >& cake, int i, int ii){
    for(int j=0;j<cake[i].size();j++){
        cake[i][j]=cake[ii][j];
    }
}
int main(){
    //freopen("A.in", "rt", stdin);
    int T;
    int R,C;
    cin>>T;
    forn(k,T){
        cin>>R>>C;
        std::vector<std::vector<char> > cake(R,std::vector<char> (C));
        std::vector<pii> letter;
        std::vector<bool> empty_line(R);
        forn(i,R){
            int c=0;
            forn(j,C){
                cin>>cake[i][j];
                if(cake[i][j]!='?'){
                    c++;
                    letter.push_back(mp(i,j));
                }
            }
            if(c==0){
                empty_line[i]=true;
            }else{
                 empty_line[i]=false;
            }
        }
        for(int i=0;i<letter.size();i++){
            draw(cake,letter[i]);
        }
        for(int i=0;i<empty_line.size();i++){
            if(empty_line[i]){
                if(i!=0){
                    copy_line(cake,i,i-1);
                }else{
                    int ii=i+1;
                    while(empty_line[ii] && ii<R)ii++;
                    copy_line(cake,i,ii);

                }
            }
        }
        cout<<"Case #"<<k+1<<":\n";
        forn(i,R){
            forn(j,C){
                cout<<cake[i][j];
            }
            cout<<"\n";
        }

    }

return 0;
}
