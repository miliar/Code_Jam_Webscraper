/**************************************************
   Had a dream, I was king, I woke up, still king.
***************************************************/
#include <bits/stdc++.h>
using namespace std;
 
#define MOD 						1000000007
#define MAX     					INT_MAX
#define MIN     					INT_MIN
#define pb      					push_back
#define ff    						first
#define ss    						second
#define mp      					make_pair
#define CLR     					clear()
#define ln(a)                       a.length();
#define FOR(i, begin, end)          for (long i = (begin);i<= (end); i ++)
#define set(a)                		memset( a, -1,    sizeof(a) )
#define clr(a)               		memset( a,  0,    sizeof(a) )
#define xx(x) 						cout << '>' << #x << ':' << x << endl;
#define fa(i, begin, end)           for (long i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
 
typedef  long long         	 	 ll;
typedef  map<int, int>           mii;
typedef  map<ll, ll>             mll;
typedef  pair<int,int> 	         pii;
typedef  pair<ll,ll> 	         pll;
 
string Int_String (int a){
    ostringstream temp;
    temp<<a;
    return temp.str();
}
 
int String_Int(string str){
 
return atoi(str.c_str());
 
}

string invert(string inp, int index, int k){
        fa(i,index,index+k) if(inp[i] == '+') inp[i] = '-';
        else inp[i] = '+';
        return inp;
}
string pinvert(string inp, int index, int k){
        fa(i,index-k+1,index+1) if(inp[i] == '+') inp[i] = '-';
        else inp[i] = '+';
        return inp;
}

int clean(string inp){
        int sz = inp.size();
        fa(i,0,sz) if(inp[i]!= '+') return 0;
        return 1;
}

int process(string inp,int k){
        int ans = 0, best = 11234567, n = inp.size();
        string clone = inp;
        fa(i,0, n-k+1) if(inp[i] == '-') {
                inp = invert(inp,i,k);
                ans++;
        }
        if(clean(inp)) best = min(ans,best);
        ans = 0;
        inp = clone;
        for(int i = n-1; i>=k-1; i--) if(inp[i] == '-') {
                        inp = pinvert(inp,i,k);
                        ans++;
                }
        if(clean(inp)) best = min(ans,best);
        return best;
}
int main(){
	ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	ofstream output;
	output.open("1.txt");
	int n,curr=0,k;
	string s;
	cin>>n;
	for(int f=1 ; f<=n ;f++){
		cin>>s>>k;
		 int ans =  process(s,k);
         if(ans == 11234567) output << "Case #" << f << ": " << "IMPOSSIBLE\n";
         else output << "Case #" << f << ": " << ans <<endl;		
	}
	return 0;
}