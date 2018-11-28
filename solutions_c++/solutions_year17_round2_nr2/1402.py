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

using namespace std;



ifstream cin("/Users/naginahas/Downloads/B-small-attempt0.in");
ofstream cout("/Users/naginahas/Downloads/Bzzzzzz.txt");




int main(int argc, const char * argv[]) {
    
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        //
        int N, R, O, Y, G, B,  V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        if (R > N/2 || O > N /2 || Y >N/2 || B  >N/2 ||  V> N/2 || G>N/2){
            cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        string s;
        vector <char > vc (N);
        vector <pair <int, char> >  vpic;
        pair <int, char> pic;;
        pic.first  = R;
        pic.second = 'R';
        vpic.push_back(pic);
        pic.first  = O;
        pic.second = 'O';
        vpic.push_back(pic);
        pic.first  = Y;
        pic.second = 'Y';
        vpic.push_back(pic);
        pic.first  = G;
        pic.second = 'G';
        vpic.push_back(pic);
        pic.first  = B;
        pic.second = 'B';
        vpic.push_back(pic);
        pic.first  = V;
        pic.second = 'V';
        vpic.push_back(pic);
        sort(vpic.begin(),vpic.end());
        reverse(vpic.begin(),vpic.end());
        int k=0;
        for(int i=0;i<vpic.size();i++){
            for(int j=0;j<vpic[i].first;j++){
                vc[k] = vpic[i].second;
                k = (k+2);
                if(k>=N) k = 1;
            }
        }
        for(int i=0;i<N;i++) s+=vc[i];
        cout << "Case #" << t+1 << ": " << s << endl;
    }
    return 0;
}

