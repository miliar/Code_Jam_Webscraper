//#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<iterator>
#include<unordered_map>
#include<unordered_set>
#include<assert.h>
#include <iomanip>
using namespace std;



ifstream cin("/Users/naginahas/Downloads/A-Large.in");
ofstream cout("/Users/naginahas/Downloads/Ammmmm.txt");

const double mypi = 3.14159265358979323;

bool cmp(pair <int,int> pi1,pair <int,int> pi2){
    return 2.0*mypi *double(pi1.first) *double(pi1.second) > 2.0*mypi*double(pi2.first)*pi2.second;
}


int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        
        int N,K;
        cin >> N >> K;
        int R, H;
        vector <pair <int,int> > cyls;
        for(int i=0;i<N;i++){
            cin >> R >> H;
            cyls.push_back(make_pair(R,H));
        }
        double bestsum =0;;
        for(int i=0;i<N;i++){
            vector <pair <int,int> >vp = cyls;
            pair <int,int> pi = vp[i];
            vp.erase(vp.begin()+i);
            sort(vp.begin(),vp.end(),cmp);
            vector <pair <int,int> > cand;
            cand.push_back(pi);
            for(int i=0;i<K-1;i++){
                cand.push_back(vp[i]);
            }
            double sum = 0;
            int mx = 0;
            for(int j=0;j<K;j++){
                sum += 2*mypi*double(cand[j].first)*cand[j].second;
                mx = max(mx,cand[j].first);
            }
            
            
            sum += 1.0*mx*1.0 *mx*mypi;
            bestsum = max(sum,bestsum);
            
        }
        
        
        
       
        
        cout << "Case #" << t+1 << ": "  << fixed << setprecision(10)<< bestsum  <<endl;
    }
    return 0;
}
