#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool emp[50];

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
    for(int coun = 0; coun < T; coun++) {
        vector<vector<char> > grid;
        int R, C;
        fin >> R >> C;
        for(int i = 0; i < R; i++) {
            vector<char> c;
            emp[i] = true;
            for(int j = 0; j < C; j++) {
                char n;
                fin >> n;
                if(n != '?') {
                    emp[i] = false;
                }
                c.push_back(n);
            }
            grid.push_back(c);
        }

        for(int i = 0; i < R; i++) {
            if(!emp[i]) {
                for(int j = 0; j < C; j++) {
                    if(grid[i][j] == '?') {
                        char n = ' ';
                        for(int ji = j; ji < C; ji++) {
                            if(grid[i][ji] != '?') {
                                n = grid[i][ji];
                                break;
                            }
                        }
                        if(n == ' ') {
                            for(int ji = j; ji >=0; ji--) {
                                if(grid[i][ji] != '?') {
                                    n = grid[i][ji];
                                    break;
                                }
                            }
                        }
                        grid[i][j] = n;
                    }
                }
            }
        }

        for(int i = 0; i < R; i++) {
            if(emp[i]) {
                int x = i;
                while(x >= 1) {
                    x--;
                    if(!emp[x]) {
                        for(int j = 0; j < C; j++) {
                            grid[i][j] = grid[x][j];
                        }
                        emp[i] = false;
                        break;
                    }
                }

                if(emp[i]) {
                    int x = i;
                    while(x < R) {
                        x++;
                        if(!emp[x]) {
                            for(int j = 0; j < C; j++) {
                                grid[i][j] = grid[x][j];
                            }
                            emp[i] = false;
                            break;
                        }
                    }
                }
            }

        }
        fout << "Case #" << coun+1 << ": \n";
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                fout << grid[i][j];
            }
            fout << '\n';
        }

    }

}
