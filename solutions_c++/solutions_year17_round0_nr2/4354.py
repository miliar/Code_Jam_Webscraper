#include <fstream>

using namespace std;

long long int n, res, ntemp;

int k, t, cif, r;

int v[20], ans[20];

int main()
{
    ifstream in ("infile.txt");
    ofstream out ("outfile.txt");
    in>>t;
    k = 1;
    while(k <= t){
        in>>n;
        cif = 0;
        ntemp = n;
        while(n){
            v[++cif] = n % 10;
            ans[cif] = v[cif];
            n /= 10;
        }
        for(int i = cif; i >= 2; --i){
            if(v[i] > v[i - 1] && v[i] > 1){
                r = i;
                while(ans[r] == v[i]){
                    ans[r] = 9;
                    r++;
                }
                ans[r - 1] = v[i] - 1;
                for(int j = i - 1; j >= 1; --j){
                    ans[j] = 9;
                }
                goto finish;
            }
            if(v[i] > v[i - 1] && v[i] == 1){
                ans[cif] = 0;
                for(int j = cif - 1; j >= 1; --j)
                    ans[j] = 9;
                goto finish;
            }
        }
        finish:
        res = 0;
        for(int i = cif; i >= 1; --i){
            res = res * 10 + ans[i];
            ans[i] = 0;
            v[i] = 0;
        }
        out<<"Case #"<<k<<": "<<res<<"\n";
        k++;
    }
    return 0;
}
