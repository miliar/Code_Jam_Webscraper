#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <string.h>

#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

// Input macros
#define s(n)                        scanf("%d",&n)
#define p(n)                        printf("%d\n",n)
#define pl(n)                       printf("%lld\n",n);
#define INF                         (int)1e9
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define mod 1000000007LL

// Useful container manipulation / traversal macros
#define all(n)                      for(int i=0;i<n;i++)
#define alls(m)                     for(int j=0;j<m;j++)
#define rep(a,n)                    for(int i=a;i<n;i++)
#define each(v, c)               	for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all1(a)                     a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define init(Arr) memset((Arr), 0, sizeof (Arr))


int cases,a,b,c,d,i,j,k,n,m,t,ar[1000001],flag,w[1010][1010],cur=0,ans,pre =-1;
string ch,ch2;
pii p;
char str[10000];
bool myfunction (int i,int j) { return (i<j); }


void  solve(){

//cout<<pre;
if(pre ==1)
{
	if(b>=c){
		ch[k]='Y';
		pre =2;
		b--;
	}
	else{
		ch[k]='B';
		pre =3;
		c--;

	}
	return;

}

if(pre ==2){
	if(a>=c){
		ch[k]='R';
		pre =1;
		a--;
	}
	else{
		ch[k]='B';
		pre =3;
		c--;

	}
	return;

}

if(pre ==3){

//cout<<a<<b;
	if(a>=b){
		ch[k]='R';
		pre =1;
		a--;
	}
	else{
		ch[k]='Y';
		pre =2;
		b--;

	}
	return ;

}

}


int main()
{
   
     freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout); 
     cin>>cases;
    
    for(t=1;t<=cases;t++)
    {
     
       printf("Case #%d: ",t); 
    	cin>>n;
        for(i=0;i<6;i++)
        {
        	cin>>ar[i];
        		
        }

		a =0;
        for(i=0;i<6;i++)
        	if(ar[i]>=a)
        		a=ar[i];

        	if(a>(n/2)){
        		cout<<"IMPOSSIBLE\n";
        	}

        	else{

        		a=ar[0];
        		b=ar[2];
        		c=ar[4];
				//int pre = -1;
        			
        		pre =-1;
        		k=0;	
        				
				for(i=0;i<1;i++){

        			if(a>=b&&a>=c&&a!=pre){
        			//	cout<<'R';
        				ch[k]='R';
        				a--;
        				pre =1;
        				continue;
        			}	

        			if(b>=c&&b>=a&&b!=pre){
        				ch[k]='Y';
        				b--;
        				pre =2;
        				continue;
        			}

        			if(c>=a&&c>=b&&c!=pre){
        			ch[k]='B';
        			c--;
        			pre=3;
        			}

        		}
        		
        		//cout<<pre;
        		for(i=1;i<n;i++){
        		//cout<<a<<b<<c<<"\n";
        			k++;
              		solve();
        	}
        	if(ch[0]==ch[n-1])
        	{
        		
        		ch[n-1]=ch[n-2];
        		ch[n-2] =ch[0];
        	}
        		for(i=0;i<n;i++)
        		cout<<ch[i];
        	

        	cout<<"\n";
        	}
    }
        
    
return 0;   
		
}