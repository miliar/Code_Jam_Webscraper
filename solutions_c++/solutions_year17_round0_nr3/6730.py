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
#define ft                          first
#define sd                          second
#define pq                          priority_queue

#define st string
#define ld long double
 
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
int slate[1120];

pair<int, int > fille(int lim){
        int lef[1013], rig[1123];
        fa(i,1,lim) if(slate[i] == 0) lef[i] = lef[i-1]+1;
        else lef[i] = 0;
        for(int i = lim; i>0; i--) if(slate[i] == 0) rig[i] = rig[i+1]+1;
                else rig[i] = 0;
        pair<int, int >bedd, tedd;
        fa(i,0,lim){
                if(min(lef[i],rig[i])>bedd.ft and slate[i]!=1 ) {
                        bedd.ft = min(lef[i],rig[i]);
                        bedd.sd = i;
                }
        }
        fa(i,0,lim){
                if(max(lef[i],rig[i])>tedd.ft and min(lef[i],rig[i]) == bedd.ft and slate[i]!=1) {
                        tedd.ft = max(lef[i],rig[i]);
                        tedd.sd = i;
                }
        }
        int multa = 0;
        fa(i,0,lim) if(min(lef[i],rig[i]) == bedd.ft) multa++;
        //   trace(bedd,tedd,multa);
        if(multa>1) slate[tedd.sd] = 1;
        else slate[bedd.sd] = 1;
        //  fa(i,0,lim ) cout << slate[i];
        return mp(tedd.ft,bedd.ft);
}



int main(){
	ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int n,k,t;
	freopen("output1.out","w",stdout);
	cin>>t;
	for(int f=1;f<=t;f++){
		cin>>n>>k;
		 fa(i,0,n+2) slate[i]= 0;
         slate[0]= 1;
         slate[n+1] = 1;
         pair<int,int > ans;
         fa(i,0,k) ans = fille(n+2);
         cout << "Case #" << f<< ": " << ans.ft-1 << " " << ans.sd-1 << "\n";
	}




	return 0;
}