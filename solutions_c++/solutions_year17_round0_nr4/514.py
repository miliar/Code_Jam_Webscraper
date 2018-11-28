// THIS #@$%! PROBLEM RUINED MY WEEKEND HOPE YOU ARE HAPPY CODEJAM PROBLEMSETTER


// Also I failed my first submission because I forgot to delete a debug message vOv 
#ifdef VX_PRECOMPILED
    #include "precomp.h"
    typedef mpz_class big;
    // I use 4 cores :)
    #define MAX_THREADS 1
#else
    #include <bits/stdc++.h>
    #include<sys/stat.h>
    #include<unistd.h>
    // http://gmplib.org/ (uncomment if solution uses big nums)
    // most likely you'll get an error about mpz_class not being declared...
    //#include "gmpxx.h"
    #define big mpz_class
    // I figure that when other people want to test my solutions they shouldn't
    // get the whole multi-threaded mess that requires and deletes folders and files...
    #define MAX_THREADS 1
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64

using namespace std;

//=========================================================
// program:
//
struct solver
{
    int N;
    vector<string> orig;
    
    void debug(string title, vector<string> & b)
    {
        auto &x = cerr;
        x << endl << title <<" : "<<endl; for (auto s: b) x << s << endl; x << endl;
    }
    
    
    vector<string> solve()
    {
        debug("orig", orig);

        
        int posO = -1;
        for (int i = 0; i < N; i++) {
            if (orig[0][i] == 'o') {
                posO = i;
            }
            if (orig[0][i] == 'x') {
                posO = i;
            }
        }
    
        if (posO == -1) {
            posO = 0;
        }
        vector<string> res(N, string(N,'.'));
        bool reverse_it = false;
        if (posO == N-1) {
            reverse_it = true;
            posO = N - 1 - posO;
        }
        //cerr << "posO = " << posO<<endl;
        /*
                +++o++++
                x.......
                .x......
                ..x.....
                ....x...
                .....x..
                ......x.
                .++++++x
                
        */
        for (int i = 0; i < N; i++) {
            res[0][i] = '+';
            res[N-1][i] = '+';
        }
        res[N-1][0] = '.';
        for (int i = N - 1; i > posO; i--) {
            res[i][i] = 'x';
        }
        for (int i = 0; i < posO; i++) {
            res[i+1][i] = 'x';
        }
        res[0][posO] = 'o';
        if (reverse_it) {
            for (auto & s : res) {
                reverse(s.begin(), s.end());
            }
        }
        debug("res", res);
        return res;
        
    }
    
    // Verify stuff:
    int score( const vector<string>& orig, const vector<string> &board )
    {
        int N = orig.size();
        vector<bool> row(N, false);
        vector<bool> column(N, false);
        vector<bool> diag(2*N-1, false);
        vector<bool> gaid(2*N-1, false);
        
        // returns -1 if invalid
        int numO = 0, numP = 0, numX = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 'o') {
                    numO++;
                }
                if (board[i][j] == '+') {
                    numP++;
                    if ( (orig[i][j] == 'o') || (orig[i][j] == 'x') ) {
                        return -1;
                    }                    
                } else if (board[i][j] != '.') {
                    if (row[i] ||column[j]) {
                        return -2;
                    }
                    row[i] = column[j] = true;
                }
                if (board[i][j] == 'x') {
                    numX++;
                    if ( (orig[i][j] == 'o') || (orig[i][j] == '+') ) {
                        return -3;
                    }
                } else if (board[i][j] != '.') {
                    int a = i+j;
                    int b = i-j+N-1;
                    if (diag[a] || gaid[b]) {
                        cerr << a << ","<<b<<" : "<<diag[a]<<" : "<<gaid[b]<<endl;
                        return -4;
                    }
                    diag[a] = gaid[b] = true;
                }
                if (board[i][j] == '.') {
                    if (orig[i][j] != '.') {
                        return -5;
                    }
                }
            }
        }
        
        return 2*numO + numP + numX;
    }
    
    void verify( const vector<string> & orig, const vector<string> & board)
    {
        int s = score(orig, board);
        if (s < 0) { cerr <<"error: "<<s<<endl; }
        assert(s >= 0);
        
    }
    
    void init() { }
    void read() {
        cin >> N;
        orig = vector<string>(N, string(N,'.') );
        int M;
        cin >> M;
        for (int i = 0; i < M; i++) {
            char ch;
            int R, C;
            cin >> ch >> R >> C;
            assert(R == 1);
            //cout << ch << " " << R << " " << C << endl;
            orig[R-1][C-1] = ch;
        }
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        cout << "Case #"<<cn<<": ";
        vector<string> x = solve();
        verify(orig, x);
        
        vector< tuple<char,int,int> > changes;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if ( x[i][j] !=  orig[i][j] ) {
                    changes.push_back( make_tuple(x[i][j],i+1,j+1) );
                }
            }
        }
        cout << score(orig,x) << " " << changes.size() << endl;
        for (auto t: changes) {
            char ch; int i; int j;
            tie(ch,i,j) = t;
            cout << ch << " " << i << " " << j << endl;
        }
    }
    
};

//=========================================================
// I/O:
//
#if MAX_THREADS > 1
    void run(const char* x)
    {
        int r = system(x);
        cerr<<x<<" "<<"("<<r<<")"<<endl;
    }
#endif

int main(int argc, const char* argv[])
{
    int TestCases, mode;
    #if MAX_THREADS == 1
        // Simple and straight forward. 
        cin >> TestCases;
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            theSolver->read();
            theSolver->write(i);
        }
        delete theSolver;    
    #else
        cin>>TestCases;
        //-------------------------------------------
        // Copy the whole input to a file...
        ofstream f;
        f.open("tests/.input");
        f << cin.rdbuf();
        f.close();
        // Yeah...wipe that folder... Cause we will need its files to be empty
        run("rm ./tests/.t*");
        int k = 0;
        mode = 0;
        // We create some extra threads...
        while (k < MAX_THREADS) {
            if ( fork() == 0 ) {
                mode = k + 1;
                break;
            }
            k++;
        }
        // Reopen the input, this happens for each of the threads...
        if (mode != 0) {
            assert( freopen( "tests/.input","r",stdin) );
        }
    
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            // Yeah, I don't like this much either
            ofstream f;
            char fn1[200], fn2[200];
            sprintf(fn1, "tests/.test.%d", i);
            sprintf(fn2, "tests/.test.%d.done", i);
            if (mode == 0) {
                // main thread shall just join stuff together as it becomes ready
                struct stat stFileInfo;
                // When a thread finishes a test case, it writes the .done file
                // Wait for that...
                while ( stat(fn2, &stFileInfo) !=0 ) {
                    sleep(1);
                }
                // Now copy the output file...
                ifstream f(fn1);
                cout << f.rdbuf();
            } else {
                // The trick is to make each thread read all the inputs, whether
                // it will process it or not...
                theSolver->read();
                // If fn1 exists, it is being processed already. Else process it
                f.open(fn1, ios_base::out | ios_base::in);
                if ( !f ) {
                    theSolver->cout.open(fn1, ios_base::out);
                    cerr << "[" << i << "/"<<TestCases<<"] "<<mode << endl;
                    theSolver->write(i);
                    theSolver->cout.close();
                    f.open(fn2);
                    f << "1" << endl;
                }
            }
        }
        delete theSolver;
    #endif

    
    return 0;
}
