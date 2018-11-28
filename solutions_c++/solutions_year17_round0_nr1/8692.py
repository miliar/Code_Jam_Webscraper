#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t,T;
    fin >> t;
    T = t;
    int switched[1010];
    while(t--) {
        string s;
        int k;
        fin>>s>>k;
        int rez = 0;
        memset(switched,0,sizeof(switched));
        int cur_on = 0;
        for(int ctr1=0;ctr1<s.length();ctr1++) {
            if(ctr1>=k) {
                cur_on -= switched[ctr1-k];
            }
            if (ctr1 + k <= s.length()){
                if(((s[ctr1] == '+') + cur_on) & 1)
                    continue;
                switched[ctr1] = 1;
                rez++;
                cur_on++;
            } else {
                if(!(((s[ctr1] == '+') + cur_on) & 1)){
                    rez = -1;
                }
            }
        }
        if(rez == -1) {
            fout<<"Case #"<<T-t<<": IMPOSSIBLE\n";
            cout<<"Case #"<<T-t<<": IMPOSSIBLE\n";
            continue;
        }
        fout<<"Case #"<<T-t<<": "<<rez<<"\n";
        cout<<"Case #"<<T-t<<": "<<rez<<"\n";
    }

    fin.close();
    fout.close();
    return 0;
}
