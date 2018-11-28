#include <iostream>
#include <fstream>


using namespace std;

void SplitCake(int R, int C, char data[100][100]){
    // first insert row to full
    bool empty[100];
    for (int r = 0; r < R; ++r){
        int c = 0;
        bool found = false;
        while (c < C){
            if (data[r][c] != '?'){
                found = true;
                for (int t = c - 1; t >= 0 && data[r][t] == '?'; --t){
                    data[r][t] = data[r][c];
                }
                for (c += 1; c < C && data[r][c] == '?'; ++c){
                    data[r][c] = data[r][c-1];
                }
            }else{
                ++c;
            }
        }
        empty[r] = !found;
    }

    // make up rows
    int r = 0;
    while (r < R){
        if (!empty[r]){
            for (int t = r - 1; t >= 0 && empty[t]; --t) {
                for (int c = 0; c < C; ++c) {
                    data[t][c] = data[r][c];
                }
            }
            for (r+= 1; r < R && empty[r]; ++r) {
                for (int c = 0; c < C; ++c) {
                    data[r][c] = data[r-1][c];
                }
            }
        }else{
            ++r;
        }
    }
}

int main() {

    ifstream in_file("data/cake_large.in");
    ofstream out_file("data/cake.out");
    int T = 0;
    in_file >> T;

    char data[100][100];
    for (int t = 0; t < T; ++t){

        // read data
        int R, C;
        in_file >> R >> C;

        for (int r = 0; r < R; ++r){
            for (int c = 0; c < C; ++c){
                in_file >> data[r][c];
            }
        }

        // run
        SplitCake(R, C, data);

        out_file<<"Case #"<<t+1<<":"<<std::endl;

        for (int r = 0; r < R; ++r){
            for (int c = 0; c < C; ++c){
                out_file<<data[r][c];
            }
            out_file<<std::endl;
        }
    }
    return 0;
}