#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main()
{
    ifstream fin("test.in");
    ofstream fout("rez.out");
    int t;
    fin>>t;
    int T=t;
    int n,g;
    while(t--){
        fin>>n>>g;
        int ar[4];
        memset(ar,0,sizeof(ar));
        int rez = 0;
        int k;
        for(int ctr1 = 0; ctr1 < n; ctr1++) {
            fin>>k;
            ar[k%g]++;
        }
        rez += ar[0];
        ar[0] = 0;
        if (g == 2) {
            rez += ar[1]/2;
            ar[1] %= 2;
        }
        else if(g == 3) {
            int tt = min(ar[1], ar[2]);
            rez += tt;
            ar[1] -= tt;
            ar[2] -= tt;
        }
        else if (g == 4) {
            int tt = min(ar[1], ar[3]);
            rez += tt;
            ar[1] -= tt;
            ar[3] -= tt;
            rez += ar[2]/2;
            ar[2] %= 2;
            if(ar[1] < ar[3])
                swap(ar[1],ar[3]);
            if(ar[2] == 1 && ar[1] >= 2){
                ar[1] -= 2;
                ar[2]--;
                rez++;
            }
        }
        bool flag = 0;
        for(int ctr1 = 3; ctr1 > 0; ctr1 --) {
            if (flag) {
                rez += ar[ctr1]/g;
            }
            else {
                flag = ar[ctr1]%g;
                rez += ar[ctr1]/g;
            }
        }
        rez += flag;
        fout<<"Case #"<<T-t<<": "<<rez<<"\n";
        cout<<"Case #"<<T-t<<": "<<rez<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
