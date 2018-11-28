#include <fstream>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

char v[30][30];
bool b[300];
int t, T, R, C, gol[30];

void init(){
    for(int i = 0; i < 30; i++){
        for(int j = 0; j < 30; j++){
            v[i][j] = '#';
        }
    }
    for(int i = 0; i < 255; i++){
        b[i] = 0;
    }
}

int main(){
    cin >> T;
    for(int t = 1; t <= T; t++){
        init();
        cin >> R >> C;

        for(int i = 1; i <= R; i++){
            for(int j = 1; j <= C; j++){
                cin >> v[i][j];
            }
        }
        for(int i = 1; i <= R; i++){
            int j = 1;
            for(; j <= C; j++){
                if(v[i][j] != '?'){
                    gol[i] = 0;
                    break;
                }
            }
            if(j == C+1){
                gol[i] = 1;
            }
        }

        for(int i = 1; i <= R; i++){
            for(int j = 1; j <= C; j++){
                if(v[i][j] != '?' && !b[v[i][j]]){
                    int lung = 0;
                    char c = v[i][j];
                    b[c] = 1;
                    while(v[i][j+lung+1] == '?'){
                        lung++;
                    }
                    int lat = 0;
                    while(gol[i+lat+1]){
                        lat++;
                    }
                    for(int i1 = i; i1 <= i + lat; i1++){
                        for(int j1 = j; j1 <= j + lung; j1++){
                            v[i1][j1] = c;
                        }
                    }
                }
            }
        }

        for(int i = 1; i <= R; i++){
            int j = 1;
            while(v[i][j] == '?'){
                j++;
            }
            char c = v[i][j];
            while(v[i][--j] == '?'){
                v[i][j] = c;
            }
        }
        for(int j = 1; j <= C; j++){
            if(v[1][j] == '#'){
                int aux = 0;
                while(v[1+aux+1][j] == '#'){
                    aux++;
                }
                char c = v[1+aux+1][j];
                for(int i = 1+aux; i > 0; i--){
                    v[i][j] = c;
                }
            }
        }

        cout << "Case #" << t << ":\n";
        for(int i = 1; i <= R; i++){
            for(int j = 1; j <= C; j++){
                cout << v[i][j];
            }
            cout << '\n';
        }
    }


    return 0;
}
