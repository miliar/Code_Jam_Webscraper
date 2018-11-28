#include <bits/stdc++.h>

using namespace std;

/* Template Begins */

#define FOR(i,N) FORR(i, 0, N)
#define FORR(i,a,b) FOTR(i, a, b, 1)
#define FOTR(i,a,b,c) for(int i=(a);i<(b);i+=(c))
#define FOREACH(it, x) for(__typeof__((x).begin()) it=(x).begin();it!=(x).end();it++)
#define MEM(a,x) memset(a,x,sizeof(a))
#define BCHK(a,x) (((a)>>(x))&1)
#define BSET(a,x) ((a)|(1<<(x)))
#define BCLR(a,x) ((a)&(~(1<<(x))))
#define BTGL(a,x) ((a)^(1<<(x)))
#define FMT(...) (sprintf(CRTBUFF, __VA_ARGS__)?CRTBUFF:0)
#define read() freopen("input.txt","r",stdin)
#define write() freopen("output.txt","w",stdout)
#define cpp_io() {ios_base::sync_with_stdio(false);cin.tie(NULL);}
#define BUFFSIZE 30000
#define INF 1000000000
#define MOD 1000000007
#define MAX 200000
#define pb push_back
#define mkpr make_pair
#define pii pair<int, int>
typedef long long ll;

char CRTBUFF[BUFFSIZE];

#define dbg(args...) {cout<<"-->";debugger::call(#args,args);cout<<"\n";}
struct debugger {
	static void call(const char* it) {}
	template<typename T, typename ... aT>
	static void call(const char* it, T a, aT... rest) {
		string b;
		for (; *it&&*it != ','; ++it) if (*it != ' ')b += *it;
		cout << b << "=" << a << " ";
		call(++it, rest...);
	}
};

/* Template Ends */

string tidy(string st){
    int i;
    for(i=1; i<st.size(); i++){
        if(st[i]>st[i-1]){
            st[i]--;
            if(st[i]<='0'){
                if(i<st.size()-1){
                    st[i+1]--;
                    st[i] = '9';
                }
                else st[i]='0';
            }
            for(int j=i-1; j>=0; j--)st[j]='9';
        }
    }
    if(st[i]<'0')st[i]='0';
    reverse(st.begin(), st.end());
    return st;
}

ll toLL(string s){
    ll ret;
    stringstream ss;
    ss.str(s);
    ss>>ret;
    return ret;
}

int main(){
	read();
	write();
	//cpp_io();

    int T, cs;
    cin>>T;
    string num1, num2;
    for(cs=1; cs<=T;cs++){
        cin>>num1;
        reverse(num1.begin(), num1.end());
        string s1 = tidy(num1);
        cout<<"Case #"<<cs<<": "<<toLL(s1)<<"\n";
    }
	return 0;
}


