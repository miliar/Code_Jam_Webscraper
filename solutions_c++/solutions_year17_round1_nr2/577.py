#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

ii get_fit(int a, int n) {
    a *= 10;
    int k2 = a/(n*11) - 1;
//    cout << a << " " << n*k2*11 << " "<< k2<<endl;
    while(a > n*k2*11) {
        k2++;
    }
    int k1 = a/(n*9) + 1;
    while(a < n*k1*9){
        k1--;
    }
    if (a < n*k2*9 || a > n*k1*11) {
        return {-1, -1};
    }
    return {k2, k1};
}

int main()
{
    ifstream fin("test.in");
    ofstream fout("rez.out");
    int t;
    fin>>t;
    int T=t;
    while(t--){
        int n,p;
        fin>>n>>p;
        vector<int> one_ing;
        for(int ctr1=0;ctr1<n;ctr1++){
            int t;
            fin>>t;
            one_ing.push_back(t);
        }
        vector<int> pkgs[n];
        queue<ii> srted_pkgs[n];
        for(int ctr1=0;ctr1<n;ctr1++){
            for(int ctr2=0;ctr2<p;ctr2++){
                int t;
                fin>>t;
                pkgs[ctr1].push_back(t);
            }
            sort(pkgs[ctr1].begin(),pkgs[ctr1].end());
            for(int ctr2=0;ctr2<pkgs[ctr1].size();ctr2++) {
                ii t=get_fit(pkgs[ctr1][ctr2],one_ing[ctr1]);
                if(t.first != -1)
                srted_pkgs[ctr1].push(t);
            }
        }
        int rez=0;
        int cur_take = 1;
        while(1) {
            rbgn:
            for(int ctr1=0;ctr1<n;ctr1++) {
                bgn:
                if(srted_pkgs[ctr1].empty())
                    goto done;
                while(srted_pkgs[ctr1].front().second < cur_take) {
                    srted_pkgs[ctr1].pop();
                    goto bgn;
                }
                if (srted_pkgs[ctr1].front().first > cur_take) {
                    cur_take = srted_pkgs[ctr1].front().first;
                    goto rbgn;
                }
            }
            rez++;
            for(int ctr1=0;ctr1<n;ctr1++)
                srted_pkgs[ctr1].pop();
        }
        done:
        fout<<"Case #"<<T-t<<": "<<rez<<"\n";
        cout<<"Case #"<<T-t<<": "<<rez<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
