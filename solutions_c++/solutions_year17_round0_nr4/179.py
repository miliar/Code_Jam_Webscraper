/* Date: 2017-04-08
 * Comments: in-contest
 */

#include <fstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
#define err(...) fprintf(stderr,__VA_ARGS__)
#define debug(var) cerr << #var << " = " << var << " ";

#define maxn 100

int n,m;
struct Cell {
    char origtype;
    char finaltype;
    int hasP;
    int hasX;
} cell[maxn+1][maxn+1];

bool rowused[maxn+1];
bool colused[maxn+1];

void fillX() {
    for (int i=1; i<=n; i++) for (int j=1; j<=n; j++) {
        if (!rowused[i] && !colused[j]) {
            rowused[i] = colused[j] = true;
            cell[i][j].hasX = true;
        }
    }
}

// Diagonals: name by i-j+n (1 to 2n-1)
// Slant diagonals: name by i+j (2 to 2n)
// d and s meet "on board" if d+s-n is EVEN and between 2 and 2n, inclusive, and s-d+n has same bounds.
bool dblock[2*maxn];
bool sblock[2*maxn+1];

int sprev[2*maxn+1]; //Use 0 to indicate unmatched
bool dused[2*maxn];

bool dfs(int d) {
    if (d == 0) return true;
    if (dblock[d] || dused[d]) return false;
    dused[d] = true;
    for (int s=2; s<=2*n; s++) {
        if (sblock[s]) continue;
        if ((d+s-n)%2 == 1) continue;
        int i = (d+s-n)/2;
        int j = (s-d+n)/2;
        if (i<1 || i > n || j<1 || j>n) continue;

        int dd = sprev[s];
        if (dfs(dd)) {
            sprev[s] = d;
            return true;
        }
    }
    return false;
}

void fillP() {
    for (int d=1; d<=2*n-1; d++) dblock[d] = false;
    for (int s=2; s<=2*n; s++) {
        sblock[s] = false;
        sprev[s] = 0;
    }
    for (int i=1; i<=n; i++) for (int j=1; j<=n; j++) {
        int d = i-j+n;
        int s = i+j;
        if (cell[i][j].hasP) dblock[d] = sblock[s] = true;
    }

    //Compute sprev for a maximal matching
    for (int d=1; d<=2*n-1; d++) {
        for (int dd=1; dd<=2*n-1; dd++) dused[dd] = false;
        dfs(d);
    }
    
    // Update hasP
    for (int i=1; i<=n; i++) for (int j=1; j<=n; j++) {
        int d = i-j+n;
        int s = i+j;
        if (dblock[d] || sblock[s]) continue;
        if (sprev[s] == d) cell[i][j].hasP = 1;
    }
}

void showMe() {
    err("original grid:\n");
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            err("%c",cell[i][j].origtype);
        }
        err("\n");
    }
    err("final grid:\n");
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            err("%c",cell[i][j].finaltype);
        }
        err("\n");
    }
}

void doCase(int case_number) {
    cin >> n >> m;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            cell[i][j].origtype = '.';
            cell[i][j].hasP = cell[i][j].hasX = 0;
        }
        rowused[i] = false;
        colused[i] = false;
    }
    for (int l=0; l<m; l++) {
        char t;
        int i,j;
        cin >> t >> i >> j;
        cell[i][j].origtype = t;
        if (t == '+' || t == 'o') cell[i][j].hasP = 1;
        if (t == 'x' || t == 'o') cell[i][j].hasX = 1;
        if (cell[i][j].hasX) rowused[i] = colused[j] = true;
    }

    fillX();
    fillP();

    int score = 0;
    vector<pair<int,int> > changes;
    for (int i=1; i<=n; i++) for (int j=1; j<=n; j++) {
        score += cell[i][j].hasX + cell[i][j].hasP;
        if (cell[i][j].hasX && cell[i][j].hasP) cell[i][j].finaltype = 'o';
        else if (cell[i][j].hasX) cell[i][j].finaltype = 'x';
        else if (cell[i][j].hasP) cell[i][j].finaltype = '+';
        else cell[i][j].finaltype = '.';
        if (cell[i][j].finaltype != cell[i][j].origtype) {
            changes.push_back(pair<int,int>(i,j));
        }
    }

    printf("Case #%d: %d %lu\n",case_number,score,changes.size());
    for (vector<pair<int,int> >::iterator it=changes.begin(); it != changes.end(); it++) {
        int i = it->first;
        int j = it->second;
        char c = cell[i][j].finaltype;
        printf("%c %d %d\n",c,i,j);
    }
    //showMe();
}

