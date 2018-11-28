#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i,d;
    string n;
    int k ,c;
    for (i = 0; i < numCase; i++)
    {
        fin >> n >> k;
        int count = 0;
        bool a [n.size()];
        bool pos = true;
        for (int j = 0;j<n.size();j++){
            if(n[j]=='+')a[j] = true;
            else{a[j]=false;}
            if(j >= k){if(!a[j-k]){count++;
                for(int l = 0; l < k ;l++){a[j-k+l]=!a[j-k+l];}
            }}
        }if(!a[n.size()-k]){count++;for(int l = 0; l < k ;l++){a[n.size()-k+l]=!a[n.size()-k+l];}}
        for(int l = 0; l < k ;l++)pos = pos && a[n.size()-k+l];
        if(!pos){fout << "Case #" << (i + 1) << ": " << "IMPOSSIBLE"<< endl;}
        else{fout << "Case #" << (i + 1) << ": " << count << endl;}
    }
    fin.close();
    fout.close();
    return 0;
}
