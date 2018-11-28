#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

char cake[25][25];

void spreadInRow(int y, int x, int r){
    char tmpC = cake[y][x];
    for(int tmpY =y-1; tmpY >=0;--tmpY){
        if(cake[tmpY][x] ==  '?'){
            cake[tmpY][x] = tmpC;
        }else{
            break;
        }
    }

    for(int tmpY =y+1; tmpY <r;++tmpY){
        if(cake[tmpY][x] ==  '?'){
            cake[tmpY][x] = tmpC;
        }else{
            break;
        }
    }
}

void spreadInCol(int y, int x, int c){
    char tmpC = cake[y][x];
    for(int tmpX = x-1; tmpX>=0; --tmpX){
        if(cake[y][tmpX] == '?'){
            cake[y][tmpX] = tmpC;
        }else{
            break;
        }
    }

    for(int tmpX = x+1; tmpX<c; ++tmpX){
        if(cake[y][tmpX] == '?'){
            cake[y][tmpX] = tmpC;
        }else{
            break;
        }
    }
}

int main() {
    int t;
    cin >> t;

    for(int testID=1; testID <=t; ++testID){
        int r,c;
        cin >> r >> c;

        for(int y=0; y < r ; ++y){
            for(int x=0; x<c; ++x){
                cin  >> cake[y][x];
            }
        }

        for(int y=0; y < r ; ++y){
            for(int x=0; x<c; ++x){
                spreadInRow(y,x,r);
            }
        }


            for(int x=0; x<c; ++x){
                for(int y=0; y < r ; ++y) {
                    spreadInCol(y, x, c);
                }
            }

        cout << "Case #"<< testID << ":"<< endl;
        for(int y=0; y < r ; ++y){
            for(int x=0; x<c; ++x){
                cout  << cake[y][x];
            }

            cout << endl;
        }


    }

    return 0;
}