#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <algorithm>
#include <ctime>
#include <map>
#include <bitset>
using namespace std;

int const BTS_SIZE = 4096;

int const MAX_N = 1024 * 1024;
int const MAX_CH = 5000010;
int const INT_INF = 1000000000;
char const HOR_CH = '-';
char const VER_CH = '|';
int const DX[4] = {-1,1,0,0};
int const DY[4] = {0,0,-1,1};
int const OCH_SIZE = 256*256*5;
int const RIGHT_MOVE = 3;
int const DOWN_MOVE = 1;
int const LEFT_MOVE = 2;
int const UP_MOVE = 0;

int n,m;

char st[MAX_CH];
char s[128][128],rec_s[128][128];
int nnew[128][128][4];

struct elem {
    int x,y;
    char ch;
    int can_h, can_v;
    bitset<BTS_SIZE> h,v;
    elem():x(-1),y(-1),ch(0),can_h(0),can_v(0) {h.reset(); v.reset();}
    elem(int x, int y, char ch):x(x),y(y),ch(ch),can_h(0),can_v(0) {h.reset(); v.reset();}
};
vector<elem> ms,new_ms;

bitset<BTS_SIZE> fld,emp_fld,init_fld;

int x_och[OCH_SIZE], y_och[OCH_SIZE], dd_och[OCH_SIZE];

inline int is_shooter(char ch) {
    return ch == HOR_CH || ch == VER_CH;
}

inline int valid_cell_to_go(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m)
        return 0;
    if (s[x][y] == '#')
        return 0;
    return 1;
}

void add_cell(int new_x, int new_y, int new_dir, int & p_write) {
    if (!valid_cell_to_go(new_x,new_y))
        return;

    if (new_dir < 0 || new_dir >= 4)
        return;

    x_och[p_write] = new_x;
    y_och[p_write] = new_y;
    dd_och[p_write] = new_dir;

    nnew[new_x][new_y][new_dir] = 1;

    p_write++;
}

int get_cover_map(int x, int y, char ch, bitset<BTS_SIZE> & flag) {
    flag.reset();
    char save_ch = s[x][y];
    s[x][y] = ch;

    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            for (int k=0; k<4; k++)
                nnew[i][j][k] = 0;

    int p_read = 0, p_write = 0;

    if (ch == HOR_CH) {
        if (valid_cell_to_go(x,y+1)) {
            x_och[p_write] = x;
            y_och[p_write] = y+1;
            dd_och[p_write] = RIGHT_MOVE;
            nnew[x][y+1][RIGHT_MOVE] = 1;
            p_write++;
        }
        if (valid_cell_to_go(x,y-1)) {
            x_och[p_write] = x;
            y_och[p_write] = y-1;
            dd_och[p_write] = LEFT_MOVE;
            nnew[x][y-1][LEFT_MOVE] = 1;
            p_write++;
        }
    }
    else {
         if (valid_cell_to_go(x-1,y)) {
            x_och[p_write] = x-1;
            y_och[p_write] = y;
            dd_och[p_write] = UP_MOVE;
            nnew[x-1][y][UP_MOVE] = 1;
            p_write++;
        }
        if (valid_cell_to_go(x+1,y)) {
            x_och[p_write] = x+1;
            y_och[p_write] = y;
            dd_och[p_write] = DOWN_MOVE;
            nnew[x+1][y][DOWN_MOVE] = 1;
            p_write++;
        }
    }

    while (p_read < p_write) {
        int x = x_och[p_read];
        int y = y_och[p_read];
        int dd = dd_och[p_read];
        p_read++;

        if (s[x][y] == '#')
            continue;

        if (s[x][y] == '.') {
            add_cell(x + DX[dd], y + DY[dd], dd, p_write);
            continue;
        }

        if (s[x][y] == '/') {
            if (dd == UP_MOVE)
                add_cell(x + DX[RIGHT_MOVE], y + DY[RIGHT_MOVE], RIGHT_MOVE, p_write);
            else if (dd == DOWN_MOVE)
                add_cell(x + DX[LEFT_MOVE], y + DY[LEFT_MOVE], LEFT_MOVE, p_write);
            else if (dd == RIGHT_MOVE)
                add_cell(x + DX[UP_MOVE], y + DY[UP_MOVE], UP_MOVE, p_write);
            else if (dd == LEFT_MOVE)
                add_cell(x + DX[DOWN_MOVE], y + DY[DOWN_MOVE], DOWN_MOVE, p_write);
            continue;
        }

        if (s[x][y] == '\\') {
            if (dd == UP_MOVE)
                add_cell(x + DX[LEFT_MOVE], y + DY[LEFT_MOVE], LEFT_MOVE, p_write);
            else if (dd == DOWN_MOVE)
                add_cell(x + DX[RIGHT_MOVE], y + DY[RIGHT_MOVE], RIGHT_MOVE, p_write);
            else if (dd == RIGHT_MOVE)
                add_cell(x + DX[DOWN_MOVE], y + DY[DOWN_MOVE], DOWN_MOVE, p_write);
            else if (dd == LEFT_MOVE)
                add_cell(x + DX[UP_MOVE], y + DY[UP_MOVE], UP_MOVE, p_write);
            continue;
        }
    }

    s[x][y] = save_ch;

    int is_Ok = 1;

    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            for (int k=0; k<4; k++)
                if (nnew[i][j][k]) {
                    if (s[i][j] == '.')
                        flag.set(i*m+j,1);
                    if (is_shooter(s[i][j]))
                        is_Ok = 0;
                }

    return is_Ok;
}

