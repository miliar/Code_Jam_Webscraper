/*
  Author:       Dean Hirsch
  Date:         April 8th, 2017
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>

#define DO(n) for(i=0; i < n; i++)

using namespace std;

#define INPUT_FILENAME      "C-large.in" //"D-large.in"
#define OUTPUT_FILENAME     "output.out"

typedef unsigned long long int u64;
typedef long long int i64;

i64 compute(i64 N, i64 M);

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open(INPUT_FILENAME);
    if(!fin.is_open()){
        cout << "Error: failed to open input file\n";
        return 1;
    }
    fout.open(OUTPUT_FILENAME, ios::trunc);
    if(!fout.is_open()){
        cout << "Error: failed to open output file\n";
        return 1;
    }

    int T;
    fin >> T;
    for(int line_num=1; line_num<=T; line_num++){
        if(fin.eof()){
            cout << "Error: fewer lines than what was promised!\n";
            fout << "Error: fewer lines than what was promised!\n";
            break;
        }
        i64 N, M;
        fin >> N >> M;
        i64 ret = compute(N, M);
        cout << "Case #" << line_num << ": " << ret/2 << " " << (ret-1)/2 << "\n";
        fout << "Case #" << line_num << ": " << ret/2 << " " << (ret-1)/2 << "\n";
    }

    fin.close();
    fout.close();
    return 0;
}

i64 compute(i64 N, i64 M)
{
    i64 k;
    i64 n1=N, n2=N+1;
    i64 c1=1, c2=0;
    for(k=1; k < M;)
    {
        //cout <<n1<<":"<<c1<<", "<<n2<<": "<<c2<<"\n";

        if(n1%2==0)
            c2 += c1 + c2;
        else
            c1 += c1 + c2;
        M -= k;
        k *= 2;

        n1 = (n1-1)/2;
        n2 = n2/2;
    }
    return M <= c2 ? n2 : n1;
}


