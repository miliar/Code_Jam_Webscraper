//_______Coder_Dinesh@IIT-ISM_____________
#include<bits/stdc++.h>  //Entire STL
using namespace std;   //Declare classes and function for the STL

//*******MACROS BEGIN ******************************************
#define ll long long int
typedef vector<ll>vi;
typedef vector<vi>vvi;
typedef pair<ll,ll>ii;
#define sz(a) ll((a).size())
#define mp make_pair
#define pb push_back
#define rep(i,a,b) for(ll i=a;i<=b;i++)
#define f first
#define s second
#define sf(n) scanf("%lld",&n)
#define pf(n) printf("%lld \n" ,n)
#define all(c) c.begin(),c.end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())



//*****END OF MACROS*********************************************


//string findDigitsInBinary(int n) {
//            string ans;
//            if (n == 0) return "0";
//            
//            while (n > 0) {
//            int rem = n % 2; 
//            ans.push_back((char)('0' + rem));
//            n /= 2;
//            }
//
//            reverse(ans.begin(), ans.end());
//            return ans;
//        }

//int Solution::cpFact(int A, int B) {
//  while(__gcd(A,B) != 1){
//    A = A / __gcd(A,B);
//  } 
//  return A;
//}

bool find(ll n) {
            vector<int>ans;
            while (n > 0LL) {
            ll rem = n % 10LL; 
            ans.push_back(rem);
            n /= 10LL;
            }
            
            vector<int>v1(ans);
            reverse(ans.begin(),ans.end());
            sort(v1.begin(),v1.end());
            for(int i=0;i<v1.size();i++){
            	if(v1[i]!=ans[i]){
            		return false;
            		break;
				}
			}
			return true;
        }

int main(){
				freopen("B-small-attempt0.in","r",stdin);
				freopen("output.txt","w",stdout);
	ll t;
	sf(t);
	rep (tt,1,t){
		ll n;
		 sf(n);
		 if(n==0LL) return 0;
		 for(ll i=n;i>=1LL;i--){
		 	if(find(i)){
		 		cout<<"Case #"<<tt<<": "<<i<<endl;
		 		break;
			 }
		 }
	
		  
	}
return 0;
}
