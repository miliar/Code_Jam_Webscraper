#include <bits/stdc++.h> 
using namespace std   ;
#define vi vector<int> 
#define vli vector < long long int> 
#define ii pair<int,int>
#define lii pair<long long int,long long int> 
#define vii vector <ii> 
#define vlii vector <lii> 
#define pb push_back 
#define mp make_pair
#define F first 
#define S second 
#define lli long long int 
#define loop(A,B,C) for(A=B;A<C;A++) 
#define fio ios_base::sync_with_stdio(false) 
#define inf 1000000007 
#define linf 9223372036854700007 
#define ll endl 

int main() 
{
	fio ; 
    int t , i  ;
    cin>>t  ;
    loop(i , 1 , t+1)
    {
    	lli d , n ,  j   ; 
    	cin>>d>>n; 
    	double ans=0 , temp2 , temp1 , temp ; 
    	loop(j , 0 , n )
    	{
    		cin>>temp>>temp1  ; 
    		temp2  = (d-temp)/temp1  ; 
    		ans = max(temp2 , ans) ; 
    	}
    	ans = d/ans  ; 
    	cout<<fixed<<setprecision(6);  
    	cout<<"Case #"<<i<<": "<<ans<<endl ; 
    }

	return 0 ;
}