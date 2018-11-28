#include <cmath>
#include <queue>
#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
#include <stack>
#include <climits>
#include <assert.h>
#include <set>
#include <queue>
#include <algorithm>

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
   
    int t, it;
    cin>>t;
    it = t;
    while(t--){
        
        string s;
        cin>>s;
        int k;
        cin>>k;
        int flag = 0;
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '-'  && i + k <= s.size()){
                for(int j = i; j < i + k; j++){
                    if(s[j] == '+'){
                        s[j] = '-';
                    }
                    else{
                        s[j] = '+';
                    }
                }
                count++;
                //cout<<i<<" "<<s<<endl;
            }
            if(s[i] == '-' && i + k > s.size()){
                cout<<"Case #"<<it-t<<": IMPOSSIBLE"<<endl;
                flag = 1;
                break;
            }
        }
        if(!flag){
            cout<<"Case #"<<it-t<<": "<<count<<endl;
        }
        
        
    }
    
    return 0;
}
