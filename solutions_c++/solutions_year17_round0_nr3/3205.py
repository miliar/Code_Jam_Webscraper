#include <bits/stdc++.h>

using namespace std;
int main(){

    freopen("porfin.in", "r", stdin);
    freopen( "salida.out", "w", stdout );

    int tc; cin >> tc;
    int c = 0;
    while( tc-- ){

        long long n, k, p; cin >> n >> k;
        priority_queue<long long>pq;
        pair<long long,long long>par;
        map<long long,long long>mp;
        pq.push(n);
        mp[n]++;
        while( k>0 ){

            p = pq.top();
            pq.pop();
            if( p%2LL == 0 ){
                if( mp[ p/2LL ] ){
                    mp[ p/2LL ]+= mp[p];
                }else{
                    pq.push( p/2LL );
                    mp[ p/2LL ] += mp[p];
                }
                if( mp[ p/2LL -1LL ] ){
                    mp[ p/2LL - 1LL ]+=mp[p];
                }else{
                    pq.push( p/2LL -1LL );
                    mp[ p/2LL - 1LL ]+= mp[p];
                }
                par = {p/2LL,p/2LL -1LL};
            }else{
                if( mp[ p/2LL ] ){
                    mp[ p/2LL ]+= mp[p];
                    mp[ p/2LL ]+= mp[p];
                }else{
                    mp[ p/2LL ]+= mp[p];
                    mp[ p/2LL ]+= mp[p];
                    pq.push( p/2LL );
                }
                par = {p/2LL,p/2LL};
            }
            k-= (mp[p]);
            mp[p] = 0;
        }

        cout << "Case #" << ++c << ": ";
        cout << par.first << ' ' << par.second << '\n';
    }
}
