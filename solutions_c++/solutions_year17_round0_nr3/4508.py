#include <fstream>

using namespace std;

int lungv, t;

long long int v[5], no[5], n, k, decided, step;

struct pereche {
    int x, y;
};

pereche r;

void managev(){
    if(lungv == 1){
        if(v[1] % 2 == 1){
            v[1] /= 2; no[1] = 2 * no[1];
        }
        else {
            lungv = 2;
            v[1] = v[1] / 2 - 1;
            v[2] = v[1] + 1;
            no[2] = no[1];
        }
    }
    else {
        if(v[1] % 2 == 0){
            v[1] = v[1] / 2 - 1;
            v[2] = v[1] + 1;
            no[2] = 2 * no[2] + no[1];
        }
        else {
            v[1] = v[1] / 2;
            v[2] = v[1] + 1;
            no[1] = 2 * no[1] + no[2];
        }
    }
}

pereche solve(int value){
    pereche temp;
    if(value % 2){
        temp.x = value / 2;
        temp.y = temp.x;
    }
    else {
        temp.x = value / 2;
        temp.y = temp.x  - 1;
    }
    return temp;
}

int main()
{
    ifstream in("infile.txt");
    ofstream out("outfile.txt");
    in>>t;
    for(int i = 1; i <= t; ++i){
        in>>n;
        in>>k;
        out<<"Case #"<<i<<": ";
        decided = 0; step = 1;
        lungv = 1; v[1] = n; no[1] = 1;
        while(decided + step < k){
                decided += step;
                step *= 2;
                managev();
                /*out<<"\n"<<lungv<<" ";
                if(lungv == 1) out<<v[1];
                if(lungv == 2) out<<no[1]<<" "<<no[2];*/
        }
        if(lungv == 1){
            r = solve(v[1]);
        }
        else if(lungv == 2){
            if(decided + no[2] >= k){
                //out<<v[2]<<"\n";
                r = solve(v[2]);
            }
            else r = solve(v[1]);
        }
        out<<r.x<<" "<<r.y<<"\n";
    }
    return 0;
}
