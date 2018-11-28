#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<cstring>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<climits>
#include<string>
#include<sstream>
#include<cmath>
#include<cctype>
#include<iomanip>
#include<list>
#include<conio.h>

using namespace std;

typedef pair <int, int> PII;
typedef pair <int, double> PID;
typedef pair <double, double> PDD;
typedef vector <int> VI;
typedef vector <double> VD;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define MP make_pair
#define PB push_back
#define PPB pop_back
#define PF push_front
#define PPF pop_front
#define EL endl
#define CO cout



void solve(){
    ///variables
    vector<int> state;///pan_cake_state
    int possible=0;
    int step_used=0;
    

    ///input
    string S;
    cin >> S;

    int K=0;
    cin>>K;

    ///solution
    for(int i=0;i<S.size();i++){
        if(S[i]=='+'){
        	state.push_back(0);
        }
        else if(S[i]=='-'){
        	state.push_back(1);
        }else{
        	state.push_back(-1000);
        }
    }

    for(int i=0;i<state.size()-K+1;i++){
        state[i]%=2;
        if(state[i]==1){
            step_used++;
            for(int j=0;j<K;j++){
                state[i+j]=(state[i+j]+1)%2;
            }
        }
    }

    for(int i=state.size()-K+1;i<state.size();i++){
        possible+=state[i];
    }
    if(possible==0){
        cout<<step_used<<endl;
    }else if(possible>0){
        cout<<"IMPOSSIBLE"<<endl;
    }else{
        cout<<"error"<<endl;
    }

}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
        solve();
	}

	getch();
	return 0;
}
