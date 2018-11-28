#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define INF INT_MAX/2
#define PI 3.14159265358979323846264338327950
#define reset(a,x) memset(a,x,sizeof(a))

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define vi vector<int> 
#define vii vector<ii>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(c) (c).begin,(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define rep(a,b,c)   for(int (a)=(b); (a)<(c); (a)++)
#define repn(a,b,c)  for(int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for(int (a)=(b); (a)>=(c); (a)--)

int moves[8][2]={{-1,0},{1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
bool issafe(int i,int j){
    return (i>=0 && i<8 && j>=0 && j<8);
}

int main(){
	int t;
	string n;
	cin>>t;
	repn(test,1,t){
		cin>>n;
		int nine=n.length();	
		for(int i=n.length()-2;i>=0;i--){
			if(n[i]>n[i+1]){
				n[i]--;
				nine=i+1;
			}
		}
		for(int j=nine;j<n.length();j++)
			n[j]='9';
		printf("Case #%d: ",test);
		for(int i=0;i<n.length();i++){
			if(n[i]!='0')
				cout<<n[i];
		}
		cout<<endl;
	}

	return 0;
}

