#include<bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fp, *fc;
    int t;
    ifstream fin("A-large (2).in");
    ofstream fout("out.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        double mt=0;
        double n, s[1005];
        double d, k[1005];
        double ti[1005], ms;
        fin>>d>>n;
        for(int i=0;i<n;i++){
            fin>>k[i]>>s[i];
            ti[i] = (double)((d-k[i])/s[i]);
            mt = max(ti[i], mt);
        }
        ms = (double)(d/mt);
        fout<<"Case #"<<cas<<": ";
        fout<<std::fixed<<std::setprecision(6)<<ms<<endl;

    }
    fin.close();
    fout.close();
    return 0;
}

