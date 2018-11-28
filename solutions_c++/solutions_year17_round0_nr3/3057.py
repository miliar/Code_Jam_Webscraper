#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
long long n,k,t,sum,ant,act,res,may,men,caso;
map <long long, long long> m[2];
int main()
{
    cin >> t;
    while (t--){
        caso++;
        cin >> n >> k;
        sum = 1;
        res = 0;
        ant = 0;
        act = 1;
        may = men = 0;
        m[ant].clear();
        m[ant][n]++;
        while (sum < k){
            m[act].clear();
            for (map<long long, long long> :: iterator it = m[ant].begin(); it!=m[ant].end();++it){
                long long x = it->first, can = it->second;
                //cout << x << "->" << can << " ";
                if (x%2 == 1){
                    if (x/2>0){
                        m[act][x/2] += can *2;
                        sum+=can*2;
                    }
                } else {
                    if (x/2 > 0){
                        if (m[act].find(x/2) != m[act].end()){
                            m[act][x /2] += can;
                        } else {
                            m[act][x /2] = can;
                        }
                        sum+=can;
                    }
                    if (x/2-1> 0){
                        if (m[act].find(x/2-1) != m[act].end()){
                            m[act][x /2-1] += can;
                        } else {
                            m[act][x /2-1] = can;
                        }
                        sum+=can;
                    }
                }
            }
            //cout << "\n";
            act = (act+1) %2;
            ant = (ant+1)%2;
        }
        for (map<long long, long long> :: iterator it = m[ant].begin(); it!=m[ant].end();++it){
            long long x = it->first, can = it->second;
            //cout << x << "->" << can << " ";
            res += it->second;
            if (sum-res < k){
                if (it->first %2 == 0){
                    may = it->first / 2;
                    men = it->first / 2 -1;
                } else {
                    may = men = it->first /2;
                }
                break;
            }
        }
        //cout << "\n";
        cout << "Case #"<< caso<< ": "<< may << " " << men << "\n";
    }
    return 0;
}
