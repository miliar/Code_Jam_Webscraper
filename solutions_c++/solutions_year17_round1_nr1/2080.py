#include <bits/stdc++.h>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

using namespace std;


typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;
const int N = 100001;
const int MOD = 1e9 + 7;

int main(int argc, const char * argv[]) {
    freopen("inputlarge.in","r",stdin);
    freopen("outputlarge.out","w",stdout);
    int t;
    cin>>t;
    for(int tc = 0; tc < t; tc++){
        int r,c;
        cin>>r>>c;
        string cake[r];
        for(int i = 0; i < r; i++){
            cin>>cake[i];
        }
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(cake[i][j] != '?'){
                    for(int z = 0; z < c && (cake[i][z] == '?' || cake[i][z] == cake[i][j] || z < j); z++){
                        if(z < j && cake[i][z] == '?'){
                            cake[i][z] = cake[i][j];
                        }
                        else if(z > j && cake[i][z] == '?'){
                            cake[i][z] = cake[i][j];
                        }
                    }
                }
            }
        }

        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(cake[i][j] != '?'){
                    for(int z = 0; z < r && (cake[z][j] == '?' || cake[z][j] == cake[i][j] || z < i); z++){
                        if(z < i && cake[z][j] == '?'){
                            cake[z][j] = cake[i][j];
                        }
                        else if(z > i && cake[z][j] == '?'){
                            cake[z][j] = cake[i][j];
                        }
                    }
                }
            }
        }

        cout<<"Case #"<<tc+1<<": "<<endl;
        for(int i = 0; i < r;i++){
            cout<<  cake[i] <<endl;
        }


    }
    return 0;
}
