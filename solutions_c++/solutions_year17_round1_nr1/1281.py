#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

struct Box {
    int xmin, xmax, ymin, ymax;
    Box() {
        xmin = ymin = 1000;
        xmax = ymax = -1000;
    }
};

int R, C;

Box box['Z'+1];

string M[25];


static bool rowEmpty(int z, int a, int b) {
    if (z<0 || z>=R || a<0 || b>=C)
        return false;
    for (int i=a; i<=b; i++)
        if (M[z][i] != '?')
            return false;
    return true;
}

static bool colEmpty(int z, int a, int b) {
    if (z<0 || z>=C || a<0 || b>=R)
        return false;
    for (int i=a; i<=b; i++)
        if (M[i][z] != '?')
            return false;
    return true;
}

static void fillRow(int z, int a, int b, char x) {
    for (int i=a; i<=b; i++) M[z][i] = x;
}

static void fillCol(int z, int a, int b, char x) {
    for (int i=a; i<=b; i++) M[i][z] = x;
}

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        fill(box+'A', box+'Z'+1, Box());
        cin>>R>>C;
        for (int i=0; i<R; i++) {
            cin>>M[i];
            for (int j=0; j<C; j++) {
                char a = M[i][j];
                if (a != '?') {
                    box[a].xmin = min(box[a].xmin, j);
                    box[a].xmax = max(box[a].xmin, j);
                    box[a].ymin = min(box[a].ymin, i);
                    box[a].ymax = max(box[a].ymin, i);
                }
            }
        }
        
        bool chg;
        do {
            chg = false;
            for (char a='A'; a<='Z'; a++) {
                if (box[a].xmax < 0)
                    continue;
                if (colEmpty(box[a].xmin-1, box[a].ymin, box[a].ymax))
                    box[a].xmin--, fillCol(box[a].xmin, box[a].ymin, box[a].ymax, a), chg=true;
                if (colEmpty(box[a].xmax+1, box[a].ymin, box[a].ymax))
                    box[a].xmax++, fillCol(box[a].xmax, box[a].ymin, box[a].ymax, a), chg=true;
                if (rowEmpty(box[a].ymin-1, box[a].xmin, box[a].xmax))
                    box[a].ymin--, fillRow(box[a].ymin, box[a].xmin, box[a].xmax, a), chg=true;
                if (rowEmpty(box[a].ymax+1, box[a].xmin, box[a].xmax))
                    box[a].ymax++, fillRow(box[a].ymax, box[a].xmin, box[a].xmax, a), chg=true;
            }
        }
        while (chg);
                    
        cout<<"Case #"<<t<<":\n";
        for (int i=0; i<R; i++)
            cout<<M[i]<<endl;
    }
    
    return 0;
}

