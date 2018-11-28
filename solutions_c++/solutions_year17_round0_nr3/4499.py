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

class segment{
    public:
    long long int amount;///how many stalls in this segment
    long long int number;///how many segments'  "the amount of stalls" is as same as this segment
    segment(){amount=0;number=0;}
    segment(long long int amount_in,long long int number_in){
        amount=amount_in;   number=number_in;
    }
};
void add_segment(vector<segment>& ans,segment tmp){
    bool input = false;
    for(int i=0;i<ans.size();i++){
        if(ans[i].amount==tmp.amount){
            ans[i].number+=tmp.number;
            input = true;
            break;
        }
    }
    if(!input){
        ans.push_back(tmp);
    }
}
void spelt_segment(vector<segment>& ans){
    segment tmp;
    long long int Ls= (ans[0].amount - 1)/2;
    long long int Rs=(ans[0].amount - 1)-((ans[0].amount - 1)/2);

    ans[0].number--;
    if(Ls==Rs) add_segment(ans,segment(Ls,2));
    else{
        add_segment(ans,segment(max(Ls,Rs),1));
        add_segment(ans,segment(min(Ls,Rs),1));
    }

    if(ans[0].number==0){
        ans.erase(ans.begin());
    }

}
void solve(){

    ///input
    long long N=0;
    long long K=0;
    cin>>N>>K;

    ///variable
    vector <segment> ans;///each segment means empty stalls between two people
    segment tmp;
    long long int Ls=0,Rs=0;

    ///initial condition
    tmp.amount=N;        tmp.number=1;
    ans.push_back(tmp);

    for(int i=0;i<K-1;i++){
        spelt_segment(ans);
    }
    Ls= (ans[0].amount - 1)/2;
    Rs=(ans[0].amount - 1)-((ans[0].amount - 1)/2);
    cout<<max(Ls,Rs)<<" "<<min(Ls,Rs)<<endl;
}
int main() {
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("check.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
        solve();
	}

	return 0;
}
