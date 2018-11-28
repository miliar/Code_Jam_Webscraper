/* Date: 2017 04 14
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
#include <queue>

using namespace std;
typedef long long ll;
#define err(...) fprintf(stderr,__VA_ARGS__)
#define debug(var) cerr << #var << " = " << var << " ";

#define maxn 50
#define maxp 50

int n,p;
ll req[maxn];

struct Package {
    int ing; // Ingredient number
    ll minServe;
    ll maxServe;
    Package(int ing, ll quant): ing(ing) {
        minServe = (quant*10 + 11*req[ing]-1) / (11*req[ing]);
        maxServe = (quant*10) / (9*req[ing]);
    }
    // < compares by the maximum num. servings this can be used in
    // Reverse order, so that smaller maxima are dequeued first
    bool operator< (const Package &other) const {
        return maxServe > other.maxServe;
    }
};

// This comparator is for the vector (not the pqueue)... sort by minimum number of servings to use it in
// Break ties by the lower maximum serving
bool packMinCmp(const Package &a, const Package &b) {
    if (a.minServe != b.minServe) return a.minServe < b.minServe;
    return a.maxServe < b.maxServe;
}

vector<Package> packs;
priority_queue<Package> useful[maxn];

void doCase(int case_number) {
    scanf("%d%d",&n,&p);
    for (int i=0; i<n; i++) {
        scanf("%lld",req+i);
        while (!useful[i].empty()) useful[i].pop(); //empty from earlier test cases
    }

    packs.clear();
    for (int i=0; i<n; i++) {
        for (int j=0; j<p; j++) {
            ll quant;
            scanf("%lld",&quant);
            Package pack(i,quant);
            if (pack.minServe <= pack.maxServe) packs.push_back(pack);
        }
    }
    
    sort(packs.begin(), packs.end(), packMinCmp);
    
    ll servings = 0;
    int kits = 0;

    for (vector<Package>::iterator it = packs.begin(); it != packs.end(); it++) {
        Package nx = *it;
        useful[nx.ing].push(nx);
        //err("Pulling off [%d,%d] for ingredient %d...\n",nx.minServe,nx.maxServe,nx.ing);
        servings = nx.minServe;
        //err("Servings = %d\n",servings);
    
        // Pop off any packages that can no longer be used, and count ingredients present
        int ings = 0;
        for (int i=0; i<n; i++) {
            while (!useful[i].empty() && useful[i].top().maxServe < servings) {
                //err("Obsolete: [%d,%d] for %d\n",useful[i].top().minServe,useful[i].top().maxServe,useful[i].top().ing);
                useful[i].pop();
            }
            if (!useful[i].empty()) ings++;
        }

        // Make a kit if possible!
        if (ings == n) {
            kits++;
            for (int i=0; i<n; i++) {
                //err("KITTING: [%d,%d] for %d\n",useful[i].top().minServe,useful[i].top().maxServe,useful[i].top().ing);
                useful[i].pop();
            }
        }
    }

    printf("Case #%d: %d\n",case_number,kits);
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
