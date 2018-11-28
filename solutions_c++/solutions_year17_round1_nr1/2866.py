#include <bits/stdc++.h>

using namespace std;

int R, C;
string line;

void _main(int TEST)
{
    scanf("%d%d", &R, &C);
    vector<vector<char> > grid(R, vector<char>(C, '?'));
    vector<pair<int, int>> letters;

    for(int i = 0; i < R; ++i){
        cin >> line;
        for(int j = 0; j < C; ++j){
            grid[i][j] = line[j];

            if(line[j] != '?')
                letters.push_back({j, i});
        }
    }

    for(int i = 0; i < letters.size(); ++i)
    {
        int vleft, vtop, vright, vbottom;
        int count = 0;

        for(int left = letters[i].first; left >= 0; --left){
            for(int right = letters[i].first; right < C; ++right){
                for(int top = letters[i].second; top >= 0; --top){
                    for(int bottom = letters[i].second; bottom < R; ++bottom){

                        int nb = 0;
                        for(int x = left; x <= right; ++x){
                            for(int y = top; y <= bottom; ++y){
                                if(grid[y][x] != '?' && grid[y][x] != grid[letters[i].second][letters[i].first]){
                                    x = y = 100;
                                    nb = 0;
                                }
                                else{
                                    ++nb;
                                }
                            }
                        }

                        if(nb > count){
                            count   = nb;
                            vleft   = left;
                            vtop    = top;
                            vright  = right;
                            vbottom = bottom;
                        }

                    }
                }
            }
        }
cerr << "count: " << count << endl;
        for(int x = vleft; x <= vright; ++x){
            for(int y = vtop; y <= vbottom; ++y){
                grid[y][x] = grid[letters[i].second][letters[i].first];
            }
        }
    }

    for(int i = 0; i < R; ++i){
        for(int j = 0; j < C; ++j){
            cout << grid[i][j];
            cerr << grid[i][j];
        }
        cout << endl;
        cerr << endl;
    }
}

int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: \n", i);
        cerr << "Case #" << i << ": " << endl;
        _main(i);
    }
}