/* PROBLEM NON-SPECIFIC TEMPLATE CODE FOLLOWS.
 * This template version created 25 April 2016.
 * The code below reads the input, and prints the output either to stdout or to a file.
 * If output goes to a file, it also writes a log file for later reference.
 * Notes:
 *  - If no arguments are provided, the program reads from standard input and prints to standard output.
 *  - The first argument specifies the input file name. If it is "x", the standard input is used.
 *  - The second argument specifies the output file name. If it is "a", an unused filename is created.
 *  - This code assumes that the first line of the input is the number of cases that follow.
 *  - If output is written to a file, then a corresponding "log" file is also created, to store some basic information and the source code used to create this output.
 */

ofstream logstream;

int main(int argc, char **argv) {
    if (argc>1 && argv[1][0]!= 'x') freopen(argv[1],"r",stdin);
    if (argc>2) {
        // Second argument tells filename for the output.
        // If the argument is "a" (for auto), one is created.
        char outfname[100];
        char logfname[100];
        if (argv[2][0] != 'a') {
            strcpy(outfname,argv[2]);
            sprintf(logfname,"%s.log",outfname);
        } else {
            int id = 0;
            // stem will remove ".in" from the input file name, if present.
            char stem[100];
            strcpy(stem,argv[1]);
            if (strcmp(stem+(strlen(stem)-3),".in") == 0) stem[strlen(stem)-3] = 0;
            char outfname[100];
            while (true) {
                sprintf(outfname,"%s.out%d",stem,id);
                sprintf(logfname,"%s.log%d",stem,id);
                ifstream in(outfname);
                if (!in) break;
                id++;
            }
            freopen(outfname,"w",stdout);
            logstream.open(logfname);
            err("Writing output to %s.\n",outfname);

            // Generate a log for this execution.
            time_t rawtime = time(NULL);
            tm *timeinfo = localtime(&rawtime);
            logstream << asctime(timeinfo);
        }
    }
    int T; cin >> T;
    err("There are %d cases.\n",T);
    logstream << "There are " << T << " cases." << endl;
    
    clock_t prev,cur = clock();
    clock_t start = cur;
    for (int t=1; t<=T; t++) {
        doCase(t);
        prev = cur;
        cur = clock();
        int time_elapsed = (int) ( 1000*(cur - prev) / ((int)CLOCKS_PER_SEC));
        err("_%d(%d)_",t, time_elapsed);
        logstream << "Case #" << t << " completed in " << time_elapsed << "ms" << endl;

    }
    int total_time = (int) ( 1000*(cur-start) / ((int)CLOCKS_PER_SEC) );
    err("\nFinished %d cases in %d milliseconds.\n",T,total_time);

    // Print the source code (minus the template) to the log for reference.
    if (logstream.good()) {
        logstream << "Total time: " << total_time << endl;
        logstream << "\nCurrent source code for " << __FILE__ << ":" << endl;
        ifstream src;
        src.open(__FILE__);
        while (true) {
            string line; getline(src,line);
            if (line == "/* PROBLEM NON-SPECIFIC TEMPLATE CODE FOLLOWS.") break;
            logstream << line << endl;
        }
        logstream << "(Truncating at the beginning of the template code)" << endl;
    }
}
