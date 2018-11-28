#include <bits/stdc++.h>
using namespace std;

map<long long, long long> mp1, mp2;
map<long long, long long>::iterator it;
map<long long, long long>::reverse_iterator rit, it2;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, N, K, cas, x, y, t;
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #" << cas << ": ";
        cin >> N >> K;
        mp2.clear();
        mp2[N] = 1;
        while(K){
            mp1.clear();
            
            /*cout << "Map 1\n";
            for(it=mp1.begin();it!=mp1.end();it++){
                cout << it->first << ": " << it->second << '\n';
            }
            
            cout << "Map 2\n";
            for(it=mp2.begin();it!=mp2.end();it++){
                cout << it->first << ": " << it->second << '\n';
            }
            */
            for(it2=mp2.rbegin();it2!=mp2.rend();it2++){
            
                x = (it2->first-1)/2;
                y = (it2->first-1) - x;
                
                //cout << "K=" << K << " it2->first=" << it2->first << " it2->second=" << it2->second << '\n';
                
                if(K<=it2->second){
                    K = 0;
                    //cout << "x=" << x << " y=" << y << '\n';
                    break;
                }
                else K -= it2->second;
                
                it = mp1.find(x);
                if(it!=mp1.end()) it->second += it2->second;
                else mp1[x] = it2->second;
                
                it = mp1.find(y);
                if(it!=mp1.end()) it->second += it2->second;
                else mp1[y] = it2->second;
            }
            if(!K) break;
            mp2.clear();
            for(it=mp1.begin();it!=mp1.end();it++){
                mp2[it->first] = it->second;
            }
        }
        cout << y << ' ' << x << '\n';
	}
	return 0;
}
