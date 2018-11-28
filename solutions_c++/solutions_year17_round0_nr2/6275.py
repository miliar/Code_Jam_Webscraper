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
   
    int t;
    cin>>t;
    for(int aaa = 1; aaa <= t; aaa++){
        cout<<"Case #"<<aaa<<": ";
        long long n;
        cin>>n;
        string s = to_string(n);
        
        int lasti = 0;
        int flag = 0;
        for(int i = 1; i < s.size(); i++){
            if(s[i-1] > s[i]){
                lasti = i-1;
                flag = 1;
                break;
            }
            
        }
        
        if(!flag){
            cout<<n<<endl;
        }
        else if(lasti == 0){
            if(s[lasti] - '0' -1!= 0){
                cout<<--s[lasti];
            }
            for(int i = 0; i < s.size()-1; i++){
                cout<<'9';
            }
            cout<<endl;
        }
        /*else if(s[lasti] != '1'){
            s[lasti]--;
            for(int i = lasti+1; i < s.size(); i++){
                s[i] = '9';
            }
            cout<<s<<endl;
        }*/
        else{
            //cerr<<lasti<<endl;

            while(lasti >= 0){
                if(s[lasti-1] <= s[lasti]-1){
                    break;
                }
                lasti--;
            }
            //cerr<<lasti<<endl;
            if(lasti == -1){
                
                for(int i = 0; i < s.size()-1; i++){
                    cout<<'9';
                }
                cout<<endl;
            }
            else{
                s[lasti]--;
                for(int i = lasti+1; i < s.size(); i++){
                    s[i] = '9';
                }
                long long p = stoll(s);
                cout<<p<<endl;
            }
            
        }
        
    }
    
    return 0;
}
