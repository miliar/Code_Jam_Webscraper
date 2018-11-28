#include <iostream>
#include <cstdint>
#include <fstream>
#include <cmath>
#include <vector>
#include <fstream>
using namespace std;
#define pb push_back

int main() {

 ifstream fin;
 ofstream fout;
 fout.open("prog2.txt");
 fin.open("B-small-attempt0.in");

 int t;
 fin>>t;
 for(int d=0; d<t; d++)
 {
    uint64_t m;
    fin>>m;
    vector<int> q;
    while(m>9){
        int a = m%10;
        m = m/10;
        int b = m%10;
        q.pb(a);
        if(a<b){
            for(int i=0; i<q.size(); i++)
                q[i] = 9;
            m--;
        }
    }
    if(m)
        q.pb(m%10);

    uint64_t z = 0;
    for(int i=0; i<q.size(); i++){
        z = z + (q[i]*pow(10, i));
    }
    fout<<"Case #"<<d+1<<": "<<z<<endl;

	q.clear();
  }

 	fin.close();
 	fout.close();
    return 0;
}
