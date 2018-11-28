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
 bool check(string s){
 	for(int i=0;i<s.length();i++){
 		if(s[i]=='-'){
 			return false;
 			break;
		 }
	 }
	 return true;
 }
 
int main(){
				freopen("A-large (2).in","r",stdin);
				freopen("output.txt","w",stdout);
	ll t;
	sf(t);
	rep (tt,1,t){
		  string s;
		  int l;
		  cin>>s>>l;
		  int k=0;
		  int n=s.length();
		for(int i=0;i<n-l+1;i++){
			if(s[i]=='-'){
				k++;
				for(int j=i;j<i+l;j++){
				   if(s[j]=='-'){
				   	s[j]='+';
				   }
				   else{
				   	s[j]='-';
				   }	
				}
			}
		}
		if(!check(s)){
		
			cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
		}
		else {
			
			cout<<"Case #"<<tt<<": "<<k<<endl;
		}
		  
	}
return 0;
}
