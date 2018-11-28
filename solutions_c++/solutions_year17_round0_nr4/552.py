#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>

using namespace std;


struct point {
    int x;
    int y;
    char type;
};

void printbd(auto board){
   for(c : board){
        for(d:c){
            cout << d;
        } 
        cout << endl;
   }
}
int main(){

    int ncases;

    cin >> ncases;


    for(int i = 0; i < ncases;i++) {
        int n;
        int m;
        cin >> n;
        cin >> m;
        set<int> seenc;
        set<int> seenr;
        set<int> seendp;
        set<int> seendm;
        vector<point> ans;
        vector<vector<char>> board;
        vector<char> tmp(n, '.');
        for(int a = 0; a < n; a++){
            board.push_back(tmp);
        }
        for(int j = 0; j < m; j++) {
           point tmp;
           cin >> tmp.type;
           cin >> tmp.x;
           cin >> tmp.y;
           tmp.x--;
           tmp.y--;
           board[tmp.x][tmp.y] = tmp.type;
           if(tmp.type != 'x'){
                seendp.insert(tmp.x + tmp.y);
                seendm.insert(tmp.x - tmp.y);
           }
           if(tmp.type != '+'){
                seenc.insert(tmp.x);
                seenr.insert(tmp.y);
           }
        }
        auto boardcp = board;
        for(int i =0 ; i < n; i++){
           if(seendp.find(i) == seendp.end() && seendm.find(i) == seendm.end() && board[i][0] == '.'){
             board[i][0] = '+';
             seendp.insert(i);
             seendm.insert(i);
           }
           if(seendm.find(i - n + 1) == seendm.end() && seendp.find(i + n - 1) == seendp.end() && board[i][n - 1] == '.'){
             board[i][n - 1] = '+';
             seendm.insert(i - n + 1);
             seendp.insert(i + n - 1);
           }
           if(seendp.find(n - 1 + i) == seendp.end() && seendm.find(n - 1 - i) == seendm.end() && board[n -1][i] == '.'){
             board[n - 1][i] = '+';
             seendm.insert(n - 1 - i);
             seendp.insert(n - 1 + i);
           }
           if(seendp.find(i) == seendp.end() && seendm.find(-i) == seendm.end() && board[0][i] == '.'){
             board[0][i] = '+';
             seendp.insert(i);
             seendm.insert(-i);
           }
        }
        for(int i =0 ; i < n; i++){
            bool enc =  false;
            if(seenc.find(i) == seenc.end()){
                for(int j =0 ; j < n; j++){
                    if(seenr.find(j) == seenr.end() && board[i][j] == '.'){
                        board[i][j] = 'x';
                        seenc.insert(i);
                        seenr.insert(j);
                        enc = true;
                        break;
                    }

                }
                if(enc == false){
                    for(int j =0 ; j < n; j++){
                        if(seenr.find(j) == seenr.end()){
                            board[i][j] = 'o';
                            seenc.insert(i);
                            seenr.insert(j);
                            break;
                        }
                    }
                }
            }
        }

        if(n == 1){
            board[0][0] = 'o';
        }
        int score = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 'x' || board[i][j] == '+'){
                    score ++;
                    if(board[i][j] != boardcp[i][j]){
                        ans.push_back({i+1,j+1,board[i][j]});
                    }
                }
                if(board[i][j] == 'o'){
                    if(board[i][j] != boardcp[i][j]){
                        ans.push_back({i+1,j+1,board[i][j]});
                    }
                    score += 2;
                }
            }
        
        }

        cout << "Case #" << i + 1 << ": " << score << " " << ans.size() << endl;
        for(a : ans){
            cout << a.type << " " << a.x << " " << a.y << endl;
        }
        cout << endl;
    }
}