void print_our_field() {
    for (int i=0; i<n; i++) {
        printf("\n");
        for (int j=0; j<m; j++) printf("%c",s[i][j]);
    }
}

vector<pair<int,char> > cov_map[128][128];
int cov_map_len[128][128];

int REC_ANS_FOUND = 0;
clock_t t_bg;

int emp_x[128*128],emp_y[128*128],emp_len = 0;

double tot_time = 0.0;
double const ONE_TEST_TIME = 9.0;

void rec(int from, bitset<BTS_SIZE> fld) {
    if (REC_ANS_FOUND)
        return;

    if (from >= (int) new_ms.size()) {
        if (fld == emp_fld) {
            REC_ANS_FOUND = 1;
            for (int i=0; i<n; i++)
                for (int j=0; j<m; j++)
                    rec_s[i][j] = s[i][j];
        }
        return;
    }

    for (int i=0; i<emp_len; i++) {
        int x = emp_x[i];
        int y = emp_y[i];

        if (!fld.test(x*m+y))
            if (cov_map_len[x][y] <= 0)
                return;
    }

    tot_time = ((double) (clock()-t_bg)) / (CLOCKS_PER_SEC);
    if (tot_time > ONE_TEST_TIME)
        return;

    // rem item from cml
    for (int i=0; i<emp_len; i++) {
        int x = emp_x[i];
        int y = emp_y[i];

        if (new_ms[from].h.test(x*m+y))
            cov_map_len[x][y]--;
        
        if (new_ms[from].v.test(x*m+y))
            cov_map_len[x][y]--;
    }
    //

    s[new_ms[from].x][new_ms[from].y] = HOR_CH;
    rec(from+1, fld | new_ms[from].h);

            if (REC_ANS_FOUND)
                return;
            tot_time = ((double) (clock()-t_bg)) / (CLOCKS_PER_SEC);
            if (tot_time > ONE_TEST_TIME)
                return;

    s[new_ms[from].x][new_ms[from].y] = VER_CH;
    rec(from+1, fld | new_ms[from].v);

            if (REC_ANS_FOUND)
                return;
            tot_time = ((double) (clock()-t_bg)) / (CLOCKS_PER_SEC);
            if (tot_time > ONE_TEST_TIME)
                return;

    // add item from cml
    for (int i=0; i<emp_len; i++) {
        int x = emp_x[i];
        int y = emp_y[i];

        if (new_ms[from].h.test(x*m+y))
            cov_map_len[x][y]++;
        
        if (new_ms[from].v.test(x*m+y))
            cov_map_len[x][y]++;
    }
    //
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
        cerr<<"\r"<<qq;
		
        gets(st);
        sscanf(st,"%d%d",&n,&m);
        for (int i=0; i<n; i++) {
            gets(st);
            for (int j=0; j<m; j++)
                s[i][j] = st[j];
        }

        ms.clear();
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (is_shooter(s[i][j]))
                    ms.push_back(elem(i,j,s[i][j]));

        for (int a=0; a<n; a++)
            for (int b=0; b<m; b++)
                cov_map[a][b].clear();

        int is_poss = 1;
        for (int i=0; i<(int) ms.size(); i++) {
            ms[i].can_v = get_cover_map(ms[i].x,ms[i].y,VER_CH,ms[i].v);
            if (ms[i].can_v)
                for (int a=0; a<n; a++)
                    for (int b=0; b<m; b++)
                        if (s[a][b] == '.')
                            if (ms[i].v.test(a*m+b))
                                cov_map[a][b].push_back(make_pair(i,VER_CH));

            ms[i].can_h = get_cover_map(ms[i].x,ms[i].y,HOR_CH,ms[i].h);
            if (ms[i].can_h)
                for (int a=0; a<n; a++)
                    for (int b=0; b<m; b++)
                        if (s[a][b] == '.')
                            if (ms[i].h.test(a*m+b))
                                cov_map[a][b].push_back(make_pair(i,HOR_CH));

            if (ms[i].can_h == 0 && ms[i].can_v == 0) {
                is_poss = 0;
                break;
            }
        }

        if (!is_poss) {
            printf("Case #%d: ",qq+1);
            printf("IMPOSSIBLE");
		    printf("\n");
            continue;
        }

        new_ms.clear();
        fld.reset();

        vector<int> used((int) ms.size(), 0);
        vector<char> used_ch((int) ms.size(), 0);

        for (int a=0; a<n && is_poss; a++)
            for (int b=0; b<m; b++)
                if (s[a][b] == '.') {
                    int our_size = (int) cov_map[a][b].size();
                    if (our_size <= 0) {
                        is_poss = 0;
                        break;
                    }
                    else if (our_size == 1) {
                        int ind = cov_map[a][b][0].first;
                        char ch = cov_map[a][b][0].second;

                        used[ind] = 1;
                        used_ch[ind] = ch;
                    }
                }

        if (!is_poss) {
            printf("Case #%d: ",qq+1);
            printf("IMPOSSIBLE");
		    printf("\n");
            continue;
        }

        for (int i=0; i<(int) ms.size(); i++) {
            if (used[i]) {
                s[ms[i].x][ms[i].y] = used_ch[i];
                if (used_ch[i] == HOR_CH)
                    fld |= ms[i].h;
                else
                    fld |= ms[i].v;
                continue;
            }

            if (ms[i].can_h + ms[i].can_v == 1) {
                if (ms[i].can_h) {
                    s[ms[i].x][ms[i].y] = HOR_CH;
                    fld |= ms[i].h;
                }
                else {
                    s[ms[i].x][ms[i].y] = VER_CH;
                    fld |= ms[i].v;
                }
            }
            else
                new_ms.push_back(ms[i]);
        }

        emp_fld.reset();
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (s[i][j] == '.')
                    emp_fld.set(i*m+j,1);

        if (fld == emp_fld) {
            printf("Case #%d: ",qq+1);
            printf("POSSIBLE");
            print_our_field();
		    printf("\n");
            continue;
        }

        init_fld = fld;
        int our_new_size = (int) new_ms.size();
        if (our_new_size <= 19) {
            int fnd = 0;

            for (int code=0; code < (1<<our_new_size) && !fnd; code++) {
                fld = init_fld;
                for (int i=0; i<our_new_size; i++)
                    if ((code>>i)&1) {
                        s[new_ms[i].x][new_ms[i].y] = HOR_CH;
                        fld |= new_ms[i].h;
                    }
                    else {
                        s[new_ms[i].x][new_ms[i].y] = VER_CH;
                        fld |= new_ms[i].v;
                    }
                if (fld == emp_fld) {
                    fnd = 1;
                    printf("Case #%d: ",qq+1);
                    printf("POSSIBLE");
                    print_our_field();
		            printf("\n");
                    break;
                }
            }

            if (!fnd) {
                printf("Case #%d: ",qq+1);
                printf("IMPOSSIBLE");
		        printf("\n");
                continue;
            }
        }
        else {
            int fnd = 0;

            // R_shuffle begin

int const MAX_ITER = min(1000000, 1000000 * 16 / our_new_size);

            srand(n*m + 17);

            for (int iter=0; iter < MAX_ITER && !fnd; iter++) {
                fld = init_fld;
                for (int i=0; i<our_new_size; i++)
                    if (rand()%2 == 0) {
                        s[new_ms[i].x][new_ms[i].y] = HOR_CH;
                        fld |= new_ms[i].h;
                    }
                    else {
                        s[new_ms[i].x][new_ms[i].y] = VER_CH;
                        fld |= new_ms[i].v;
                    }
                if (fld == emp_fld) {
                    fnd = 1;
                    printf("Case #%d: ",qq+1);
                    printf("POSSIBLE");
                    print_our_field();
		            printf("\n");
                    break;
                }
            }

            if (fnd)
                continue;

            // R_shuffle end --------------

            // rec begin
            t_bg = clock();
            REC_ANS_FOUND = 0;

            for (int i=0; i<n; i++)
                for (int j=0; j<m; j++)
                    cov_map_len[i][j] = (int) cov_map[i][j].size();

            emp_len = 0;
            for (int i=0; i<n; i++)
                for (int j=0; j<m; j++)
                    if (s[i][j] == '.') {
                        emp_x[emp_len] = i;
                        emp_y[emp_len] = j;
                        emp_len++;
                    }

            tot_time = 0.0;

            rec(0, init_fld);

            // rec end --------------------

            if (!REC_ANS_FOUND) {
                printf("Case #%d: ",qq+1);
                printf("IMPOSSIBLE");
		        printf("\n");
                continue;
            }

            printf("Case #%d: ",qq+1);
            printf("POSSIBLE");
            
            for (int a=0; a<n; a++)
                for (int b=0; b<m; b++)
                    s[a][b] = rec_s[a][b];
            print_our_field();

		    printf("\n");
            continue;
        }
	}
	
	return 0;
}