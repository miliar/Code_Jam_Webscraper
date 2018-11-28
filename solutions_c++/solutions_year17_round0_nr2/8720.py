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


int valid(int inp){
        int lest = inp %10;
        while(inp>0) {
                if(inp%10>lest) return 0;
                lest = inp%10;
                inp/=10;
                
        }
        return 1;
}

int main()
{		

        int n, k;
        freopen("output.out","w",stdout);
        cin>>n;
        fa(i,0,n){
                cin>>k;
                int ans = 1;
                fa(j,1,k+1) if(valid(j)) ans = j;
                cout << "Case #" << i + 1 << ": " << ans << "\n";
        }

}