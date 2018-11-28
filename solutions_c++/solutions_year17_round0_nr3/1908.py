#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int t;
ll n, k, n1, n2, s, c1, c2, tc1, tc2, t1, t2, ans;
int main()
{
    FILE *fp, *fc;
    ifstream fin("C-large.in");
    ofstream fout("out1.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        fin>>n>>k;
        n += 2;
        if(k == 1){
            if(n & 1){
                fout<<"Case #"<<cas<<": "<<n/2 - 1<<" "<<n/2 - 1<<endl;
            }
            else fout<<"Case #"<<cas<<": "<<n/2 - 1<<" "<<n/2 - 2<<endl;
            continue;
        }
        n1 = n/2 + 1;
        if(n & 1)
            n2 = n/2 + 1;
        else n2 = n/2;
        if(k == 2){
            if(n1 & 1){
                fout<<"Case #"<<cas<<": "<<n1/2 - 1<<" "<<n1/2 - 1<<endl;
            }
            else fout<<"Case #"<<cas<<": "<<n1/2 - 1<<" "<<n1/2 - 2<<endl;
            continue;
        }
        if(k == 3){
            if(n2 & 1){
                fout<<"Case #"<<cas<<": "<<n2/2 - 1<<" "<<n2/2 - 1<<endl;
            }
            else fout<<"Case #"<<cas<<": "<<n2/2 - 1<<" "<<n2/2 - 2<<endl;
            continue;
        }
        s = 3;
        c1 = 1;
        c2 = 1;
        while(s < k){
            tc1 = 0;
            tc2 = 0;
            if(n1 > 2){
                if(n1 & 1){
                    t1 = n1/2 + 1;
                    tc1 += c1 * 2;
                }
                else{
                    t1 = n1/2 + 1;
                    tc1 += c1;
                    tc2 += c1;
                }
            }
            if(n2 > 2){
                if(n2 & 1){
                    t2 = n2/2 + 1;
                    tc2 += c2 * 2;
                }
                else{
                    t2 = n2/2;
                    tc2 += c2;
                    tc1 += c2;
                }
            }
            c1 = tc1;
            c2 = tc2;
            n1 = t1;
            n2 = t2;
            s += c1 + c2;
        }
        s -= c1+c2;
        k -= s;
        if(k <= c1){
            ans = n1;
        }
        else ans = n2;
        if(ans & 1)
            fout<<"Case #"<<cas<<": "<<ans/2 - 1<<" "<<ans/2 - 1<<endl;
        else fout<<"Case #"<<cas<<": "<<ans/2 - 1<<" "<<ans/2 - 2<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}



